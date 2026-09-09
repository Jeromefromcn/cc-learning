# Claude Code 全功能体验 Roadmap

用一个实验 repo，把 `CLAUDE.md`、`settings.json`、`rules/`、`commands/`、`skills/`、`agents/`、`hooks/`、`.mcp.json` 全部走一遍。每一步都给出「做什么 / 为什么 / 如何验证」。

---

## 第 0 步：建立实验 repo

**做什么**
新建一个小型玩具项目（比如一个简单的 Flask/Express API，或几个 Python 脚本 + 测试），本地 `git init`，确保有基本的目录结构和至少一个可运行的测试命令。

**为什么**
后面所有模块（rules、commands、hooks 等）都需要「有东西可以规范、可以自动化」，一个完全空的仓库没法体验效果。有真实的构建/测试命令，才能验证 hooks 和 commands 是否真的生效。

**如何验证**
- `git status` 能正常显示仓库状态
- 项目自带的测试命令（如 `pytest` / `npm test`）能跑通并返回结果

---

## 第 1 步：生成 CLAUDE.md

**做什么**
在项目根目录运行 `claude` 进入交互模式，执行 `/init`，让 Claude Code 扫描项目并自动生成 `CLAUDE.md` 初稿；再手动补充技术栈、构建/测试命令、目录结构说明、编码约定。

**为什么**
`CLAUDE.md` 是唯一在会话开始时**始终加载**的文件，是所有后续行为的基础上下文。没有它，Claude 每次都要重新猜测项目结构，效率低、容易出错。

**如何验证**
- 打开新会话，问 Claude「这个项目是做什么的、怎么跑测试」，回答应该直接引用 `CLAUDE.md` 里的内容，无需你重新解释
- 检查 `CLAUDE.md` 是否被 git 追踪（说明它会被团队共享）

---

## 第 2 步：配置 settings.json（含最简单的 hook）

**做什么**
创建 `.claude/settings.json`，加入：
1. 基础权限规则：`deny` 读取 `.env`、`deny` 危险命令（如 `rm -rf`）
2. 一个最简单的 `PostToolUse` hook，比如每次 Edit/Write 后 `echo "文件已修改"` 到终端

**为什么**
`settings.json` 控制权限、模型、工具和 hooks，是「安全护栏」所在地。先用一个无害的 echo hook 验证 hooks 机制本身能跑通，比一上来就写复杂的自动化脚本更容易排错。

**如何验证**
- 让 Claude 尝试读取 `.env` 文件，应该被拒绝，并在错误信息里能看到你设的 deny 规则
- 让 Claude 编辑任意文件后，终端应该打印出你在 hook 里设的提示文字

---

## 第 3 步：拆分 rules/

**做什么**
故意把 `CLAUDE.md` 写得臃肿一点（比如把代码风格规范、测试规范、API 约定都塞进去），然后把这些内容分别拆到 `.claude/rules/code-style.md`、`.claude/rules/testing.md` 等独立文件里。

**为什么**
`CLAUDE.md` 会一直占用上下文窗口，内容越多消耗越大。`rules/` 让你可以按主题模块化管理规则，甚至可以针对不同文件路径设置不同规则，避免 `CLAUDE.md` 无限膨胀。

**如何验证**
- 让 Claude 写一段代码，检查它是否遵循了 `rules/code-style.md` 里的具体规范（比如命名风格、注释要求）
- 对比拆分前后 `CLAUDE.md` 的行数变化

---

## 第 4 步：写一个 slash command

**做什么**
在 `.claude/commands/review.md` 里定义一个 `/review` 命令，内容是一段固定的 code review 提示词（检查什么、输出什么格式）。

**为什么**
Commands 是把「你经常手动输入的重复性提示词」封装成一键调用的工作流，避免每次都重新打字、每次措辞不一致。

**如何验证**
- 在会话里直接输入 `/review`，观察 Claude 是否按照 `review.md` 里定义的检查项和输出格式执行，而不需要你补充说明

---

## 第 5 步：写一个 Skill

**做什么**
在 `.claude/skills/commit-message/SKILL.md` 里写一个技能：根据 git diff 自动生成符合 Conventional Commits 规范的 commit message，并在 frontmatter 里写清楚 `description`（触发场景）。

**为什么**
Skill 和 command 的区别在于：command 需要你手动 `/调用`，而 skill 是**根据描述自动判断是否相关并加载**的可复用流程，更适合「不确定什么时候需要，但一旦需要就该自动生效」的场景。

**如何验证**
- 修改一些文件后，直接说「帮我写个 commit message」，不要提及 skill 名字，观察 Claude 是否自动识别并加载了这个 skill（可以在其回复方式或输出格式上看出明显区别）

---

## 第 6 步：配置一个 subagent

**做什么**
在 `.claude/agents/code-reviewer.md` 中定义一个专职的 code-reviewer 子代理，限定它只做代码审查、不做其他任务，并给它单独的系统提示词。

**为什么**
Subagent 有独立的上下文窗口，适合把「范围明确、可能占用大量上下文」的任务委派出去（比如审查一个大 PR），而不污染主对话的上下文。

**如何验证**
- 委派一个审查任务给这个 agent，检查主对话历史里是否只出现了任务结果摘要，而不是完整的审查过程（说明上下文确实被隔离了）

---

## 第 7 步（可选）：接入 MCP

**做什么**
在 `.mcp.json` 里配置一个简单的本地 MCP server（比如官方的 filesystem server），测试 Claude Code 能否通过它读取项目外的指定目录。

**为什么**
`.mcp.json` 用于连接外部工具和团队共享的集成，是把 Claude Code 的能力扩展到仓库之外的方式。

**如何验证**
- 让 Claude 通过 MCP 工具访问配置的外部目录，确认它能读到该目录下的文件（而不是仅限于当前 repo）

---

## 总览验证表

| 模块 | 验证方式 |
|---|---|
| CLAUDE.md | 新会话直接答对项目背景 |
| settings.json + hook | 危险操作被拦截 / echo 提示出现 |
| rules/ | 生成代码遵循拆分后的规则 |
| commands/ | `/review` 按预期格式输出 |
| skills/ | 无需点名，Claude 自动加载对应技能 |
| agents/ | 主对话上下文未被审查细节污染 |
| .mcp.json | 能访问仓库外的资源 |

走完这七步，图里提到的每个组件你都会有一次真实的动手体验，出问题也不影响任何正式项目。