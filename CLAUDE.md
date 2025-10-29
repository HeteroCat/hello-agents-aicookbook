# CLAUDE.md

此文件为 Claude Code (claude.ai/code) 在此代码库中工作时提供指导。

## 项目概述

Hello-Agents-aicookbook 是一个基于静态HTML的教育平台，用于学习AI智能体和多智能体系统。它是 Datawhale 的 Hello-Agents 教程的HTML版本，提供现代化的交互式Web界面，用于从基础理论到实际实现地学习智能体系统。

## 常用命令

### 开发环境
```bash
# 启动本地开发服务器
npm run dev
# 或
python -m http.server 8000

# 备用启动命令
npm start

# 构建（静态站点 - 无需构建过程）
npm run build
```

### 访问应用
- 启动服务器后访问 `http://localhost:8000`
- 入口文件是 `index.html`，包含主要的学习平台界面

## 架构和结构

### 静态站点架构
这是一个纯静态网站，没有构建过程或服务器端渲染。架构包括：

- **单页应用**: `index.html` 是动态加载内容的主容器
- **静态内容服务**: 所有章节内容预渲染为独立的HTML文件
- **客户端导航**: JavaScript处理章节间的动态内容加载

### 关键目录
- `html/` - 渲染的章节HTML文件（preface.html、chapter1.html、chapter2.html、chapter3.html、helloagent.html）
- `HTML-FULL/` - 章节的完整独立HTML版本（备用格式）
- `.figma/image/` - 静态资源，包括logo和图标
- `docs/` - 附加文档

### 内容结构
平台遵循结构化的教程格式：
- **介绍**: 主要概述（`helloagent.html`）
- **前言**: 项目背景和读者指导（`preface.html`）
- **章节**: 顺序学习内容（chapter1.html到chapter3.html，计划更多章节）

### 技术实现
- **前端**: 纯HTML5 + CSS3 + 原生JavaScript（ES6+）
- **样式**: 自定义CSS，现代化深色主题（`styles.css`）
- **导航**: 基于侧边栏的章节导航，带加载状态
- **内容加载**: 动态fetch API加载章节内容
- **响应式设计**: 兼容移动端和桌面端

### 部署配置
- **Vercel**: 配置静态站点构建设置（`vercel.json`）
- **缓存**: 为静态资源和HTML文件优化缓存头
- **清洁URL**: 配置清洁URL路由

## 开发注意事项

### 添加新内容
1. 在 `html/` 目录中按照命名约定创建新的HTML文件
2. 在 `index.html` 中更新导航以包含新章节
3. 确保内容遵循既定的样式和结构模式

### 静态资源管理
- 所有图像和图标存储在 `.figma/image/`
- CSS整合在 `styles.css` 中
- 无JavaScript构建过程 - 所有脚本内联或在主HTML文件中

### 内容格式
每个章节HTML应遵循既定的模板结构，以保持样式和导航的一致性。