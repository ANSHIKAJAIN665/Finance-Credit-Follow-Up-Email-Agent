import json
from datetime import datetime

def save_log(data):

    data["timestamp"] = str(datetime.now())

    with open("logs/email_logs.json", "a") as f:
        json.dump(data, f)
        f.write("\n")