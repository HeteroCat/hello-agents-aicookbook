#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复图片路径中的重复目录问题
"""

import os
import re

def fix_image_paths(md_file):
    """修复 Markdown 文件中的图片路径"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 匹配重复的目录路径，如 /images/X-figures/X-figures/xxx.png
    pattern = r'\!\[([^\]]*)\]\(/images/(\d+)-figures/\2-figures/([^)]+)\)'
    replacement = r'![\1](/images/\2-figures/\3)'

    content = re.sub(pattern, replacement, content)

    if content != original_content:
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    base_dir = r"C:\Users\h1930\Desktop\个人\AI应用开发\已上线项目\hello-agents-aicookbook"
    os.chdir(base_dir)

    fixed_count = 0

    # 处理所有章节
    for chapter_num in range(1, 17):
        chapter_dir = f"chapter{chapter_num}"
        if not os.path.exists(chapter_dir):
            continue

        # 查找目录中的 .md 文件
        for filename in os.listdir(chapter_dir):
            if filename.endswith('.md'):
                md_file = os.path.join(chapter_dir, filename)
                if fix_image_paths(md_file):
                    print(f"修复: {md_file}")
                    fixed_count += 1

    print(f"\n总计: 修复了 {fixed_count} 个文件")

if __name__ == "__main__":
    main()
