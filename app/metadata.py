import json
import subprocess
from pathlib import Path

IMAGE_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}
VIDEO_EXTENSIONS = {"mp4", "mov"}

def extract_metadata(file_path: str | Path) -> dict:
    
    path = Path(file_path).resolve()
    
    if not path.exists():
        raise FileExistsError(f"File not found: {file_path}")
    
    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")
    
    extension = path.suffix.lstrip(".").lower()
    
    if not extension in IMAGE_EXTENSIONS:
        return extract_image_metadata(path)
    
    if extension in VIDEO_EXTENSIONS:
        return extract_video_metadata(path)
    
    raise ValueError(f"Unsupported file type: {extension}")

def extract_image_metadata(path: Path) -> dict:
    
    cmd = ["exiftool", "-json", str(path)]
    
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=True,
    )
    
    data = json.loads(result.stdout)[0]
    
    return {
        "format": data.get("FileType"),
        "width": data.get("ImageWidth"),
        "height": data.get("ImageHeight"),
        "creation_date": data.get("CreateDate"),
        "modification_date": data.get("ModifyDate"),
        "software": data.get("Software"),
        "camera_make": data.get("Make"),
        "camera_model": data.get("Model"),
        "gps": data.get("GPSPosition"),
        "color_profile": data.get("ColorSpace"),
    }
    
def extract_video_metadata(path: Path) -> dict:
    
    cmd = [
        "ffprobe",
        "-v",
        "quiet",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        str(path),
    ]
    
    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=True,
    )
    
    data = json.loads(result.stdout)
    
    video_stream = next(
        (s for s in data.get("streams", []) if s.get("codec_type") == "video"),
        {}
    )
    
    audio_stream = next(
        (s for s in data.get("streams", []) if s.get("codec_type") == "audio"),
        {}
    )
    
    return {
        "container_format": data.get("format", {}).get("format_name"),
        "video_codec": video_stream.get("codec_name"),
        "audio_codec": audio_stream.get("codec_name"),
        "width": video_stream.get("width"),
        "height": video_stream.get("height"),
        "duration": data.get("format", {}).get("duration"),
        "frame_rate": video_stream.get("r_frame_rate"),
        "bit_rate": data.get("format", {}).get("bit_rate"),
        "encoder": data.get("format", {}).get("tags", {}).get("encoder"),
    }