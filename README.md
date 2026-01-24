# Hello-Agents-aicookbook 智能体学习平台



![Hello-Agents Logo](https://img.shields.io/badge/Hello--Agents-智能体学习平台-blue?style=for-the-badge&logo=robot)

🤖 **Hello-Agents 教程的HTML版本学习平台**

从基础理论到实际应用，全面掌握多智能体系统的设计与实现

[![GitHub stars](https://img.shields.io/github/stars/datawhalechina/Hello-Agents?style=social)](https://github.com/datawhalechina/Hello-Agents)
[![GitHub forks](https://img.shields.io/github/forks/datawhalechina/Hello-Agents?style=social)](https://github.com/datawhalechina/Hello-Agents)
[![Language](https://img.shields.io/badge/Language-中文-red)](README.md)



## 📖 目录

- [项目介绍](#-项目介绍)
- [快速开始](#-快速开始)
- [你将收获什么](#-你将收获什么)
- [内容导航](#-内容导航)
- [项目结构](#-项目结构)
- [技术实现](#-技术实现)
- [本地运行](#-本地运行)
- [贡献指南](#-贡献指南)
- [许可证](#-许可证)

## 🎯 项目介绍

如果说2024年是"百模大战"的元年，那么2025年无疑开启了"Agent元年"。技术的焦点正从训练更大的基础模型，转向构建更聪明的智能体应用。然而，当前系统性、重实践的教程却极度匮乏。

**Hello-Agents** 是一个系统性的智能体学习教程，旨在"授人以渔"。本项目包含：

- 📚 **完整的理论教程**：从智能体基础概念到高级应用
- 💻 **交互式学习平台**：现代化的Web界面，支持章节导航
- 🛠️ **实战代码示例**：手把手实现经典智能体架构
- 🌐 **在线阅读体验**：无需安装，即开即用

教程将带领你穿透框架表象，从智能体的核心原理出发，深入其核心架构，理解其经典范式，并最终亲手构建起属于自己的多智能体应用。

## 🚀 快速开始

### 在线阅读
🌐 **立即开始** - 访问在线版本，无需下载，随时随地学习

### 本地运行
```bash
# 1. 克隆项目
git clone https://github.com/datawhalechina/Hello-Agents.git
cd Hello-Agents

# 2. 启动本地服务器
python -m http.server 8000

# 3. 在浏览器中访问
# http://localhost:8000
```

## ✨ 你将收获什么？

| 收获 | 描述 |
|------|------|
| 📖 **Datawhale 开源免费** | 完全免费学习本项目所有内容，与社区共同成长 |
| 🔍 **理解核心原理** | 深入理解智能体（Agent）的构件、原则与经典范式 |
| 🏗️ **亲手实现** | 编码复现 ReAct、Plan-and-Solve 等经典智能体架构 |
| 🛠️ **掌握高级技能** | 学习并应用上下文工程、RAG、工具使用等前沿技术 |
| 🤝 **构建多智能体** | 掌握多智能体协作、通信与评估的核心方法 |
| 🚀 **驱动真实案例** | 实战开发智能旅行助手、自动化研究员等综合项目 |

## 📚 内容导航

### 第一部分：智能体与语言模型基础
- **前言** - 项目的缘起、背景及读者建议 ✅
- **第一章** - 初识智能体：定义、类型、范式与应用 ✅
- **第二章** - 智能体发展史：从符号主义到 LLM 驱动的演进 ✅
- **第三章** - 大语言模型基础：Transformer、提示、主流LLM及其局限 ✅

### 第二部分：构建你的大语言模型智能体
- **第四章** - 智能体经典范式构建：手把手实现 ReAct、Plan-and-Solve、Reflection ✅
- **第五章** - 基于低代码平台的智能体搭建：Coze、n8n等商业化平台使用 ✅
- **第六章** - 框架开发实践：AutoGen、AgentScope、LangGraph 等主流框架应用 ✅
- **第七章** - 构建你的Agent框架：从0开始构建智能体框架 ✅

### 第三部分：高级知识扩展
- **第八章** - 记忆与检索：记忆系统, RAG, 图\向量数据库 ✅
- **第九章** - 上下文工程：持续交互的"情境理解" ✅
- **第十章** - 智能体通信协议：MCP, A2A, ANP 等协议解析 ✅
- **第十一章** - 多智能体系统：协作、通信、博弈论与 AI Society ✅
- **第十二章** - 智能体性能评估：核心指标、基准测试与评估框架 ✅

### 第四部分：综合案例进阶
- **第十三章** - 智能旅行助手：RAG与多智能体协作的真实世界应用 ✅
- **第十四章** - 自动化深度研究智能体：DeepResearch Agent 复现与解析 🚧
- **第十五章** - 构建赛博小镇：Agent 与游戏的结合，模拟社会动态 ✅

### 第五部分：毕业设计及未来展望
- **第十六章** - 毕业设计：构建属于你的完整多智能体应用 🚧

> ✅ 已完成 | 🚧 建设中

## 📁 项目结构

```
hello-agents-aicookbook/
├── README.md                    # 项目说明文档
├── index.html                   # 主页面HTML文件
├── styles.css                   # 样式文件
├── content/                     # 原始内容文件
│   ├── helloagent.md           # Hello-Agents介绍
│   ├── 前言.md                  # 前言内容
│   ├── 第一章 初识智能体.md      # 第一章内容
│   ├── 第二章 智能体发展史.md    # 第二章内容
│   └── 第三章 大模型基础.md      # 第三章内容
├── test/                        # 渲染后的HTML文件
│   ├── helloagent.html         # 主介绍页面
│   ├── 前言.html                # 前言页面
│   ├── 第一章_初识智能体.html    # 第一章页面
│   ├── 第二章_智能体发展史.html  # 第二章页面
│   └── 第三章_大模型基础.html    # 第三章页面
└── .figma/                      # 设计资源
    └── image/                   # 图标和图片资源
```

## 🛠️ 技术实现

### 技术栈
- **前端**: HTML5 + CSS3 + JavaScript (ES6+)
- **样式**: Tailwind CSS + 自定义CSS
- **图标**: Font Awesome
- **服务器**: Python HTTP Server (开发环境)

### 核心功能
- **响应式设计**: 支持桌面端和移动端
- **深色主题**: 现代化的深色配色方案
- **动态内容加载**: 使用 Fetch API 动态加载章节内容
- **章节导航**: 侧边栏导航，支持章节状态显示
- **交互式界面**: 悬停效果、动画过渡

### 浏览器兼容性
- Chrome 60+
- Firefox 60+
- Safari 12+
- Edge 79+

## 🖥️ 本地运行

### 环境要求
- Python 3.6+ (用于启动本地服务器)
- 现代浏览器

### 运行步骤
1. **克隆项目**
   ```bash
   git clone https://github.com/datawhalechina/Hello-Agents.git
   cd Hello-Agents
   ```

2. **启动服务器**
   ```bash
   # 使用 Python 3
   python -m http.server 8000
   
   # 或使用 Python 2
   python -m SimpleHTTPServer 8000
   ```

3. **访问应用**
   - 打开浏览器访问 `http://localhost:8000`
   - 默认显示 Hello-Agents 介绍页面
   - 点击左侧菜单可切换不同章节

## 🤝 贡献指南

我们欢迎所有形式的贡献！

### 如何贡献
1. **Fork** 本项目
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 **Pull Request**

### 贡献类型
- 📝 **内容贡献**: 完善教程内容、修正错误
- 🐛 **Bug修复**: 修复界面或功能问题
- ✨ **新功能**: 添加新的交互功能
- 🎨 **界面优化**: 改进用户体验和视觉设计
- 📚 **文档完善**: 改进文档和注释

### 开发规范
- 使用语义化的提交信息
- 保持代码风格一致
- 添加必要的注释和文档
- 确保跨浏览器兼容性

## 📄 许可证

本项目采用 [MIT License](LICENSE) 开源协议。

## 🙏 致谢

感谢 [Datawhale](https://github.com/datawhalechina) 开源社区的支持，以及所有贡献者的努力！

---



**⭐ 如果这个项目对你有帮助，请给我们一个 Star！**

**⭐ Power by [HeteroCat](https://github.com/HeteroCat)**

[🏠 返回首页](https://github.com/datawhalechina/Hello-Agents) | [📖 开始学习](http://localhost:8000) | [💬 加入讨论](https://github.com/datawhalechina/Hello-Agents/discussions)

