#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为章节 Markdown 文件添加图片引用
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
            # 移除 "图 X.X " 或 "表 X.X " 前缀，保留描述部分
            desc_match = re.match(r'[图表]\s+\d+\.\d+\s+(.+)', desc_text)
            if desc_match:
                description = desc_match.group(1)
            else:
                description = desc_text

            images.append({
                'filename': filename,
                'description': description,
                'full_desc': desc_text
            })

    return images

def find_chapter_markdown(chapter_num):
    """查找章节对应的 Markdown 文件"""
    chapter_dir = f"chapter{chapter_num}"

    if not os.path.exists(chapter_dir):
        return None

    # 查找目录中的 .md 文件
    for file in os.listdir(chapter_dir):
        if file.endswith('.md'):
            return os.path.join(chapter_dir, file)

    return None

def add_images_to_markdown(md_file, images, chapter_num):
    """在 Markdown 文件中添加图片引用"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False
    changes = []

    for img in images:
        # 查找描述文字（可能前面有空格和换行）
        # 匹配格式：单独一行的描述文字
        patterns = [
            # 匹配前面有空白和换行的描述
            rf'(^\s*\n\s*{re.escape(img["full_desc"])}\s*\n)',
            # 匹配只有空格然后是描述
            rf'(^\s*{re.escape(img["full_desc"])}\s*\n)',
            # 匹配在 div 中的描述
            rf'(^\s*<div[^>]*>\s*\n\s*{re.escape(img["full_desc"])}\s*\n\s*</div>)',
        ]

        for pattern in patterns:
            match = re.search(pattern, content, re.MULTILINE)
            if match:
                # 构建图片引用
                # filename 已经包含了目录部分（如 1-figures/xxx.png），所以不需要再加 {chapter_num}-figures
                if '/' in img['filename']:
                    image_ref = f'\n\n![{img["description"]}](/images/{img["filename"]})\n\n'
                else:
                    image_ref = f'\n\n![{img["description"]}](/images/{chapter_num}-figures/{img["filename"]})\n\n'
                content = content[:match.start()] + image_ref + content[match.end():]
                changes.append(f"添加图片: {img['description']} -> {img['filename']}")
                modified = True
                break

    # 如果没有修改，尝试查找不包含图号前缀的描述
    if not modified or len(changes) < len(images):
        for img in images:
            # 检查是否已经处理过
            if any(img['filename'] in change for change in changes):
                continue

            # 尝试只用描述部分（不含图号）
            desc_only = img['description']
            pattern = rf'(^\s*{re.escape(desc_only)}\s*\n)'
            match = re.search(pattern, content, re.MULTILINE)
            if match:
                # filename 已经包含了目录部分（如 1-figures/xxx.png），所以不需要再加 {chapter_num}-figures
                if '/' in img['filename']:
                    image_ref = f'\n\n![{img["description"]}](/images/{img["filename"]})\n\n'
                else:
                    image_ref = f'\n\n![{img["description"]}](/images/{chapter_num}-figures/{img["filename"]})\n\n'
                content = content[:match.start()] + image_ref + content[match.end():]
                changes.append(f"添加图片: {img['description']} -> {img['filename']}")
                modified = True

    if modified:
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)

    return modified, changes

def main():
    base_dir = r"C:\Users\h1930\Desktop\个人\AI应用开发\已上线项目\hello-agents-aicookbook"
    os.chdir(base_dir)

    total_changes = 0

    # 处理所有 16 个章节
    for chapter_num in range(1, 17):
        html_file = f"docs_html/chapter{chapter_num}.html"
        md_file = find_chapter_markdown(chapter_num)

        if not os.path.exists(html_file):
            print(f"警告: HTML 文件不存在 - {html_file}")
            continue

        if not md_file:
            print(f"警告: 未找到章节 {chapter_num} 的 Markdown 文件")
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
        modified, changes = add_images_to_markdown(md_file, images, chapter_num)

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
