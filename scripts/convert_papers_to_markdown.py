#!/usr/bin/env python3
"""
将论文梳理Excel文件转换为markdown笔记的脚本
参考awesome-papers的组织方式
"""

import pandas as pd
from pathlib import Path
import shutil
from datetime import datetime

def read_excel_sheets(excel_path):
    """读取Excel文件的所有sheet"""
    xl = pd.ExcelFile(excel_path)
    sheets_data = {}

    for sheet_name in xl.sheet_names:
        df = pd.read_excel(xl, sheet_name=sheet_name)
        # 替换NaN为空字符串
        df = df.fillna('')
        sheets_data[sheet_name] = df

    return sheets_data

def sheet_to_filename(sheet_name):
    """将sheet名称转换为文件名"""
    # 英文直接小写，中文可以保留或转换
    name_mapping = {
        '推测性解码': 'speculative-decoding',
        'MoE': 'moe',
        'KVCache': 'kv-cache',
        '训推一体': 'unified-training-inference',
        'RL系统': 'rl-systems',
        '存储优化': 'memory-optimization',
        '量化': 'quantization',
        '算子生成': 'operator-generation',
        'agent': 'agents',
        'PD分离': 'prefill-decoding-disaggregation',
        '稀疏': 'sparsity',
        'Serving': 'serving',
        'DiT': 'diffusion-transformers',
        'offload': 'offload',
        '端侧': 'on-device',
        '算子优化': 'operator-optimization'
    }
    return name_mapping.get(sheet_name, sheet_name.lower().replace(' ', '-'))

def create_paper_list_markdown(sheet_name, df):
    """创建论文列表markdown（简洁版）"""
    md_lines = []

    md_lines.append(f"# {sheet_name}\n")
    md_lines.append(f"\n本页面收集了 {sheet_name} 相关的论文及其核心思想。\n")
    md_lines.append(f"\n总共 {len(df)} 篇论文\n")
    md_lines.append("\n---\n\n")

    for idx, row in df.iterrows():
        # 获取论文标题（第一列）
        paper_title = row.iloc[0] if len(row) > 0 else ''
        # 获取idea（第二列）
        idea = row.iloc[1] if len(row) > 1 else ''
        # 获取思考（第三列）
        thinking = row.iloc[2] if len(row) > 2 else ''
        # 获取来源（第四列，如果有的话）
        source = row.iloc[3] if len(row) > 3 else ''

        if not paper_title or not str(paper_title).strip():
            continue

        paper_title = str(paper_title).strip()

        md_lines.append(f"### {paper_title}\n\n")

        if idea and str(idea).strip():
            idea_text = str(idea).strip()
            # 将换行符转换为句号，保持段落格式
            idea_text = idea_text.replace('\n', '\n\n')
            md_lines.append(f"{idea_text}\n\n")

        if source and str(source).strip():
            md_lines.append(f"*来源: {str(source).strip()}*\n\n")

    return '\n'.join(md_lines)

def create_reading_notes_markdown(sheet_name, df):
    """创建阅读笔记markdown（详细版，包含思考）"""
    md_lines = []

    md_lines.append(f"# {sheet_name}\n")
    md_lines.append(f"\n## Meta Info\n\n")
    md_lines.append(f"论文数量: {len(df)}\n")
    md_lines.append(f"更新时间: {datetime.now().strftime('%Y-%m-%d')}\n")
    md_lines.append("\n## Papers\n\n")

    for idx, row in df.iterrows():
        # 获取各列数据
        paper_title = row.iloc[0] if len(row) > 0 else ''
        idea = row.iloc[1] if len(row) > 1 else ''
        thinking = row.iloc[2] if len(row) > 2 else ''
        source = row.iloc[3] if len(row) > 3 else ''

        if not paper_title or not str(paper_title).strip():
            continue

        paper_title = str(paper_title).strip()

        md_lines.append(f"### {paper_title}\n\n")

        if idea and str(idea).strip():
            md_lines.append(f"**核心思想 (Idea)**\n\n")
            idea_text = str(idea).strip()
            idea_text = idea_text.replace('\n', '\n\n')
            md_lines.append(f"{idea_text}\n\n")

        if thinking and str(thinking).strip():
            md_lines.append(f"**思考与备注**\n\n")
            thinking_text = str(thinking).strip()
            thinking_text = thinking_text.replace('\n', '\n\n')
            md_lines.append(f"{thinking_text}\n\n")

        if source and str(source).strip():
            md_lines.append(f"**来源**: {str(source).strip()}\n\n")

        md_lines.append("---\n\n")

    return '\n'.join(md_lines)

