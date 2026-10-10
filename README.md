# Yangshuai Wang — academic homepage

个人学术主页，发布地址：https://yangshuaiwang.github.io/ 。基于 Hugo / HugoBlox，静态内容、照片、字体和样式无需 Google 服务即可显示。Google Scholar 和论文出版方链接属于可选外链。

## 内容维护

- `content/_index.md`：首页简介、研究方向、教育、经历、教学摘要及联系方式。
- `data/authors/me.yaml`：姓名、职位、机构、个人链接；调整身份信息时与首页核对。
- `content/publications/*/index.md`：论文、预印本、书稿和博士论文，每篇一个文件。
- `content/teaching.md`：完整教学记录；首页只展示其中最近五条。
- `content/conferences/*/index.md`：报告和会议组织记录。
- `assets/media/authors/me.png`：本地头像。
- `_extraction/source-data.json`、`_extraction/EXTRACTION-TABLE.md`：内容核对记录、原始来源、正式出版信息及待补链接，最近核对日期为 2026-10-10。它们是审计记录，不会自动改写网页。

论文元数据使用 `publication`、`preprint`、`book`、`thesis` 标签明确分类；已接收论文归入 `publication`，并在刊物名称中保留 accepted 状态。`source_order` 按各列表的来源编号降序显示，不使用虚构的具体出版日期排序。`publication_year` 用于页面展示；只知道年份时仅填写 `publication_year` 和 `date_precision: year`，不填写虚构的月日。作者列表中 `me` 会显示并加粗 Yangshuai Wang，其他作者仅显示真实姓名。

更新论文时同时核对题目、作者顺序、刊物、状态、年份和公开链接。将预印本转为已接收论文时直接更新原文件及标签，保留 URL。需要改 URL 时添加 `aliases`。旧条目若仅从 Selected Preprints 列表消失，先标为 `draft: true`，不据此宣称撤稿。不要将编辑部投稿后台地址用作公开论文链接。

Google Sites 仍可手动维护；本仓库不会自动抓取并发布其变动。没有当前 CV PDF 时不展示虚构的下载入口。

页面内容有实质更新时，在对应 Markdown 文件的 front matter 中填写实际修改日 `lastmod: YYYY-MM-DD`。论文列表变更时，同时更新首页、`content/publications/_index.md` 或 `content/preprints.md` 中受影响列表页的 `lastmod`。它表示网页修改时间，与论文出版年份及页面最初的 `date` 分开维护；不要在每次构建时统一刷新未修改页面的日期。

## 本地预览与检查

需要 Hugo Extended **0.164.0**、Go、Node.js，以及项目指定的 **pnpm 10.14.0**。保持 `.npmrc` 的 `node-linker=hoisted`；pnpm 11 的不同配置行为会导致此 Hugo 版本无法解析 Tailwind 启动脚本。

```sh
corepack pnpm@10.14.0 install --frozen-lockfile
hugo server --disableFastRender
```

正式构建与检查：

```sh
hugo --minify --cleanDestinationDir
corepack pnpm@10.14.0 run pagefind
python3 scripts/check_site.py
```

检查器核对完整论文列表的成员与顺序、站内链接和锚点、主要页面标题，以及外部运行时资源。核对记录随内容一起更新后再运行。

## GitHub Pages 发布

仓库为 `YangshuaiWang/YangshuaiWang.github.io`，默认分支为 `master`。`.github/workflows/deploy.yml` 在 `master` / `main` 推送后构建并发布，GitHub 的 Settings → Pages → Source 应使用 GitHub Actions。构建使用锁定的依赖文件；依赖更新应单独检查。

本地源码文件夹可能来自下载的 ZIP，缺少 `.git`；请勿把它当作已连接的仓库直接推送。发布时先与远端最新版本比较，将确认的修改提交到真实仓库。`public/`、`node_modules/`、`resources/` 和本地测试缓存不应提交。

## 搜索引擎验证与站点地图

站点地图地址为 `https://yangshuaiwang.github.io/sitemap.xml`。Google、Bing、百度提供 HTML 标签验证时，将标签中 `content` 属性的值填入 `config/_default/params.yaml` 的 `hugoblox.verification` 对应字段，只填验证码，不粘贴整段 HTML：

| 配置字段 | 构建后生成的 meta name |
|---|---|
| `hugoblox.verification.google` | `google-site-verification` |
| `hugoblox.verification.bing` | `msvalidate.01` |
| `hugoblox.verification.baidu` | `baidu-site-verification` |

当前主题已负责生成这些标签，无需另加脚本或启用访问统计。将含真实验证码的配置部署到 GitHub Pages，确认公开首页源码中的标签正确后，再在对应站长平台完成验证并提交站点地图。验证成功后保留这些配置，供平台后续检查所有权；平台显示的验证及收录状态才是结果依据。

## 已知待补信息

4 个预印本在 Google Sites 中的 arXiv 链接实际指向其他论文，已去掉错误链接并保留论文信息；详见核对记录。部分已接收论文尚未提供公开链接。中文姓名“王阳帅”已由本人确认并加入主页和搜索信息。当前构建不能证明网站在所有中国大陆网络中均可访问。
