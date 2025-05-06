## 🗣️ 语音切割工具（基于 pyannote-audio）

本工具可批量处理音频文件，**自动检测语音段落并切割保存**，适用于中泰混合语音的前处理，便于后续 ASR 和语言识别任务。

---

### 📁 项目结构

```
audio/
├── main.py              # 主入口，支持批量分析与切割
├── utils.py             # 封装的分析与切割函数
├── audio/               # 示例输入目录（存放 .mp3 / .wav 文件）
├── outputs/             # 切割结果输出目录，每个音频一个子目录
└── README.md            # 使用说明
```

---

### 🔧 安装依赖（使用 [uv](https://github.com/astral-sh/uv)）

1. 初始化虚拟环境：

   ```bash
   uv venv
   ```

2. 安装所需依赖：

   ```bash
   uv pip install pyannote.audio ffmpeg-python huggingface_hub
   ```

---

### 🔐 Hugging Face 配置

由于 `pyannote-audio` 和其依赖模型为 gated 模型，你需完成以下一次性配置：

1. 注册账号
   👉 [https://huggingface.co/join](https://huggingface.co/join)

2. 登录 Hugging Face CLI：

   ```bash
   huggingface-cli login
   ```

3. 手动接受以下模型协议（必须访问网页点击“Access repository”）：

   - [https://huggingface.co/pyannote/voice-activity-detection](https://huggingface.co/pyannote/voice-activity-detection)
   - [https://huggingface.co/pyannote/segmentation](https://huggingface.co/pyannote/segmentation)

---

### ▶️ 使用方法

准备：

- 将所有音频文件（支持 `.mp3` 和 `.wav`）放入输入目录（如 `audio/`）

运行：

```bash
uv run main.py -i audio -o outputs
```

示例输出结构：

```
outputs/
├── test1/
│   ├── segment_001.mp3
│   ├── segment_002.mp3
│   └── ...
├── test2/
│   ├── segment_001.mp3
│   └── ...
```

---

### ✅ 功能说明

- ✅ 自动静音检测（基于 VAD）
- ✅ 每段语音精准切割（ffmpeg 无损）
- ✅ 每个音频单独输出，便于管理

---

### 💡 后续建议（可拓展）

- 加入语段语言识别（区分中/泰）
- 语者分离（diarization）
- WhisperX + pyannote 联合文本对齐
