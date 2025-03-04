import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import pickle
try: # for production
    from app.config import Config
except ImportError: # for development
    from config import Config

def load_data():
    """
    Load data from csv file and preprocess it
    """
    file = os.path.join(Config.DATA_PATH, 'spam.csv')
    df = pd.read_csv(file)

    df = df[['TEXT', 'LABEL']]
    df.columns = ['text', 'label']

    def sort_label(label):
        if label.lower() == 'ham':
            return 0
        elif label.lower() == 'spam':
            return 1
        elif label.lower() == 'smishing':
            return 2
        else:
            return None
        
    df['label'] = df['label'].map(sort_label)

    return df

def train_model():
    """
    Train model and save it
    """
    dataset = load_data()
    texts = dataset['text']
    labels = dataset['label']

    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

    vectorizer = CountVectorizer()
    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)

    model = MultinomialNB()
    model.fit(X_train, y_train)

    if not os.path.exists(Config.MODELS_PATH):
        os.mkdir(Config.MODELS_PATH)

    with open(f'{Config.MODELS_PATH}/model.pkl', 'wb') as f:
        pickle.dump(model, f)

    with open(f'{Config.MODELS_PATH}/vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)

if __name__ == '__main__':
    train_model()