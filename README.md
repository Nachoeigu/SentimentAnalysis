# Hotel Review Sentiment with Tiny LLMs
This project explores fast and efficient sentiment analysis for hotel reviews, prioritizing low latency, low cost, and high accuracy. 
Instead of using a dense parameter LLMs, I opted for a smaller one and focused on crafting a highly effective prompt to guide it.

### The approach:
A small LLM model is used for speed and cost efficiency.
The core of the project involves prompt engineering with software design that helps the LLM understand how to classify sentiment in hotel reviews.
The code provides a simple SentimentClassifier class for easy integration.
To run the project:
pip install -r requirements.txt
Create a .env file with WORKDIR=[your project path] and also add the APIKEYs (if needed)

Let me know if you have any questions or find anything interesting!