def create_readme(sheets_data):
    """创建主README文件"""
    md_lines = []

    md_lines.append("# 论文笔记\n\n")
    md_lines.append('> "Think different." —— Apple Inc.\n\n')
    md_lines.append("本仓库整理了我对AI系统和LLM推理相关论文的笔记。\n\n")

    # 统计信息
    total_papers = sum(len(df) for df in sheets_data.values())
    md_lines.append(f"## 统计信息\n\n")
    md_lines.append(f"- 主题数量: {len(sheets_data)}\n")
    md_lines.append(f"- 论文总数: {total_papers}\n\n")

    # 目录
    md_lines.append("## 主题目录\n\n")

    # 按类别组织
    categories = {
        '推理优化': ['推测性解码', 'PD分离', 'Serving', 'offload'],
        '模型架构': ['MoE', 'DiT', '稀疏'],
        '系统优化': ['KVCache', '存储优化', '量化', '端侧'],
        '训练与编译': ['训推一体', '算子生成', '算子优化'],
        '其他': ['agent', 'RL系统']
    }

    for category, sheet_names in categories.items():
        md_lines.append(f"### {category}\n\n")
        for sheet_name in sheet_names:
            if sheet_name in sheets_data:
                filename = sheet_to_filename(sheet_name)
                count = len(sheets_data[sheet_name])
                md_lines.append(f"- [{sheet_name}]({filename}.md) ({count} 篇论文)\n")
        md_lines.append("\n")

    # 所有主题列表
    md_lines.append("## 所有主题\n\n")
    for sheet_name in sorted(sheets_data.keys()):
        filename = sheet_to_filename(sheet_name)
        count = len(sheets_data[sheet_name])
        md_lines.append(f"- [{sheet_name}]({filename}.md) ({count} 篇论文)\n")

    # 使用说明
    md_lines.append("\n## 使用说明\n\n")
    md_lines.append("1. 在 `paper-list/` 目录中查看简洁的论文列表\n")
    md_lines.append("2. 在 `reading-notes/` 目录中查看详细的阅读笔记（包含思考）\n")
    md_lines.append("3. 修改Excel后运行脚本自动更新: `python scripts/convert_papers_to_markdown.py`\n")

    # 更新日志
    md_lines.append("\n## 更新日志\n\n")
    md_lines.append(f"* {datetime.now().strftime('%Y-%m-%d')}: 初始版本，包含 {len(sheets_data)} 个主题，{total_papers} 篇论文\n")

    # License
    md_lines.append("\n## License\n\n")
    md_lines.append("MIT License\n")
    md_lines.append(f"\nCopyright © {datetime.now().year}\n")

    return '\n'.join(md_lines)

def setup_git_repo(repo_path):
    """初始化git仓库"""
    import subprocess

    if not (repo_path / '.git').exists():
        subprocess.run(['git', 'init'], cwd=repo_path, check=True)
        subprocess.run(['git', 'config', 'user.email', 'paper-notes@example.com'], cwd=repo_path, check=True)
        subprocess.run(['git', 'config', 'user.name', 'Paper Notes'], cwd=repo_path, check=True)

        # 重命名分支为main
        subprocess.run(['git', 'branch', '-m', 'main'], cwd=repo_path, check=True)
        print("✓ Git仓库初始化完成")
    else:
        print("✓ Git仓库已存在")

    # 创建.gitignore
    gitignore_content = """*.xlsx
*.xls
*.pyc
__pycache__/
.DS_Store
*.swp
*.swo
*~
.vscode/
.idea/
"""
    (repo_path / '.gitignore').write_text(gitignore_content)
    print("✓ .gitignore 文件已创建")

