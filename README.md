# deepseek-playground

这是一个由 AI 维护的 GitHub 仓库，用于探索自动同步、远程协作和跨平台文件管理。

## 项目简介

本仓库是一个实验性的自动同步仓库，由 DeepSeek 通过 `write_file` 工具持续写入本地文件，再通过 `upload.py` 脚本上传到 GitHub。目标是测试 AI 能否作为“远程协作者”独立维护一个真实的代码仓库。

## 目录结构

```
.
├── README.md              # 项目说明（本文件）
├── hello.txt              # 初次问候
├── hello_world.py         # Python 示例脚本
├── upload.py              # GitHub 上传脚本（从环境变量读取 Token）
├── examples/              # 示例代码目录
│   └── greet.py          # 打招呼脚本（随机问候语）
└── notes/                # 笔记目录
    ├── ideas.md          # 想法和待办记录
    ├── daily.md          # 日记
    └── quote.txt         # 名言摘录
```

## 核心功能

- **自动同步**：AI 通过 `write_file` 将文件写入本地目录，再由 `upload.py` 推送到远程仓库，形成闭环。
- **跨设备协作**：你可以在任何设备上编辑本地仓库，运行脚本即可同步到 GitHub。
- **无需手动 Git 命令**：上传脚本封装了 `git add/commit/push`，简化操作。

## 使用方式

### 1. 克隆仓库

```bash
git clone https://github.com/qwc2009/deepseek-playground.git
cd deepseek-playground
```

### 2. 设置环境变量

在终端中设置 GitHub 个人访问令牌（需要 `repo` 权限）：

```bash
export GITHUB_TOKEN=你的token
```

### 3. 运行上传脚本

```bash
python upload.py
```

脚本会自动扫描本地文件，上传所有非隐藏、非 `.git` 目录下的文件到远程仓库。

### 4. 由 AI 持续维护

DeepSeek 会不定期向本仓库写入新内容（如代码、笔记、配置等），你只需定期运行 `python upload.py` 即可同步最新内容。

## 已实现功能

- [x] 基础文件上传（支持文本文件、代码文件）
- [x] 环境变量读取 Token（安全）
- [x] 跳过 `.git` 目录和隐藏文件
- [x] 支持子目录结构（`examples/`、`notes/`）
- [x] AI 自动写入新内容

## 待办

- [ ] 添加定时自动同步（cron / systemd timer）
- [ ] 支持二进制文件上传（图片、压缩包）
- [ ] 实现冲突检测与自动合并

## 技术栈

- **语言**：Python 3
- **依赖**：`requests`
- **API**：GitHub REST API
- **环境**：Termux / Linux / Windows（支持 Python 3）

## 常见问题

### Q：Token 权限不足怎么办？

确保在生成 Token 时勾选了 `repo` 全部权限。如果 Token 已过期，重新生成即可。

### Q：上传失败并返回 403 错误？

可能原因：
- Token 权限不足（检查 `repo` 权限）
- Token 已过期（重新生成）
- 文件名包含特殊字符（重命名后重试）

### Q：如何添加新文件？

直接在本仓库目录下创建文件，或由 AI 通过 `write_file` 工具写入，然后运行 `python upload.py` 即可。

## 贡献

本仓库由 DeepSeek 与用户共同维护。如果你有好的想法，欢迎提 Issue 或直接修改后 Push。

## 许可证

MIT License

---

*最后更新：2026-08-22*
