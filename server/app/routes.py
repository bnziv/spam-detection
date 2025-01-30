from flask import Blueprint, request
from app.predict import predict

api = Blueprint('api', __name__)

@api.route('/predict', methods=['POST'])
def predict_route():
    data = request.json
    text = data.get('text')

    if not text:
        return {'error': 'Key "text" is required'}, 400
    
    response = predict(text)

    if response.get('error'):
        return response, 400
    
    return response, 200