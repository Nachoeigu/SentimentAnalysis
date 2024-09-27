reviews = [
    {"review": "Terrible experience. The air conditioning broke, and they didn’t fix it for two days!", "evaluation": "negative"},
    {"review": "Sparki had great amenities, and the spa was exactly what I needed to relax.", "evaluation": "positive"},
    {"review": "The hotel was okay, but nothing special. I feel like I could have found better for the price.", "evaluation": "neutral"},
    {"review": "Not a fan. The room wasn’t ready when I arrived, and the staff wasn’t helpful at all.", "evaluation": "negative"},
    {"review": "Absolutely loved my stay at Sparki! The ocean view from my room was breathtaking.", "evaluation": "positive"},
    {"review": "The location is unbeatable, but the hotel itself is a bit outdated.", "evaluation": "neutral"},
    {"review": "The service was subpar. The staff seemed uninterested in helping with anything.", "evaluation": "negative"},
    {"review": "I had a wonderful time at Sparki. The beach access was super convenient!", "evaluation": "positive"},
    {"review": "It's an okay hotel, but it was noisy at night. I couldn’t sleep well.", "evaluation": "neutral"},
    {"review": "I had the worst experience here. The hotel was dirty, and the pool was closed for maintenance.", "evaluation": "negative"},
    {"review": "Highly recommend Sparki for anyone looking for a relaxing getaway. The food was excellent too!", "evaluation": "positive"},
    {"review": "The price was decent, but you get what you pay for. The rooms were a bit small.", "evaluation": "neutral"},
    {"review": "I wouldn’t stay here again. The customer service was terrible and the room wasn’t as described.", "evaluation": "negative"},
    {"review": "Sparki exceeded my expectations! It’s the perfect spot for a romantic vacation.", "evaluation": "positive"},
    {"review": "It’s a good location, but the hotel’s facilities need some updating.", "evaluation": "neutral"},
    {"review": "I loved everything about Sparki. The staff made me feel so welcome and the pool area was stunning.", "evaluation": "positive"},
    {"review": "Average experience. Nothing stood out, but nothing was particularly bad either.", "evaluation": "neutral"},
    {"review": "The rooms were outdated, and the WiFi was horrible. Wouldn’t recommend.", "evaluation": "negative"},
    {"review": "Perfect location for exploring Cancun, and the hotel had a lively atmosphere. I really enjoyed my stay.", "evaluation": "positive"},
    {"review": "The hotel was okay. Not bad, but I think there are better options in Cancun.", "evaluation": "neutral"},
    {"review": "Horrible experience. The staff was rude and the amenities were broken.", "evaluation": "negative"},
    {"review": "I had an amazing time at Sparki! The breakfast buffet was delicious every morning.", "evaluation": "positive"},
    {"review": "The hotel was fine, but I had issues with noise from the nearby construction site.", "evaluation": "neutral"},
    {"review": "Sparki was a disaster. My room was dirty, and it took hours to get it cleaned.", "evaluation": "negative"},
    {"review": "I couldn’t have asked for a better hotel! Sparki had everything I needed for a perfect vacation.", "evaluation": "positive"},
    {"review": "The hotel was clean and the staff was friendly, but the overall experience was just average.", "evaluation": "neutral"},
    {"review": "My stay was a nightmare. I will never return to Sparki. The worst hotel experience I’ve had.", "evaluation": "negative"},
    {"review": "Loved everything about Sparki! The rooftop bar had stunning views of the sunset.", "evaluation": "positive"},
    {"review": "It was a decent hotel, but I found it to be overpriced for what they offer.", "evaluation": "neutral"},
    {"review": "The front desk staff was incredibly rude, and the room wasn’t cleaned properly.", "evaluation": "negative"},
    {"review": "Sparki is amazing! The proximity to the beach and the friendly staff made my stay unforgettable.", "evaluation": "positive"},
    {"review": "It’s a solid hotel, but there’s nothing that sets it apart from the competition.", "evaluation": "neutral"},
    {"review": "The worst part of my vacation was staying at Sparki. The room was uncomfortable and noisy.", "evaluation": "negative"},
    {"review": "Sparki exceeded all my expectations! The beachfront location and the spa were the highlights of my trip.", "evaluation": "positive"},
    {"review": "The hotel is in a good spot, but they really need to upgrade their rooms.", "evaluation": "neutral"},
    {"review": "I had several issues with my stay. The water pressure was low, and the bed was uncomfortable.", "evaluation": "negative"},
    {"review": "Fantastic hotel! I’ll definitely be staying at Sparki again on my next trip to Cancun.", "evaluation": "positive"},
    {"review": "The hotel was decent, but it could use some improvements. The rooms felt a bit old.", "evaluation": "neutral"},
    {"review": "I would not recommend Sparki to anyone. The experience was a mess from start to finish.", "evaluation": "negative"},
    {"review": "Had a great stay! Sparki is one of the best hotels I’ve visited in Cancun.", "evaluation": "positive"},
    {"review": "It’s a middle-of-the-road hotel. Not bad, but not great either.", "evaluation": "neutral"},
    {"review": "The staff was inattentive, and I felt like they didn’t care about the guests at all.", "evaluation": "negative"},
    {"review": "Sparki provided a fantastic vacation experience! Can’t wait to come back.", "evaluation": "positive"}
]

correct_predictions = 0
incorrect_predictions = 0

for question in reviews:

    import json
    result = model.invoke(messages + [HumanMessage(content = question['review'], id = uuid.uuid4())])
    import re

    cleaned_response = result.content.replace('\n', '').replace(' ','')

    try:
        data = json.loads(cleaned_response)
        automatically = 1
    except:
        data = json.loads('{'+re.search(pattern = '\"evaluation\"\:\"(positive|negative|neutral)\"', string = cleaned_response).group()+'}')
        automatically = 0
    
    print(automatically)
    if data['evaluation'] == question['evaluation']:
        print("Correct prediction")
        correct_predictions += 1
    else:
        print("Incorrect prediction")
        incorrect_predictions += 1
        print(f"Prediction was: {data['evaluation']}")
        print(f"Real was: {question['evaluation']}")
        print(f"Review was: {question['review']}")


print("Accuracy:", str(round(correct_predictions/len(reviews),4)))
