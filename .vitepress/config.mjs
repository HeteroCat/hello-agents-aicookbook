import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/runtime-config
export default defineConfig({
  // 站点配置
  title: 'Hello-Agents',
  description: '从零开始构建智能体系统原理与实践教程',
  lang: 'zh-CN',
  base: '/',
  head: [
    ['link', { rel: 'icon', href: '/favicon.ico' }],
    ['meta', { name: 'theme-color', content: '#3c8772' }],
    // Giscus
    ['script', {
      src: 'https://giscus.app/client.js',
      'data-repo': 'datawhalechina/Hello-Agents',
      'data-repo-id': 'R_kgDONF_mUw',
      'data-category': 'General',
      'data-category-id': 'DIC_kwDONF_m84CkpY3S',
      'data-mapping': 'pathname',
      'data-strict': '0',
      'data-reactions-enabled': '1',
      'data-emit-metadata': '0',
      'data-input-position': 'bottom',
      'data-theme': 'light',
      'data-lang': 'zh-CN',
      'data-loading': 'lazy',
      crossOrigin: 'anonymous',
      async: true
    }]
  ],

  // 主题配置
  themeConfig: {
    // 导航栏
    nav: [
      { text: '首页', link: '/' },
      { text: '前言', link: '/前言' },
      { text: '在线阅读', link: 'https://datawhalechina.github.io/hello-agents/' }
    ],

    // 侧边栏
    sidebar: [
      {
        text: '入门',
        items: [
          { text: 'Hello-Agents', link: '/' },
          { text: '前言', link: '/前言' }
        ]
      },
      {
        text: '第一部分：智能体与语言模型基础',
        collapsed: false,
        items: [
          { text: '第一章 初识智能体', link: '/chapter1/第一章-初识智能体' },
          { text: '第二章 智能体发展史', link: '/chapter2/第二章-智能体发展史' },
          { text: '第三章 大语言模型基础', link: '/chapter3/第三章-大语言模型基础' }
        ]
      },
      {
        text: '第二部分：构建你的大语言模型智能体',
        collapsed: false,
        items: [
          { text: '第四章 智能体经典范式构建', link: '/chapter4/第四章-智能体经典范式构建' },
          { text: '第五章 基于低代码平台的智能体搭建', link: '/chapter5/第五章-基于低代码平台的智能体搭建' },
          { text: '第六章 框架开发实践', link: '/chapter6/第六章-框架开发实践' },
          { text: '第七章 构建你的Agent框架', link: '/chapter7/第七章-构建你的Agent框架' }
        ]
      },
      {
        text: '第三部分：高级知识扩展',
        collapsed: false,
        items: [
          { text: '第八章 记忆与检索', link: '/chapter8/第八章-记忆与检索' },
          { text: '第九章 上下文工程', link: '/chapter9/第九章-上下文工程' },
          { text: '第十章 智能体通信协议', link: '/chapter10/第十章-智能体通信协议' },
          { text: '第十一章 Agentic-RL', link: '/chapter11/第十一章-Agentic-RL' },
          { text: '第十二章 智能体性能评估', link: '/chapter12/第十二章-智能体性能评估' }
        ]
      },
      {
        text: '第四部分：综合案例进阶',
        collapsed: false,
        items: [
          { text: '第十三章 智能旅行助手', link: '/chapter13/第十三章-智能旅行助手' },
          { text: '第十四章 自动化深度研究智能体', link: '/chapter14/第十四章-自动化深度研究智能体' },
          { text: '第十五章 构建赛博小镇', link: '/chapter15/第十五章-构建赛博小镇' }
        ]
      },
      {
        text: '第五部分：毕业设计及未来展望',
        collapsed: false,
        items: [
          { text: '第十六章 毕业设计', link: '/chapter16/第十六章-毕业设计' }
        ]
      }
    ],

    // 社交链接
    socialLinks: [
      { icon: 'github', link: 'https://github.com/datawhalechina/Hello-Agents' }
    ],

    // 页脚
    footer: {
      message: '基于 CC BY-NC-SA 4.0 发布',
      copyright: 'Copyright © 2024-present Datawhale'
    },

    // 编辑链接
    editLink: {
      pattern: 'https://github.com/datawhalechina/Hello-Agents/edit/main/docs/:path',
      text: '在 GitHub 上编辑此页'
    },

    // 最后更新时间
    lastUpdated: {
      text: '最后更新',
      formatOptions: {
        dateStyle: 'short',
        timeStyle: 'medium'
      }
    },

    // 大纲标题
    outline: {
      label: '页面导航',
      level: [2, 3]
    },

    // 分页导航
    docFooter: {
      prev: '上一章',
      next: '下一章'
    },

    // 搜索
    search: {
      provider: 'local'
    }
  },

  // Markdown 配置
  markdown: {
    // 代码行号
    lineNumbers: true,

    // 代码高亮
    languages: ['python', 'javascript', 'typescript', 'bash', 'json', 'yaml', 'markdown'],

    // 数学公式
    math: true,

    // 前置 emoji
    theme: {
      light: 'github-light',
      dark: 'github-dark'
    }
  },

  // 构建配置
  build: {
    outDir: '.vitepress/dist',
    assetsDir: 'assets'
  },

  // 忽略死链接
  ignoreDeadLinks: true,

  // 多语言配置
  locales: {
    root: {
      label: '简体中文',
      lang: 'zh-CN'
    },
    en: {
      label: 'English',
      lang: 'en',
      title: 'Hello-Agents',
      description: 'From Zero to Hero: Building Agent Systems',
      head: [
        ['link', { rel: 'icon', href: '/favicon.ico' }],
        ['meta', { name: 'theme-color', content: '#3c8772' }],
        // Giscus
        ['script', {
          src: 'https://giscus.app/client.js',
          'data-repo': 'datawhalechina/Hello-Agents',
          'data-repo-id': 'R_kgDONF_mUw',
          'data-category': 'General',
          'data-category-id': 'DIC_kwDONF_m84CkpY3S',
          'data-mapping': 'pathname',
          'data-strict': '0',
          'data-reactions-enabled': '1',
          'data-emit-metadata': '0',
          'data-input-position': 'bottom',
          'data-theme': 'light',
          'data-lang': 'en',
          'data-loading': 'lazy',
          crossOrigin: 'anonymous',
          async: true
        }]
      ],
      themeConfig: {
        nav: [
          { text: 'Home', link: '/en/' },
          { text: 'Preface', link: '/en/Preface' },
          { text: 'Read Online', link: 'https://datawhalechina.github.io/hello-agents/' }
        ],

        sidebar: [
          {
            text: 'Getting Started',
            items: [
              { text: 'Hello-Agents', link: '/en/' },
              { text: 'Preface', link: '/en/Preface' }
            ]
          },
          {
            text: 'Part 1: Agent and LLM Fundamentals',
            collapsed: false,
            items: [
              { text: 'Chapter 1: Introduction to Agents', link: '/en/chapter1/Chapter1-Introduction-to-Agents' },
              { text: 'Chapter 2: History of Agents', link: '/en/chapter2/Chapter2-History-of-Agents' },
              { text: 'Chapter 3: Fundamentals of Large Language Models', link: '/en/chapter3/Chapter3-Fundamentals-of-Large-Language-Models' }
            ]
          },
          {
            text: 'Part 2: Building Your LLM Agents',
            collapsed: false,
            items: [
              { text: 'Chapter 4: Building Classic Agent Paradigms', link: '/en/chapter4/Chapter4-Building-Classic-Agent-Paradigms' },
              { text: 'Chapter 5: Building Agents with Low-Code Platforms', link: '/en/chapter5/Chapter5-Building-Agents-with-Low-Code-Platforms' },
              { text: 'Chapter 6: Framework Development Practice', link: '/en/chapter6/Chapter6-Framework-Development-Practice' },
              { text: 'Chapter 7: Building Your Agent Framework', link: '/en/chapter7/Chapter7-Building-Your-Agent-Framework' }
            ]
          },
          {
            text: 'Part 3: Advanced Knowledge',
            collapsed: false,
            items: [
              { text: 'Chapter 8: Memory and Retrieval', link: '/en/chapter8/Chapter8-Memory-and-Retrieval' },
              { text: 'Chapter 9: Context Engineering', link: '/en/chapter9/Chapter9-Context-Engineering' },
              { text: 'Chapter 10: Agent Communication Protocols', link: '/en/chapter10/Chapter10-Agent-Communication-Protocols' },
              { text: 'Chapter 11: Agentic RL', link: '/en/chapter11/Chapter11-Agentic-RL' },
              { text: 'Chapter 12: Agent Performance Evaluation', link: '/en/chapter12/Chapter12-Agent-Performance-Evaluation' }
            ]
          },
          {
            text: 'Part 4: Advanced Case Studies',
            collapsed: false,
            items: [
              { text: 'Chapter 13: Intelligent Travel Assistant', link: '/en/chapter13/Chapter13-Intelligent-Travel-Assistant' },
              { text: 'Chapter 14: Automated Deep Research Agent', link: '/en/chapter14/Chapter14-Automated-Deep-Research-Agent' },
              { text: 'Chapter 15: Building Cyber Town', link: '/en/chapter15/Chapter15-Building-Cyber-Town' }
            ]
          },
          {
            text: 'Part 5: Graduation Project and Future',
            collapsed: false,
            items: [
              { text: 'Chapter 16: Graduation Project', link: '/en/chapter16/Chapter16-Graduation-Project' }
            ]
          }
        ],

        socialLinks: [
          { icon: 'github', link: 'https://github.com/datawhalechina/Hello-Agents' }
        ],

        footer: {
          message: 'Released under CC BY-NC-SA 4.0',
          copyright: 'Copyright © 2026-present Datawhale'
        },

        editLink: {
          pattern: 'https://github.com/datawhalechina/Hello-Agents/edit/main/docs/:path',
          text: 'Edit this page on GitHub'
        },

        lastUpdated: {
          text: 'Last Updated',
          formatOptions: {
            dateStyle: 'short',
            timeStyle: 'medium'
          }
        },

        outline: {
          label: 'On this page',
          level: [2, 3]
        },

        docFooter: {
          prev: 'Previous',
          next: 'Next'
        },

        search: {
          provider: 'local'
        }
      }
    }
  },

  // 构建配置
  build: {
    outDir: '.vitepress/dist',
    assetsDir: 'assets'
  }
})
