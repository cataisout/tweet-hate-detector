# Tweet Hate Detector

O Tweet Hate Detector é uma aplicação que utiliza técnicas de Processamento de Linguagem Natural aliadas a Machine Learning para detectar tweets que contenham discurso de ódio. Esta aplicação é útil para identificar e filtrar conteúdo prejudicial em redes sociais. Ela atualmente é mais eficaz na identificação de discursos que envolvem sexismo e machismo, pois os dados utilizados no treinamento possuiam em maior parte textos com esses rótulos

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- **src**: Esta pasta contém o código-fonte da aplicação.
  - **app**: Contém os scripts em Flask para rodar a aplicação web.
  - **models**: Contém os modelos pré-treinados utilizados para a detecção de tweets de ódio.

## Requisitos de Instalação

Para rodar a aplicação localmente, é necessário ter o Python e o Docker instalados no seu sistema, idealmente linux, ou no wsl

## Como Rodar a Aplicação

1. Clone o repositório para a sua máquina local
2. Abra a pasta raiz do projeto
3. Construa a imagem do Docker utilizando o Dockerfile fornecido:
```docker build -t tweet-hate-detector .```

4. Execute o container Docker:
```docker run -p 5000:5000 tweet-hate-detector```


5. Acesse a aplicação em seu navegador web através do seguinte endereço:
http://localhost:5000


## Contribuindo

Se você quiser contribuir para este projeto, sinta-se à vontade para enviar pull requests. Toda contribuição é bem-vinda!


## Melhoramentos futuros

1. **Interface Web**: Implementar uma interface web mais intuitiva e amigável para os usuários da aplicação, possibilitando uma melhor experiência de uso.

2. **Utilizar Embeddings para Vetorização**: Explorar o uso de embeddings para vetorizar os tweets, o que pode melhorar a qualidade da detecção de discurso de ódio ao capturar nuances semânticas e contextuais.

3. **Testar Outras Arquiteturas de Redes Neurais**: Experimentar e avaliar outras arquiteturas de redes neurais para a detecção de discurso de ódio, como redes convolucionais (CNNs) ou redes recorrentes (RNNs), a fim de identificar a mais adequada para o problema em questão.

4. **Melhorar a Classificação de Outros Tipos de Discurso de Ódio**: Buscar novas amostras de textos com ourtos tipos de discursos de ódio (direcionados a outros grupos), ou implementar técnicas de oversampling para melhor generalização das amostras ja existentes




