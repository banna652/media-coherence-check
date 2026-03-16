PENALTY_MAP = {
    "mime_extension_mismatch": 20,
    "metadata_missing": 15,
    "metadata_partial_only": 8,
    "timestamp_missing": 10,
    "timestamp_mismatch": 15,
    "editing_software_detected": 10,
    "reencoding_suspected": 15,
    "low_metadata_density": 8,
    "gps_missing": 3,
}

INFORMATIONAL_FLAGS = {
    "encoder_present"
}

def calculate_score(flags: list[str]) -> int:
    
    total_penalty = 0
    penalties_applied = []
    
    for flag in flags:
        if flag in PENALTY_MAP:
            penalty = PENALTY_MAP[flag]
            total_penalty += penalty
            
            penalties_applied.append({
                "flag": flag,
                "penalty": penalty,
            })
            
    score_value = max(60, 100 - total_penalty)
    
    return {
        "value": score_value,
        "band": determine_band(score_value),
        "penalties_applied": penalties_applied,
    }
    
def determine_band(score: int) -> str:
    
    if score >= 90:
        return "high"
    
    if score >= 75:
        return "good"
    
    return "limited"