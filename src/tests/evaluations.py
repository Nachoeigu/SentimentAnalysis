import os
from dotenv import load_dotenv
import sys

load_dotenv()
WORKDIR=os.getenv("WORKDIR")
os.chdir(WORKDIR)
sys.path.append(WORKDIR)

import json
from langchain_groq import ChatGroq
from src.model import SentimentClassifier

correct_predictions = 0
incorrect_predictions = 0

model = ChatGroq(model_name = 'llama-3.2-1b-preview', temperature = 0)
with open(f"{WORKDIR}/src/tests/dataset.json","r") as file:
    reviews = json.loads(file.read())

for case in reviews:
    bot = SentimentClassifier(model = model)
    model_response = bot(review = case['review'])

    if model_response['evaluation'] == case['evaluation']:
        print("Correct prediction")
        correct_predictions += 1
    else:
        print("Incorrect prediction")
        incorrect_predictions += 1
        print(f"Prediction was: {model_response['evaluation']}")
        print(f"Real was: {case['evaluation']}")
        print(f"Review was: {case['review']}")


print("Accuracy:", str(round(correct_predictions/len(reviews),4)))
