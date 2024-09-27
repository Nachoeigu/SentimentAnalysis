import os
from dotenv import load_dotenv
import sys

load_dotenv()
WORKDIR=os.getenv("WORKDIR")
os.chdir(WORKDIR)
sys.path.append(WORKDIR)

import json
import re
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_groq import ChatGroq
from constants import SYSTEM_PROMPT, FEW_SHOT_EXAMPLES
from langchain_core.language_models.chat_models import BaseChatModel
import uuid
from src.utils import convert_to_json

class SentimentClassifier:
    """
    SentimentClassifier class for classifying the sentiment of hotel reviews.

    Attributes:
        model (BaseChatModel): The language model used for sentiment classification.
        messages (list): The list of messages that form the prompt for the language model.
    """
    def __init__(self, model: BaseChatModel):
        """
        Initializes the SentimentClassifier with a language model.

        Args:
            model (BaseChatModel): The language model to use for sentiment classification.

        """
        self.model = model
        self.messages = self.__developing_prompt()

    def __developing_prompt(self):
        """
        Develops the prompt for the language model, including system instructions and few-shot examples.

        Returns:
            list: The list of messages that form the prompt.

        """

        messages =[
            SystemMessage(content = SYSTEM_PROMPT)
        ]

        for example in FEW_SHOT_EXAMPLES:
            human_msg = HumanMessage(content = example['review'], id = uuid.uuid4())
            ai_msg = AIMessage(content = '{"evaluation":"'+ example['evaluation']+'"}', id = uuid.uuid4())
            messages.append(human_msg)
            messages.append(ai_msg)
        
        return messages
        
    def __call__(self, review: str):
        """
        Classifies the sentiment of a given review.

        Args:
            review (str): The hotel review to classify.

        Returns:
            dict: A dictionary containing the sentiment evaluation.

        """

        output = self.model.invoke(self.messages + [HumanMessage(content = review, id = uuid.uuid4())])
        output = re.sub(r'[\n\s]+', '', output.content)
        output = convert_to_json(output)

        return output
    
if __name__ == '__main__':
    model = ChatGroq(model_name = 'llama-3.2-1b-preview', temperature = 0)
    bot = SentimentClassifier(model = model)

    output = bot(review = "Amazing. the unique point of improvement: the bathroom.")

    print(output)
