from datetime import datetime

def check_extension_mime_consistency(extension: str, mime_type: str) -> bool:
    
    if not mime_type:
        return False
    
    return extension in mime_type.lower()

def check_metadata_presence(metadata: dict) -> bool:
    
    if not metadata:
        return False
    
    return any(value is not None for value in metadata.values())

def check_timestamp_presence(metadata: dict) -> bool:
    
    return metadata.get("creation_date") is not None

def check_timestamp_consistency(metadata: dict) -> bool:
    
    creation = metadata.get("creation_date")
    modification = metadata.get("modification_date")
    
    if not creation or not modification:
        return False
    
    try:
        creation_dt = datetime.fromisoformat(str(creation))
        modification_dt = datetime.fromisoformat(str(modification))
        
        return modification_dt >= creation_dt
    
    except Exception:
        return False
    
def check_encoder_presence(metadata: dict) -> bool:
    
    return metadata.get("encoder") is not None