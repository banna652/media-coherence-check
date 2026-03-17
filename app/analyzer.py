from datetime import datetime
from pathlib import Path

from app.fileinfo import get_file_info
from app.hashing import compute_sha256
from app.metadata import extract_metadata

from app.rules import (
    check_extension_mime_consistency,
    check_metadata_presence,
    check_timestamp_presence,
    check_timestamp_consistency,
    check_encoder_presence,
)

from app.flags import generate_flags
from app.scoring import calculate_score

IMAGE_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}
VIDEO_EXTENSIONS = {"mp4", "mov"}

class MediaAnalyzer:
    
    def analyze(self, file_path: str | Path) -> dict:
        path = Path(file_path)
        
        file_info = get_file_info(path)
        sha256_hash = compute_sha256(path)
        metadata = extract_metadata(path)
        
        extension = file_info["extension"]
        
        if extension in IMAGE_EXTENSIONS:
            media_type = "image"
        elif extension in VIDEO_EXTENSIONS:
            media_type = "video"
        else:
            media_type = "unknown"
            
        structural_checks = {
            "extension_mime_match": check_extension_mime_consistency(
                file_info["extension"],
                file_info["mime_type"],
            ),
            "metadata_present": check_metadata_presence(metadata),
            "timestamp_present": check_timestamp_presence(metadata),
            "timestamp_consistent": check_timestamp_consistency(metadata),
            "encoder_present": check_encoder_presence(metadata),
        }
        
        flags = generate_flags(structural_checks, metadata)

        score = calculate_score(flags)
        
        analysis_result = {
            "analysis_version": "0.1",
            "analysis_timestamp": datetime.utcnow().isoformat(),
            "input_file": file_info,
            "hashes": {
                "sha256": sha256_hash,
            },
            "media_type": media_type,
            "technical_metadata": metadata,
            "structural_checks": structural_checks,
            "flags": flags,
            "score": score,
        }
        
        return analysis_result