from flask import Flask
import txt_cleaning as tc
import pre_process as pp


app = Flask(__name__)

@app.route('/')

def home():
    return "Minha primeira API"

@app.route('/teste')

def secreto():
    return "olá vc achou um lugar secreto hihihihih"


@app.route('/analise_texto/<string:texto>')
def classifica_texto(texto):
    txt_limpo = tc.limpeza(texto)
    txt_norm = tc.normaliza(txt_limpo)
    txt_nostopwords = tc.remove_stopwords(txt_norm)
    txt_token = tc.tokeniza(txt_nostopwords)
    #return pp.vetoriza(txt_token)
    txt_vec = pp.vetoriza(txt_token)
    txt_process = pp.pre_processamento(txt_vec)
    valor_previsao = pp.predict(txt_process)[0]

    if valor_previsao == 0: return 'Não possui discurso de ódio' 
    return 'Possui discurso de ódio' 

app.run(debug=True, host='0.0.0.0', port=5000)