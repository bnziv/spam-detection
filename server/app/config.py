import os

class Config:
    DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
    MODELS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')