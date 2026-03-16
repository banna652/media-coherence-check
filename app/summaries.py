def generate_summary(score_band: str) -> str:
    
    summaries = {
        "high": "Technical structure appears coherent with no major anomalies detected.",
        "good": "The media file shows generally consistent technical structure with minor anomalies.",
        "limited": "The file presents several structural inconsistencies that may indicate transformations."
    }
    
    return summaries.get(
        score_band,
        "Unable to determine structural coherence interpretation."
    )