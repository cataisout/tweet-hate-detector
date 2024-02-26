import re
import nltk
from nltk.corpus import stopwords
import unicodedata
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer


################## funções de limpeza de texto ######################


# criando funções de limpeza com regex
# a ideia é depois montar uma pipeline com essas funções

def remove_numeros(text):
  return re.sub(r'\d+', '', text)

def remove_liveon(text):
  return re.sub(r'\(@\S+(.*\))', '',  text)

def remove_pontuacao(text):
  return re.sub(r'(["''-.,:;=!_?])', '', text)

def substitui_homemdeverdade(text):
  return re.sub(r'\@homemdeverdade', 'homem de verdade ', text)

def tira_arroba(text):
  return re.sub(r'@\w+', '', text)

def remove_links(text):
  return re.sub(r'https?:?//\S+|www\.\S+', '', text)

def remove_hashtag(text):
  return re.sub(r'#(\w+)', r'\1', text)

def remove_espaco_extra(text):
  return re.sub(r'\s+', ' ', text).strip()

def tudo_minusculo(text):
  return text.lower()

def remove_rt(text):
  return re.sub(r'\bRT', '', text)

def remover_caracteres_repetidos(texto):
    return re.sub( r'(\w)\1+', r'\1', texto)


pipeline_limpeza = Pipeline([
    ('remove_numeros', FunctionTransformer(remove_numeros)),
    ('remove_rt', FunctionTransformer(remove_rt)),
    ('substitui_homemdeverdade', FunctionTransformer(substitui_homemdeverdade)),
    ('tira_arroba', FunctionTransformer(tira_arroba)),
    ('remove_liveon', FunctionTransformer(remove_liveon)),
    ('remove_pontuacao', FunctionTransformer(remove_pontuacao)),
    ('remove_links', FunctionTransformer(remove_links)),
    ('remove_hashtag', FunctionTransformer(remove_hashtag)),
    ('remove_espaco_extra', FunctionTransformer(remove_espaco_extra)),
    ('tudo_minusculo',  FunctionTransformer(tudo_minusculo)),
    ('remover_caracteres_repetidos', FunctionTransformer(remover_caracteres_repetidos))
])

def limpeza(texto):
   return pipeline_limpeza.transform(texto)

def normaliza(texto):
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8').lower() # para remover acentos e padronizar em lower case

def remove_stopwords(text):
    nltk.download('stopwords')
    stopwords_nltk = stopwords.words('portuguese')
    stopwords_set = set(stopwords_nltk) 
    tokens = text.split()
    tokens = filter(lambda token: token not in stopwords_set, tokens)
    tokens = filter(lambda token: len(token) > 2, tokens)
    return ' '.join(tokens)

def tokeniza(text):
    return re.findall("[\w']+", text)


####para testar
pipeline_tratamento = Pipeline([
   ('normalização', FunctionTransformer(normaliza)),
   ('remoção_stopwords', FunctionTransformer(remove_stopwords)),
   ('tokeniza', FunctionTransformer(tokeniza))
])

