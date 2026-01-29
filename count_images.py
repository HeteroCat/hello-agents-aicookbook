#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统计所有章节文件中的图片数量
"""

import os
import re

def count_images_in_file(md_file):
    """统计 Markdown 文件中的图片数量"""
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 统计图片引用数量
    images = re.findall(r'!\[([^\]]*)\]\([^)]+\)', content)
    return len(images)

def main():
    base_dir = r"C:\Users\h1930\Desktop\个人\AI应用开发\已上线项目\hello-agents-aicookbook"
    os.chdir(base_dir)

    total_images = 0
    chapter_stats = {}

    # 处理所有 16 个章节
    for chapter_num in range(1, 17):
        chapter_dir = f"chapter{chapter_num}"

        if not os.path.exists(chapter_dir):
            continue

        # 查找目录中的所有 .md 文件
        md_files = [f for f in os.listdir(chapter_dir) if f.endswith('.md')]

        chapter_total = 0
        file_stats = {}

        for md_filename in md_files:
            md_file = os.path.join(chapter_dir, md_filename)
            count = count_images_in_file(md_file)
            if count > 0:
                file_stats[md_filename] = count
                chapter_total += count

        if chapter_total > 0:
            chapter_stats[chapter_num] = {
                'total': chapter_total,
                'files': file_stats
            }
            total_images += chapter_total

    # 打印统计结果
    print("=" * 80)
    print("图片引用统计")
    print("=" * 80)

    for chapter_num in sorted(chapter_stats.keys()):
        stats = chapter_stats[chapter_num]
        print(f"\n章节 {chapter_num}:")
        print(f"  总计: {stats['total']} 个图片引用")
        for filename, count in sorted(stats['files'].items()):
            print(f"    - {filename}: {count} 个")

    print("\n" + "=" * 80)
    print(f"总计: {total_images} 个图片引用")
    print("=" * 80)

if __name__ == "__main__":
    main()
