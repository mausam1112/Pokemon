import json
from app.config.settings import settings

def read_tracker():
    '''
    Reads the tracker file to determine the status of first run.
    '''
    with open(settings.run_tracker_fp) as f:
        data = json.load(f)
    return data['first_run']

def update_tracker():
    '''
    Updates the tracker file to state the completion of first run.
    '''
    data = {
        "first_run": False
    }
    with open(settings.run_tracker_fp, 'w') as f:
        json.dump(data, f, indent=4)
