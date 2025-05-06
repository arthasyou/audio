import argparse
import os

from utils import analyze_speech_segments, cut_audio_segments


def main():
    parser = argparse.ArgumentParser(description="批量分析并切割音频文件")
    parser.add_argument("-i", "--input", required=True, help="输入音频目录")
    parser.add_argument("-o", "--output", required=True, help="输出根目录")
    args = parser.parse_args()

    input_dir = args.input
    output_root = args.output

    for filename in os.listdir(input_dir):
        if not filename.lower().endswith((".mp3", ".wav")):
            continue

        audio_path = os.path.join(input_dir, filename)
        name_without_ext = os.path.splitext(filename)[0]
        output_dir = os.path.join(output_root, name_without_ext)

        print(f"\n🎧 正在处理音频: {filename}")
        segments = analyze_speech_segments(audio_path)

        print("✂️ 切割中...")
        cut_audio_segments(audio_path, segments, output_dir)

    print("\n✅ 所有音频处理完成！")


if __name__ == "__main__":
    main()
