import argparse
from pathlib import Path

from app.analyzer import MediaAnalyzer
from app.report import save_json_report, generate_markdown_report
from app.summaries import generate_summary

def run_cli():
    parser = argparse.ArgumentParser(
        description="Media Coherence Check v0.1"
    )
    
    parser.add_argument(
        "command",
        choices=["analyze"],
        help="Command to execute"
    )
    
    parser.add_argument(
        "--file",
        required=True,
        help="Path to the media file to analyze"
    )
    
    parser.add_argument(
        "--output",
        default="./outputs",
        help="Directory to store analysis results"
    )
    
    args = parser.parse_args()
    
    if args.command == "analyze":
        analyzer = MediaAnalyzer()
        
        result = analyzer.analyze(args.file)
        
        result["summary"] = generate_summary(result["score"]["band"])
        
        json_path = save_json_report(result, args.output)
        md_path = generate_markdown_report(result, args.output)
        
        print("\nAnalysis completed successfully.\n")
        print(f"JSON report: {json_path}")
        print(f"Markdown report: {md_path}")
    