import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers=headers, json=data)
    refined_response = json.loads(response.text)
    emotional_response = refined_response['emotionPredictions'][0]['emotion']

    response_data = {
        'anger': emotional_response['anger'],
        'disgust': emotional_response['disgust'],
        'fear': emotional_response['fear'],
        'joy': emotional_response['joy'],
        'sadness': emotional_response['sadness']
    }

    dominant_emotion = max(response_data, key=response_data.get)
    
    response_data['dominant_emotion'] = dominant_emotion

    return response_data