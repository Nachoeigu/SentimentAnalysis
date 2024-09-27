import json
import re

def convert_to_json(output):
    try:
        data = json.loads(output)
    except:
        data = json.loads('{'+re.search(pattern = '\"evaluation\"\:\"(positive|negative|neutral)\"', string = output).group()+'}')

    return data