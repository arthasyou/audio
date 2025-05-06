## 🪟 Windows 使用说明（语音切割工具）

本项目可在 Windows 上运行，推荐使用 `uv` 管理虚拟环境与依赖，结合 Hugging Face 模型，实现语音片段的自动检测与切割。

---

### ✅ 前提要求

1. 安装 [Python 3.10+](https://www.python.org/downloads/)
2. 安装 [uv](https://github.com/astral-sh/uv)（推荐方式管理依赖）
3. 安装 `ffmpeg`（命令行可用）

---

### 🔧 安装步骤（Windows）

#### 1. 安装 uv

打开 PowerShell 或 CMD：

```bash
pip install uv
```

验证是否成功：

```bash
uv --version
```

---

#### 2. 初始化虚拟环境并安装依赖

```bash
uv venv
uv pip install pyannote.audio ffmpeg-python huggingface_hub
```

---

#### 3. 安装 ffmpeg（必须）

- 访问：[https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
- 推荐下载 “Windows builds from gyan.dev”
- 解压后将 `bin` 文件夹路径加入系统环境变量 `PATH` 中（确保 `ffmpeg` 命令在命令行可用）

验证：

```bash
ffmpeg -version
```

---

#### 4. Hugging Face 认证 & 协议接受

##### ① 注册账号：[https://huggingface.co/join](https://huggingface.co/join)

##### ② 获取 Access Token：[https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

##### ③ 登录：

```bash
huggingface-cli login
```

> 粘贴 token 回车

##### ④ 接受模型协议：

访问以下页面并点击 “Access repository”：

- [https://huggingface.co/pyannote/voice-activity-detection](https://huggingface.co/pyannote/voice-activity-detection)
- [https://huggingface.co/pyannote/segmentation](https://huggingface.co/pyannote/segmentation)

---

### ▶️ 使用示例

1. 将音频文件（`.mp3` 或 `.wav`）放入 `audio/` 文件夹

2. 命令行执行（在项目目录下）：

```bash
uv run main.py -i audio -o outputs
```

这将会自动：

- 遍历 `audio/` 目录下的音频文件；
- 分析并切割语音段；
- 每个音频生成一个独立的输出文件夹如：

  ```
  outputs/
  ├── test1/
  │   ├── segment_001.mp3
  │   └── ...
  ```

---

### 📌 常见问题排查

| 问题                       | 解决方案                                  |
| -------------------------- | ----------------------------------------- |
| `ffmpeg: not found`        | 检查 ffmpeg 是否正确安装并加入环境变量    |
| 模型下载失败               | 确认已登录 Hugging Face，且已接受模型协议 |
| `NoneType is not callable` | 是模型未正确加载，常因协议未接受          |
