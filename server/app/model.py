import pandas as pd
import os

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