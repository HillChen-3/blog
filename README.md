# My Blog

A personal blog built with [Pelican](https://getpelican.com/) + [Tailwind CSS](https://tailwindcss.com/), deployed on GitHub Pages.

## Quick Start

```bash
# 安装依赖
pip install -r requirements.txt
npm install

# 开发模式（自动监听 + 热重载）
npm run dev
```

## Writing a New Post

在 `content/articles/` 下创建 Markdown 文件：

```markdown
Title: My Article Title
Date: 2025-12-01 10:20
Category: Python
Tags: fastapi, tutorial
Slug: my-article-slug
Cover: images/my-cover.jpg

Article content here...
```

支持的 frontmatter 字段：
| 字段 | 必填 | 说明 |
|------|------|------|
| `Title` | ✅ | 文章标题 |
| `Date` | ✅ | 发布日期 |
| `Category` | - | 分类（一个） |
| `Tags` | - | 标签（逗号分隔） |
| `Slug` | - | URL 标识（默认取自文件名） |
| `Cover` | - | 封面图片路径（放在 content/images/） |

## Deploy to GitHub Pages

### 第一步：创建仓库

在 GitHub 上创建一个仓库（可以是 `<用户名>.github.io` 用户站点，或任意项目名）。

### 第二步：推送代码

```bash
cd blog
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/<用户名>/<仓库名>.git
git branch -M main
git push -u origin main
```

### 第三步：配置 SITEURL

在 GitHub 仓库中：
1. **Settings → Secrets and variables → Actions → Variables**
2. 点击 **New repository variable**
3. Name: `SITEURL`
4. Value:
   - 用户站点：`https://<用户名>.github.io/`
   - 项目站点：`https://<用户名>.github.io/<仓库名>/`
5. Add variable

### 第四步：配置 GitHub Pages

推送到 `main` 后，GitHub Actions 自动运行。首次运行成功后：
1. **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `gh-pages`，目录: `/ (root)`
4. Save

之后每次 `git push` 到 `main` 都会自动构建和部署。

### 自定义域名

在仓库 Variables 中添加 `CNAME`，值为你的域名。

## 项目自定义

编辑 `pelicanconf.py` 修改：
- `AUTHOR` / `SITENAME` / `SITEDESCRIPTION` — 个人信息
- `SOCIAL` — 社交链接（GitHub/Twitter/LinkedIn）
- `ABOUT_ME` — 主页"关于我"内容
- `TECH_STACK` — 技术栈标签列表
- `MENUITEMS` — 导航菜单
