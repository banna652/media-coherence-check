def generate_flags(rule_results: dict, metadata: dict) -> list[str]:
    
    flags: list[str] = []
    
    if not rule_results.get("extension_mime_match", True):
        flags.append("extension_mime_mismatch")
        
    if not rule_results.get("metadata_present", True):
        flags.append("metadata_missing")
        
    if rule_results.get("metadata_present", True) and not rule_results.get("timestamp_present", True):
        flags.append("timestamp_missing")
        
    if not rule_results.get("timestamp_consistent", True):
        flags.append("timestamp_mismatch")
        
    if metadata.get("software"):
        flags.append("editing_software_detected")
        
    if metadata.get("encoder"):
        flags.append("encoder_present")
        
    if metadata.get("gps") is None:
        flags.append("gps_missing")
        
    metadata_values = [v for v in metadata.values() if v is not None]
    if len(metadata_values) < 3:
        flags.append("low_metadata_density")
        
    return flags