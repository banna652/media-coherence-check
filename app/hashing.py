import hashlib
from pathlib import Path

CHUNK_SIZE = 8192

def compute_sha256(file_path: str | Path) -> str:
    
    path = Path(file_path).resolve()
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")
    
    sha256 = hashlib.sha256()
    
    with path.open("rb") as f:
        while chunk := f.read(CHUNK_SIZE):
            sha256.update(chunk)
    
    return sha256.hexdigest()