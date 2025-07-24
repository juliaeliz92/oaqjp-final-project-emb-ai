import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers = header)  # Send a POST request to the API with the text and headers
    formatted_response = json.loads(response.text)
    anger = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
    disgust = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
    fear = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
    joy = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
    sadness = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
    anger = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
    emotions = {"anger": anger, "disgust":disgust, "fear": fear, "joy": joy, "sadness": sadness}
    dominant_emotion = max(emotions, key = emotions.get)
    return {"anger": anger, "disgust":disgust, "fear": fear, "joy": joy, "sadness": sadness, 'dominant_emotion': dominant_emotion}