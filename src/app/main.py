from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import txt_cleaning as tc
import pre_process as pp


app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta'


class TextoForm(FlaskForm):
    texto = StringField('Digite abaixo seu Tweet', validators=[DataRequired()])
    submit = SubmitField('Analisar')

    
@app.route('/', methods=['GET', 'POST'])

def home():
    form = TextoForm()
    resultado = None
    if form.validate_on_submit():
        texto = form.texto.data
        resultado = classifica_texto(texto)
    return render_template('index.html', form=form, resultado=resultado)

def classifica_texto(texto):
    txt_limpo = tc.limpeza(texto)
    txt_norm = tc.normaliza(txt_limpo)
    txt_nostopwords = tc.remove_stopwords(txt_norm)
    txt_token = tc.tokeniza(txt_nostopwords)
    txt_vec = pp.vetoriza(txt_token)
    txt_process = pp.pre_processamento(txt_vec)
    valor_previsao = pp.predict(txt_process)[0]

    if valor_previsao == 0:
        return 'Não possui discurso de ódio'
  
    
    return 'Possui discurso de ódio'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
