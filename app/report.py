import json
from pathlib import Path
from datetime import datetime


def save_json_report(analysis_result: dict, output_dir: str | Path) -> Path:
    
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    filename = f"analysis_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.json"
    file_path = output_path / filename

    with open(file_path, "w") as f:
        json.dump(analysis_result, f, indent=2)

    return file_path


def generate_markdown_report(analysis_result: dict, output_dir: str | Path) -> Path:

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    filename = f"analysis_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}.md"
    file_path = output_path / filename

    file_info = analysis_result["input_file"]
    metadata = analysis_result["technical_metadata"]
    flags = analysis_result["flags"]
    score = analysis_result["score"]

    markdown = f"""
# Media Coherence Analysis Report

## Analysis Overview
- Analysis Version: {analysis_result["analysis_version"]}
- Timestamp: {analysis_result["analysis_timestamp"]}
- Media Type: {analysis_result["media_type"]}

## File Identity
- Filename: {file_info["filename"]}
- File Size: {file_info["size_bytes"]} bytes
- MIME Type: {file_info["mime_type"]}
- SHA256: {analysis_result["hashes"]["sha256"]}

## Technical Metadata
"""

    for key, value in metadata.items():
        markdown += f"- {key}: {value}\n"

    markdown += "\n## Structural Checks\n"

    for key, value in analysis_result["structural_checks"].items():
        markdown += f"- {key}: {value}\n"

    markdown += "\n## Flags\n"

    if flags:
        for flag in flags:
            markdown += f"- {flag}\n"
    else:
        markdown += "- No anomalies detected\n"

    markdown += f"""
## Coherence Score
- Score Value: {score["value"]}
- Score Band: {score["band"]}

## Penalties Applied
"""

    if score["penalties_applied"]:
        for p in score["penalties_applied"]:
            markdown += f"- {p['flag']} (-{p['penalty']})\n"
    else:
        markdown += "- No penalties\n"

    with open(file_path, "w") as f:
        f.write(markdown)

    return file_path