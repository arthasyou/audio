# 步骤1：分析音频中有语音的段落
from utils import analyze_speech_segments, cut_audio_segments


def main():
    audio_path = "audio/test.mp3"  # 你可以换成其他路径
    output_dir = "outputs/segments"

    print("🎧 分析语音段落...")
    segments = analyze_speech_segments(audio_path)

    print("✂️ 开始切割音频...")
    cut_audio_segments(audio_path, segments, output_dir)

    print("✅ 所有操作完成！")


if __name__ == "__main__":
    main()
