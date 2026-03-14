import magic
from pathlib import Path


def get_file_info(file_path: str | Path) -> dict:
    path = Path(file_path).resolve()

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")

    mime = magic.Magic(mime=True)
    mime_type = mime.from_file(str(path))

    return {
        "filename": path.name,
        "size_bytes": path.stat().st_size,
        "extension": path.suffix.lstrip(".").lower(),
        "mime_type": mime_type,
        "path": str(path),
    }