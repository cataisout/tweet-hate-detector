import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib



## carregando os objetos treinados
vectorizer = joblib.load('tfidf_vectorizer.pkl')
clf = joblib.load('classifier.pkl')
pipeline = joblib.load('pre_process_pipeline.pkl')




def pre_processamento(x):
    return pipeline.transform(x)

def vetoriza(texto_tratado):
    tfidf_matrix = vectorizer.transform(texto_tratado)
    
    return pd.DataFrame(tfidf_matrix.toarray())

def predict(dado_processado):
    return clf.predict(dado_processado)
