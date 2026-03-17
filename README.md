# Media Coherence Check v0.1

Media Coherence Check is a Python CLI tool that performs deterministic
structural analysis of image and video files.

The tool extracts technical metadata, evaluates structural consistency
rules, generates anomaly flags, and produces a coherence score along
with detailed reports.

The analysis follows the SMCA (Structural Media Coherence Analysis)
methodology.

------------------------------------------------------------------------

## Features

-   Image metadata extraction using ExifTool
-   Video metadata extraction using FFprobe
-   Structural consistency checks
-   Deterministic anomaly flag generation
-   Coherence scoring system
-   JSON output report
-   Markdown human-readable report
-   Command Line Interface (CLI)

------------------------------------------------------------------------

## Requirements

-   Python 3.10+
-   ExifTool
-   FFmpeg (FFprobe)

Install system dependencies:

sudo apt install libimage-exiftool-perl sudo apt install ffmpeg

Install Python dependencies:

pip install -r requirements.txt

------------------------------------------------------------------------

## Usage

Run the analyzer using the CLI:

python3 -m app.main analyze --file examples/example.jpg --output outputs

Example for video:

python3 -m app.main analyze --file examples/example.mp4 --output outputs

------------------------------------------------------------------------

## Output

The tool generates two reports:

### JSON Report

Machine-readable analysis output.

Example:

outputs/example_image_analysis.json

### Markdown Report

Human-readable report containing:

-   Analysis overview
-   File identity
-   Technical metadata
-   Structural checks
-   Flags
-   Coherence score

Example:

outputs/example_image_analysis.md

------------------------------------------------------------------------

## Project Structure

media-coherence-check

├── app\
│ ├── analyzer.py\
│ ├── cli.py\
│ ├── fileinfo.py\
│ ├── hashing.py\
│ ├── metadata.py\
│ ├── rules.py\
│ ├── flags.py\
│ ├── scoring.py\
│ ├── report.py\
│ ├── summaries.py\
│ └── main.py\
│ ├── examples\
│ ├── example.jpg\
│ └── example.mp4\
│ ├── outputs\
│ ├── example_image_analysis.json\
│ ├── example_image_analysis.md\
│ ├── example_video_analysis.json\
│ └── example_video_analysis.md\
│ ├── tests\
├── requirements.txt\
└── README.md

------------------------------------------------------------------------

## Notes

This version implements deterministic structural analysis and does not
perform AI or machine learning based detection.