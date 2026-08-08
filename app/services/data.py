from app.config import PATIENTS_FILE
import json
from typing import List, Dict

def load_data() -> Dict:
    if not PATIENTS_FILE.exists():
        return {}
    
    with PATIENTS_FILE.open("r", encoding='utf-8') as file:
        return json.load(file)
    

def save_data(data):
    with PATIENTS_FILE.open("w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)