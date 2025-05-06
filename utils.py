import os
import subprocess
from typing import List, Tuple

from pyannote.audio import Pipeline


def analyze_speech_segments(audio_path: str) -> List[Tuple[float, float]]:
    """
    分析音频中有语音的段落（使用 VAD）

    参数:
        audio_path: 音频文件路径

    返回:
        [(start_time, end_time), ...] 的列表，单位为秒
    """
    pipeline = Pipeline.from_pretrained("pyannote/voice-activity-detection")
    vad_result = pipeline(audio_path)

    segments = [(segment.start, segment.end) for segment in vad_result.itersegments()]

    for i, (start, end) in enumerate(segments, 1):
        print(f"第{i:03d}段语音: 开始={start:.2f}s，结束={end:.2f}s")

    return segments


def cut_audio_segments(
    audio_path: str, segments: List[Tuple[float, float]], output_dir: str = "segments"
) -> List[str]:
    """
    根据指定时间段切割音频

    参数:
        audio_path: 音频文件路径
        segments: 语音段列表，每项是 (start_time, end_time)
        output_dir: 切割音频的输出目录

    返回:
        切割后音频文件路径列表
    """
    os.makedirs(output_dir, exist_ok=True)
    output_files = []

    for i, (start, end) in enumerate(segments, 1):
        output_file = os.path.join(output_dir, f"segment_{i:03d}.mp3")

        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i",
                audio_path,
                "-ss",
                str(start),
                "-to",
                str(end),
                "-c",
                "copy",
                output_file,
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

        print(f"✅ 已切割: {output_file}（{start:.2f}s - {end:.2f}s）")
        output_files.append(output_file)

    return output_files
