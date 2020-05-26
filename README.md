# Twitter Bot

Programa que faz o login no Twitter automaticamente.

# Descrição

Esse programa foi escrito na linguagem Python e usou a biblioteca <a href="https://www.selenium.dev/">Selenium</a> como base. Ele faz a pesquisa do Twitter no Google, usando o navegador Chrome e realiza o login automaticamente.

<b>Obs.:</b> Os dados passados para a função devem ser de uma conta pré cadastrada no Twitter.

# Como funciona?

Para o programa fazer o login no Twitter, o usuário terá que especificar o email e senha, que serão passados por meio de parâmetros para a função twitterBot().

<b>Obs.:</b> As variáveis responsáveis por passar o email e senha estão no final do código, dentro da função main(), que é a função que chama a o programa.

# Instalação

É preciso ter o Python instalado no seu computador (<a href="https://www.python.org/downloads/">Python</a>, recomendado baixar a última versão). Para importar algumas funções usadas nesse projeto é preciso fazer a instalação de uma biblioteca:

* selenium - Forma de instalação: <b>pip install selenium</b>

<b>Obs.:</b> Essa instalação pode ser feita pelo terminal do seu computador (necessário que já tenha o Python instalado) ou pelo <a href="https://www.jetbrains.com/pt-br/pycharm/download/">PyCharm</a>, se preferir.

Outra instalação importante para esse projeto é a dos webdrives para o Chrome. Vá a <a href="https://chromedriver.storage.googleapis.com/index.html?path=78.0.3904.105/">página</a>, selecione o arquivo relacionado ao seu sistema operacional e então baixe-o. Após fazer o download, mova o arquivo <i>chromedriver</i>, que estará na pasta de Downloads, para a pasta <i>bin</i>. Isso você consegue realizar a partir do comando <b>mv ~/Downloads/chromedriver /usr/local/bin</b> no terminal do seu computador. Se as instalações correram bem até agora, você deve estar preparado para iniciar o programa.

# Uso

Após as instalações, para começar a usar basta clonar esse repositório e digitar o comando <b>python twitter-bot.py</b> no terminal ou rodar pelo PyCharm.

# Exemplos

![twitter-bot](https://user-images.githubusercontent.com/60857927/82854808-e5e35d00-9edf-11ea-8602-abb144ab108e.gif)