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

def _parse_exif_date(date_value: str):

    try:
        clean_date = date_value.split("+")[0]
        return datetime.strptime(clean_date, "%Y:%m:%d %H:%M:%S")
    except Exception:
        return None

def check_timestamp_consistency(metadata: dict):

    creation = metadata.get("creation_date")
    modification = metadata.get("modification_date")

    if not creation or not modification:
        return False

    creation_dt = _parse_exif_date(str(creation))
    modification_dt = _parse_exif_date(str(modification))

    if not creation_dt or not modification_dt:
        return False

    return modification_dt >= creation_dt

def check_encoder_presence(metadata: dict):

    return metadata.get("encoder") is not None