import pickle
try: # for production
    from app.config import Config
    from app.model import train_model
except ImportError: # for development
    from config import Config
    from model import train_model

train_model()

with open(f'{Config.MODELS_PATH}/model.pkl', 'rb') as f:
    model = pickle.load(f)

with open(f'{Config.MODELS_PATH}/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

def predict(text):
    """
    Predict a message by the trained model
    """
    try:
        text = vectorizer.transform([text])
        result = model.predict(text)[0]
        prob = model.predict_proba(text)[0]

        mapping = {0: 'ham', 1: 'spam', 2: 'phishing'}
        response = {
            'result': mapping[result],
            'probability': {mapping[i]: float(prob[i]) for i in range(3)}
        }

        return response
    
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    text = "test message"
    response = predict(text)
    print(response)