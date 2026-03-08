# 使用 Vercel Web Analytics

本指南将帮助您开始在项目中使用 Vercel Web Analytics，向您展示如何启用它、将包添加到项目中、将应用部署到 Vercel，以及在仪表板中查看数据。

## 前提条件

- 一个 Vercel 账户。如果您没有账户，可以[免费注册](https://vercel.com/signup)。
- 一个 Vercel 项目。如果您没有项目，可以[创建新项目](https://vercel.com/new)。
- 安装 Vercel CLI。如果没有安装，可以使用以下命令安装：
  
  ```bash
  # 使用 pnpm
  pnpm i vercel
  
  # 使用 yarn
  yarn i vercel
  
  # 使用 npm
  npm i vercel
  
  # 使用 bun
  bun i vercel
  ```

## 在 Vercel 中启用 Web Analytics

在 [Vercel 仪表板](https://vercel.com/dashboard)上，选择您的项目，然后点击 **Analytics** 标签，并从对话框中点击 **Enable**。

> **💡 注意：** 启用 Web Analytics 将在下次部署后添加新路由（作用域为 `/_vercel/insights/*`）。

## 添加 `@vercel/analytics` 到项目

使用您选择的包管理器，将 `@vercel/analytics` 包添加到项目中：

```bash
# 使用 pnpm
pnpm i @vercel/analytics

# 使用 yarn
yarn i @vercel/analytics

# 使用 npm
npm i @vercel/analytics

# 使用 bun
bun i @vercel/analytics
```

## 集成到不同框架

### Next.js (Pages 目录)

`Analytics` 组件是跟踪脚本的封装，提供与 Next.js 的无缝集成，包括路由支持。

如果您使用的是 `pages` 目录，将以下代码添加到主应用文件：

```tsx
// pages/_app.tsx
import type { AppProps } from "next/app";
import { Analytics } from "@vercel/analytics/next";

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <>
      <Component {...pageProps} />
      <Analytics />
    </>
  );
}

export default MyApp;
```

### Next.js (App 目录)

将以下代码添加到根布局：

```tsx
// app/layout.tsx
import { Analytics } from "@vercel/analytics/next";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <title>Next.js</title>
      </head>
      <body>
        {children}
        <Analytics />
      </body>
    </html>
  );
}
```

### Remix

`Analytics` 组件是跟踪脚本的封装，提供与 Remix 的无缝集成，包括路由检测。

将以下代码添加到根文件：

```tsx
// app/root.tsx
import {
  Links,
  LiveReload,
  Meta,
  Outlet,
  Scripts,
  ScrollRestoration,
} from "@remix-run/react";
import { Analytics } from "@vercel/analytics/remix";

export default function App() {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <Meta />
        <Links />
      </head>
      <body>
        <Analytics />
        <Outlet />
        <ScrollRestoration />
        <Scripts />
        <LiveReload />
      </body>
    </html>
  );
}
```

### SvelteKit

`injectAnalytics` 函数是跟踪脚本的封装，提供与 SvelteKit.js 的无缝集成，包括路由支持。

将以下代码添加到主布局：

```ts
// src/routes/+layout.ts
import { dev } from "$app/environment";
import { injectAnalytics } from "@vercel/analytics/sveltekit";

injectAnalytics({ mode: dev ? "development" : "production" });
```

### Nuxt

`Analytics` 组件是跟踪脚本的封装，提供与 Nuxt 的无缝集成，包括路由支持。

将以下代码添加到主组件：

```vue
<!-- app.vue -->
<script setup lang="ts">
import { Analytics } from '@vercel/analytics/nuxt';
</script>

<template>
  <Analytics />
  <NuxtPage />
</template>
```

### Vue

`Analytics` 组件是跟踪脚本的封装，提供与 Vue 的无缝集成。

> **💡 注意：** 如果您使用 `vue-router`，路由支持会自动启用。

将以下代码添加到主组件：

```vue
<!-- src/App.vue -->
<script setup lang="ts">
import { Analytics } from '@vercel/analytics/vue';
</script>

<template>
  <Analytics />
  <!-- your content -->
</template>
```

### Astro

`Analytics` 组件是跟踪脚本的封装，提供与 Astro 的无缝集成，包括路由支持。

将以下代码添加到基础布局：

```astro
---
// src/layouts/Base.astro
import Analytics from '@vercel/analytics/astro';
{/* ... */}
---

<html lang="en">
  <head>
    <meta charset="utf-8" />
    <!-- ... -->
    <Analytics />
  </head>
  <body>
    <slot />
  </body>
</html>
```

> **💡 注意：** `Analytics` 组件在 `@vercel/analytics@1.4.0` 及更高版本中可用。
> 如果您使用的是早期版本，必须在 `astro.config.mjs` 文件中配置 Vercel 适配器的 `webAnalytics` 属性。

```ts
// astro.config.mjs
import { defineConfig } from "astro/config";
import vercel from "@astrojs/vercel/serverless";

export default defineConfig({
  output: "server",
  adapter: vercel({
    webAnalytics: {
      enabled: true, // 使用 @vercel/analytics@1.4.0 时设置为 false
    },
  }),
});
```

### React (Create React App)

`Analytics` 组件是跟踪脚本的封装，提供与 React 的无缝集成。

> **💡 注意：** 使用纯 React 实现时，没有路由支持。

将以下代码添加到主应用文件：

```tsx
// App.tsx
import { Analytics } from "@vercel/analytics/react";

export default function App() {
  return (
    <div>
      {/* ... */}
      <Analytics />
    </div>
  );
}
```

### VitePress

对于 VitePress 项目，在主题配置中注入 Analytics：

```ts
// .vitepress/theme/index.ts
import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import { inject } from '@vercel/analytics'

export default {
  extends: DefaultTheme,
  enhanceApp({ app, router, siteData }) {
    // Inject Vercel Analytics
    inject()
  }
} satisfies Theme
```

### HTML (纯静态网站)

对于纯 HTML 网站，可以将以下脚本添加到 `.html` 文件中：

```html
<!-- index.html -->
<script>
  window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
</script>
<script defer src="/_vercel/insights/script.js"></script>
```

> **💡 注意：** 使用 HTML 实现时，无需安装 `@vercel/analytics` 包。但是，没有路由支持。

### 其他框架

从包中导入 `inject` 函数，它将向您的应用添加跟踪脚本。**这应该只在应用中调用一次，并且必须在客户端运行**。

> **💡 注意：** `inject` 函数没有路由支持。

将以下代码添加到主应用文件：

```ts
// main.ts
import { inject } from "@vercel/analytics";

inject();
```

## 部署应用到 Vercel

使用以下命令部署您的应用：

```bash
vercel deploy
```

我们还建议[连接您项目的 Git 仓库](https://vercel.com/docs/git#deploying-a-git-repository)，这将使 Vercel 能够部署您对 main 分支的最新提交，而无需终端命令。

一旦您的应用部署完成，它将开始跟踪访问者和页面浏览量。

> **💡 注意：** 如果一切设置正确，当您访问任何页面时，应该能够在浏览器的网络选项卡中看到来自 `/_vercel/insights/view` 的 Fetch/XHR 请求。

## 在仪表板中查看数据

一旦您的应用部署完成，并且用户访问了您的网站，您就可以在仪表板中查看数据。

为此，请转到您的[仪表板](https://vercel.com/dashboard)，选择您的项目，然后点击 **Analytics** 标签。

几天的访问者数据后，您将能够开始浏览数据，通过查看和[过滤](https://vercel.com/docs/analytics/filtering)面板。

Pro 和 Enterprise 计划的用户还可以向其数据添加[自定义事件](https://vercel.com/docs/analytics/custom-events)，以跟踪用户交互，如按钮点击、表单提交或购买。

## 隐私和数据合规

了解更多关于 Vercel 如何通过 Vercel Web Analytics 支持[隐私和数据合规标准](https://vercel.com/docs/analytics/privacy-policy)。

## 下一步

现在您已经设置了 Vercel Web Analytics，可以探索以下主题以了解更多信息：

- [了解如何使用 `@vercel/analytics` 包](https://vercel.com/docs/analytics/package)
- [了解如何设置自定义事件](https://vercel.com/docs/analytics/custom-events)
- [了解数据过滤](https://vercel.com/docs/analytics/filtering)
- [阅读隐私和合规性](https://vercel.com/docs/analytics/privacy-policy)
- [探索定价](https://vercel.com/docs/analytics/limits-and-pricing)
- [故障排除](https://vercel.com/docs/analytics/troubleshooting)
