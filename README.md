# Yangshuai Wang — academic homepage

个人学术主页，发布地址：https://yangshuaiwang.github.io/ 。基于 Hugo / HugoBlox，静态内容、照片、字体和样式无需 Google 服务即可显示。Google Scholar 和论文出版方链接属于可选外链。

## 内容维护

- `content/_index.md`：首页简介、研究方向、教育、经历、教学摘要及联系方式。
- `data/authors/me.yaml`：姓名、职位、机构、个人链接；调整身份信息时与首页核对。
- `content/publications/*/index.md`：论文、预印本、书稿和博士论文，每篇一个文件。
- `content/teaching.md`：完整教学记录；首页只展示其中最近五条。
- `content/conferences/*/index.md`：报告和会议组织记录。
- `assets/media/authors/me.png`：本地头像。
- `_extraction/source-data.json`、`_extraction/EXTRACTION-TABLE.md`：内容核对记录、原始来源、正式出版信息及待补链接，最近核对日期为 2026-10-24。它们是审计记录，不会自动改写网页。

论文元数据使用 `publication`、`preprint`、`book`、`thesis` 标签明确分类；已接收论文归入 `publication`，并在刊物名称中保留 accepted 状态。`source_order` 按各列表的来源编号降序显示，不使用虚构的具体出版日期排序。`publication_year` 用于页面展示；只知道年份时仅填写 `publication_year` 和 `date_precision: year`，不填写虚构的月日。作者列表中 `me` 会显示并加粗 Yangshuai Wang，其他作者仅显示真实姓名。

更新论文时同时核对题目、作者顺序、刊物、状态、年份和公开链接。将预印本转为已接收论文时直接更新原文件及标签，保留 URL。需要改 URL 时添加 `aliases`。旧条目若仅从 Selected Publications 或 Selected Preprints 列表消失，先标为 `draft: true`，不据此宣称撤稿。不要将编辑部投稿后台地址用作公开论文链接。

Google Sites 仍可手动维护；本仓库不会自动抓取并发布其变动。`content/cv.md` 提供完整 CV，公开 PDF 保存在 `static/files/Yangshuai_Wang_CV.pdf`。2026-10-24 版本来自 Google Sites 当前公开链接，下载内容已核对；更新时保持相同路径。Selected Publications 与 Selected Preprints 仅展示当前精选，完整发表记录请见 CV。

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

## 访问统计

Google Analytics 4 衡量 ID 为 `G-HF4JN6YKF7`，配置在 `config/_default/params.yaml` 的 `hugoblox.analytics.google.measurement_id`。这个编号是公开的网页配置，不是密码。Google Sites 的“设置 → 分析”应使用相同编号；两个网站汇总到同一媒体资源，并按“主机名”区分：GitHub 为 `yangshuaiwang.github.io`，Google Sites 为 `sites.google.com`。

在 [Google Analytics](https://analytics.google.com/) 查看实时访问；日常报表选择日期范围，用“会话数”查看来访次数、“浏览次数”查看页面浏览量，再按国家/地区或城市细分。可在“探索”中组合日期、主机名、国家/地区与这些指标。统计从接入后开始，历史访问不会补录；完整报表可能需要 24–48 小时。地区按网络 IP 估算，VPN、拦截器、Cookie 选择及网络限制可能导致地区偏差或漏记；两个网站的用户数不能直接当作去重后的实际人数。

统计仅在正式构建中加载；本地 `hugo server` 不发送访问。自定义 GA4 partial 使用异步加载，不启用 Google Signals 或广告个性化信号，也不添加额外的出站跳转处理。Google 统计服务不可用时，网页内容仍可正常显示。检查器只允许这个配置编号对应的 GA4 脚本作为外部运行时资源，并检查每个内容页只有一个异步标签。

### 公开统计卡片

两个网站底部展示各自的今日访问、累计访问、国家/地区数量和前五个地区。指标为 GA4 会话数（sessions），不是页面浏览量或去重人数；累计从 2026-10-19 开始。日期使用 GA4 媒体资源的时区，卡片显示数据更新时间。报表有处理延迟，不能当作实时在线人数；过了午夜但尚未刷新时，“今日”会自动改为快照的实际日期。

`scripts/public-analytics/Code.gs` 和 `appsscript.json` 是用户本人 Apps Script 项目的源码，只申请 `analytics.readonly`，固定读取媒体资源 `559511734` 内上述两个主机名。Web 应用以所有者身份执行，允许匿名访问，只输出汇总数字；不接受查询参数，不输出访客标识、IP、账号信息或凭据。脚本缓存结果 30 分钟。不要把 OAuth token 或任何私钥放进仓库。

在 Apps Script 编辑器启用 Analytics Data 高级服务并完成只读授权，部署为 Web 应用后，将 `/exec` URL 填入 `config/public-stats.json`。更新脚本时需要将 Web 应用切换到新版本。`scripts/fetch_public_stats.py` 验证返回数据并只保留公开字段，写入 `data/visitor_stats.json` 和 `static/visitor-stats.json`。`.github/workflows/deploy.yml` 每小时第 23 分钟触发构建发布；GitHub 调度可能延迟，长期没有仓库活动时也可能暂停，届时在 Actions 中重新启用。也可手动运行发布工作流。

读取失败时优先保留线上最后一个有效快照，不会把失败变成零访问。若尚无任何有效快照，卡片显示等待连接。展示卡片使用 GitHub Pages 本地资源，不要求访客连接 Google 报表服务；但 GA4 本身被网络或浏览器拦截时，访问可能漏记。

Google Sites 的全站页脚通过“嵌入 → 网址”使用 `https://yangshuaiwang.github.io/site-statistics/google-sites/`。这个独立页面不加载 GA4，以免每次打开 Google Sites 都被额外计作 GitHub 访问。修改后需在 Google Sites 发布。

处理逻辑检查：`node --test scripts/tests/public-analytics.test.cjs` 和 `python3 -m unittest discover -s scripts/tests -p 'test_*.py'`；构建后 `python3 scripts/check_site.py` 还会检查页脚卡片和嵌入页无统计标签。

## 已知待补信息

4 个预印本在 Google Sites 中的 arXiv 链接实际指向其他论文，已去掉错误链接并保留论文信息；详见核对记录。部分已接收论文尚未提供公开链接。中文姓名“王阳帅”已由本人确认并加入主页和搜索信息。当前构建不能证明网站在所有中国大陆网络中均可访问。
