import json

def load_config(file='config.json'):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_config(config, file='config.json'):
    with open(file, 'w') as f:
        json.dump(config, f, indent=4)
