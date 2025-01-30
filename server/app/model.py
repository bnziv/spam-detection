import pandas as pd
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import pickle

def load_data():
    """
    Load data from csv file and preprocess it
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, '..', 'data', 'spam.csv')
    df = pd.read_csv(data_path)

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
    dataset = load_data()
    texts = dataset['text']
    labels = dataset['label']

    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)

    vectorizer = CountVectorizer()
    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)

    model = MultinomialNB()
    model.fit(X_train, y_train)

    with open('models/model.pkl', 'wb') as f:
        pickle.dump(model, f)

    with open('models/vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)

if __name__ == '__main__':
    train_model()