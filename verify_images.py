#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
验证图片引用并生成报告
"""

import os
import re

def verify_image_paths(md_file):
    """验证 Markdown 文件中的图片路径"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 查找所有图片引用
    images = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content)

    issues = []
    valid_count = 0

    for alt_text, path in images:
        # 检查路径格式
        if path.startswith('/images/'):
            # 检查是否有重复的目录
            if re.search(r'/\d+-figures/\d+-figures/', path):
                issues.append(f"重复目录: {path}")
            # 检查路径是否有效
            else:
                valid_count += 1
        else:
            issues.append(f"路径不以 /images/ 开头: {path}")

    return valid_count, len(images), issues

def main():
    base_dir = r"C:\Users\h1930\Desktop\个人\AI应用开发\已上线项目\hello-agents-aicookbook"
    os.chdir(base_dir)

    print("=" * 80)
    print("图片引用验证报告")
    print("=" * 80)

    total_valid = 0
    total_issues = 0

    # 处理所有 16 个章节
    for chapter_num in range(1, 17):
        chapter_dir = f"chapter{chapter_num}"

        if not os.path.exists(chapter_dir):
            continue

        # 查找目录中的所有 .md 文件
        md_files = [f for f in os.listdir(chapter_dir) if f.endswith('.md')]

        for md_filename in md_files:
            md_file = os.path.join(chapter_dir, md_filename)

            valid_count, total_count, issues = verify_image_paths(md_file)

            if total_count > 0:
                print(f"\n{md_file}:")
                print(f"  有效: {valid_count}/{total_count}")

                if issues:
                    print(f"  问题:")
                    for issue in issues:
                        print(f"    - {issue}")
                    total_issues += len(issues)
                else:
                    print(f"  [OK] 所有图片路径格式正确")

                total_valid += valid_count

    print("\n" + "=" * 80)
    print(f"总计:")
    print(f"  有效图片引用: {total_valid}")
    print(f"  发现问题: {total_issues}")
    print("=" * 80)

if __name__ == "__main__":
    main()
