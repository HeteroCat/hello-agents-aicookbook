#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为英文章节 Markdown 文件添加图片引用
"""

import os
import re

def extract_images_from_html(html_file):
    """从 HTML 文件中提取图片引用和描述"""
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    images = []

    # 使用正则表达式查找所有 img 标签
    img_pattern = r'<img[^>]*src="[^"]*images/([^"]+)"[^>]*>'
    img_matches = re.finditer(img_pattern, content)

    for img_match in img_matches:
        filename = img_match.group(1)

        # 从 img 标签位置开始，查找下一个 <p> 标签
        pos_after_img = img_match.end()
        p_pattern = r'<p[^>]*>([^<]+)</p>'
        p_match = re.search(p_pattern, content[pos_after_img:pos_after_img+500])

        if p_match:
            desc_text = p_match.group(1).strip()
            # 提取图号 (例如 "图 5.1")
            figure_num_match = re.search(r'[图表]\s+(\d+\.\d+)', desc_text)
            if figure_num_match:
                figure_num = figure_num_match.group(1)  # 例如 "5.1"
                # 提取描述部分
                desc_match = re.match(r'[图表]\s+\d+\.\d+\s+(.+)', desc_text)
                if desc_match:
                    description = desc_match.group(1)
                else:
                    description = desc_text

                images.append({
                    'filename': filename,
                    'description': description,
                    'full_desc': desc_text,
                    'figure_num': figure_num
                })

    return images

def add_images_to_english_markdown(md_file, images, chapter_num):
    """在英文 Markdown 文件中添加图片引用"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    changes = []

    for img in images:
        figure_num = img['figure_num']  # 例如 "5.1"
        # 在英文 Markdown 中查找 "Figure 5.1" 或 "figure 5.1"
        patterns = [
            # 匹配 "Figure 5.1" 后面跟描述
            rf'([Ff]igure\s+{re.escape(figure_num)}[^\n]*?\n)',
            # 匹配 "(Figure 5.1)" 的引用
            rf'(\([Ff]igure\s+{re.escape(figure_num)}\))',
        ]

        for pattern in patterns:
            # 查找所有匹配
            matches = list(re.finditer(pattern, content))
            if matches:
                # 使用第一个匹配（通常是在描述文字中）
                match = matches[0]
                # 检查是否已经添加了图片
                if '![' in content[max(0, match.start()-50):match.end()+50]:
                    continue

                # 构建图片引用 - 使用中文描述作为 alt 文本
                # filename 已经包含了目录部分（如 5-figures/xxx.png），所以不需要再加 {chapter_num}-figures
                if '/' in img['filename']:
                    image_ref = f'\n\n![{img["description"]}](/images/{img["filename"]})\n\n'
                else:
                    image_ref = f'\n\n![{img["description"]}](/images/{chapter_num}-figures/{img["filename"]})\n\n'
                content = content[:match.end()] + image_ref + content[match.end():]
                changes.append(f"添加图片: Figure {figure_num} -> {img['filename']}")
                modified = True
                break

    if modified:
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)

    return modified, changes

def main():
    base_dir = r"C:\Users\h1930\Desktop\个人\AI应用开发\已上线项目\hello-agents-aicookbook"
    os.chdir(base_dir)

    # 只处理英文章节: 5, 9, 11, 12, 14, 15, 16
    english_chapters = [5, 9, 11, 12, 14, 15, 16]
    total_changes = 0

    for chapter_num in english_chapters:
        html_file = f"docs_html/chapter{chapter_num}.html"
        md_file = f"chapter{chapter_num}"

        # 查找 Markdown 文件
        if not os.path.exists(md_file):
            print(f"警告: 目录不存在 - {md_file}")
            continue

        # 查找目录中的 .md 文件
        md_files = [f for f in os.listdir(md_file) if f.endswith('.md')]
        if not md_files:
            print(f"警告: 章节 {chapter_num} 中未找到 Markdown 文件")
            continue

        md_file = os.path.join(md_file, md_files[0])

        if not os.path.exists(html_file):
            print(f"警告: HTML 文件不存在 - {html_file}")
            continue

        # 提取图片
        images = extract_images_from_html(html_file)

        if not images:
            print(f"章节 {chapter_num}: HTML 中未找到图片引用")
            continue

        print(f"\n章节 {chapter_num}:")
        print(f"  HTML 文件: {html_file}")
        print(f"  Markdown 文件: {md_file}")
        print(f"  找到 {len(images)} 个图片引用")

        # 添加图片到 Markdown
        modified, changes = add_images_to_english_markdown(md_file, images, chapter_num)

        if modified:
            print(f"  成功添加 {len(changes)} 个图片引用:")
            for change in changes:
                print(f"    - {change}")
            total_changes += len(changes)
        else:
            print(f"  未做任何修改（可能已经添加过或找不到匹配的描述）")

    print(f"\n总计: 添加了 {total_changes} 个图片引用")

if __name__ == "__main__":
    main()
