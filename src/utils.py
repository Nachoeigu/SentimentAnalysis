import json
import re

def convert_to_json(output):
    """
    Converts a string output from the language model to a JSON object.

    Args:
        output (str): The string output from the language model.

    Returns:
        dict: A dictionary representing the JSON object.

    """

    try:
        data = json.loads(output)
    except:
        data = json.loads('{'+re.search(pattern = '\"evaluation\"\:\"(positive|negative|neutral)\"', string = output).group()+'}')

    return data