def create_summary_md(sheets_data):
    """创建SUMMARY.md（类似GitBook）"""
    md_lines = ["# Summary\n\n"]

    categories = {
        '推理优化': ['推测性解码', 'PD分离', 'Serving', 'offload'],
        '模型架构': ['MoE', 'DiT', '稀疏'],
        '系统优化': ['KVCache', '存储优化', '量化', '端侧'],
        '训练与编译': ['训推一体', '算子生成', '算子优化'],
        '其他': ['agent', 'RL系统']
    }

    for category, sheet_names in categories.items():
        md_lines.append(f"- {category}\n")
        for sheet_name in sheet_names:
            if sheet_name in sheets_data:
                filename = sheet_to_filename(sheet_name)
                md_lines.append(f"  - [{sheet_name}]({filename}.md)\n")
        md_lines.append("\n")

    return '\n'.join(md_lines)

def main():
    # 设置路径
    excel_path = Path('/home/sameta/论文梳理.xlsx')
    repo_path = Path('/home/sameta/paper-notes')

    if not excel_path.exists():
        print(f"错误: Excel文件不存在: {excel_path}")
        return

    # 清理并重新创建目录
    if repo_path.exists():
        shutil.rmtree(repo_path)
    repo_path.mkdir()

    print(f"✓ 创建目录: {repo_path}")

    # 创建子目录
    (repo_path / 'paper-list').mkdir()
    (repo_path / 'reading-notes').mkdir()
    (repo_path / 'scripts').mkdir()
    print("✓ 创建子目录: paper-list/, reading-notes/, scripts/")

    # 读取Excel数据
    print(f"✓ 读取Excel文件: {excel_path}")
    sheets_data = read_excel_sheets(excel_path)
    print(f"  - 共 {len(sheets_data)} 个主题")
    total_papers = sum(len(df) for df in sheets_data.values())
    print(f"  - 共 {total_papers} 篇论文")

    # 为每个sheet创建markdown文件
    for sheet_name, df in sheets_data.items():
        filename = sheet_to_filename(sheet_name)

        # 创建paper-list版本（简洁）
        paper_list_content = create_paper_list_markdown(sheet_name, df)
        (repo_path / 'paper-list' / f'{filename}.md').write_text(paper_list_content, encoding='utf-8')

        # 创建reading-notes版本（详细）
        reading_notes_content = create_reading_notes_markdown(sheet_name, df)
        (repo_path / 'reading-notes' / f'{filename}.md').write_text(reading_notes_content, encoding='utf-8')

        print(f"✓ 创建主题 [{sheet_name}]: {len(df)} 篇论文")

    # 创建README
    readme_content = create_readme(sheets_data)
    (repo_path / 'README.md').write_text(readme_content, encoding='utf-8')
    print("✓ 创建文件: README.md")

    # 创建SUMMARY.md
    summary_content = create_summary_md(sheets_data)
    (repo_path / 'SUMMARY.md').write_text(summary_content, encoding='utf-8')
    print("✓ 创建文件: SUMMARY.md")

    # 复制脚本到scripts目录
    script_content = Path(__file__).read_text(encoding='utf-8')
    (repo_path / 'scripts' / 'convert_papers_to_markdown.py').write_text(script_content, encoding='utf-8')
    print("✓ 创建文件: scripts/convert_papers_to_markdown.py")

    # 初始化git仓库
    setup_git_repo(repo_path)

    print("\n" + "="*60)
    print("转换完成！")
    print("="*60)
    print(f"\n仓库路径: {repo_path}")
    print(f"\n目录结构:")
    print(f"  paper-notes/")
    print(f"  ├── README.md")
    print(f"  ├── SUMMARY.md")
    print(f"  ├── paper-list/")
    print(f"  │   ├── speculative-decoding.md")
    print(f"  │   ├── moe.md")
    print(f"  │   └── ...")
    print(f"  ├── reading-notes/")
    print(f"  │   ├── speculative-decoding.md")
    print(f"  │   ├── moe.md")
    print(f"  │   └── ...")
    print(f"  └── scripts/")
    print(f"      └── convert_papers_to_markdown.py")
    print("\n下一步操作:")
    print(f"  cd {repo_path}")
    print("  git add .")
    print("  git commit -m 'Initial commit: 论文笔记'")
    print("  # 如果需要推送到远程:")
    print("  git remote add origin <your-repo-url>")
    print("  git push -u origin main")

if __name__ == '__main__':
    main()
