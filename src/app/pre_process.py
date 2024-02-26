import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import zipfile


# descompactando o arquivo pca
pca_compactado = 'src/models/pca.zip'
pca_descompactado = 'src/models/pca_descompactado.pkl'
with zipfile.ZipFile(pca_compactado, 'r') as zf:
    with open(pca_descompactado, 'wb') as f_out:
        f_out.write(zf.read(zf.namelist()[0]))


## carregando os objetos treinados
vectorizer = joblib.load('src/models/tfidf_vectorizer.pkl')
clf = joblib.load('src/models/classifier.pkl')
scaler = joblib.load('src/models/scaler.pkl')
pca = joblib.load(pca_descompactado)



def pre_processamento(x):
    pipeline = Pipeline([
    ('scaler', scaler),
    ('pca', pca) ])

    return pipeline.transform(x)

def vetoriza(texto_tratado):
    tfidf_matrix = vectorizer.transform(texto_tratado)
    
    return pd.DataFrame(tfidf_matrix.toarray())

def predict(dado_processado):
    return clf.predict(dado_processado)
