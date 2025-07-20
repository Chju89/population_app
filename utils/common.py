
import uuid

def generate_perID():
    return str(uuid.uuid4())

def validate_sex(value):
    return value.upper() in ['M', 'F']

def validate_date(date_text):
    from datetime import datetime
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False
