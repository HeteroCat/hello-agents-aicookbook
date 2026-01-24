// Default theme
import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import { h } from 'vue'
import './styles/custom.css'

// Giscus 组件
const GiscusComment = () => {
  return h('div', { class: 'giscus-wrapper' }, [
    h('script', {
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
    })
  ])
}

export default {
  extends: DefaultTheme,
  Layout: () => {
    return h(DefaultTheme.Layout, null, {
      // 在内容之后添加 Giscus 评论
      'doc-after': () => h(GiscusComment)
    })
  },
  enhanceApp({ app, router, siteData }) {
    // 可以在这里添加全局组件或其他增强
  }
} satisfies Theme
