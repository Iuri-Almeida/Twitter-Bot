# Projeto Twitter Bot - Python
# Autor: Iuri Lopes Almeida
# Perfil GitHub: https://github.com/Iuri-Almeida
# Data: 25/05/2020
# Descrição: Esse programa foi escrito na linguagem Python e usou a biblioteca
# 			 Selenium como base. Ele faz a pesquisa do Twitter no Google, usando
# 			 o navegador Chrome e realiza o login automaticamente. Desde que os
# 			 dados passados para a função sejam de uma conta pré cadastrada no Twitter.
# Forma de uso: python twitter-bot.py
# Baixar os webdrivers para o Chrome! -> https://chromedriver.storage.googleapis.com/index.html?path=78.0.3904.105/
# Após baixar, mova o arquivo "chromedriver" para a pasta "bin" a partir
# do comando no terminal -> mv ~/Downloads/chromedriver /usr/local/bin


# Importações necessárias
from selenium import webdriver
from time import sleep


# Função responsável por fazer o login no Twitter automaticamente.
def twitterBot(email, senha):

	# Abra o Chrome
	driver = webdriver.Chrome()

	# Maximize a tela do navegador.
	driver.maximize_window()

	# Abra a página.
	driver.get("https://www.google.com/")

	# Encontre o input para pesquisa e escreva o que tem na variável pesquisa.
	inputPesquisa = driver.find_element_by_name("q")
	inputPesquisa.send_keys("twitter")

	# Encontre o botão de pesquisar e clique.
	botaoPesquisar = driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div[1]/div[3]/center/input[1]")
	botaoPesquisar.click()

	# Encontre o link da pesquisa que contém o texto "Entre no Twitter" e clique.
	siteTwitter = driver.find_element_by_xpath("//h3[contains(text(), 'Entre no Twitter')]")
	siteTwitter.click()

	# Encontre o input onde é colocado o email do usuário e escreva o que tem na variável email.
	inputEmail = driver.find_element_by_xpath("//input[contains(@name, 'session[username_or_email]')]")
	inputEmail.send_keys(email)

	# Encontre o input onde é colocado a senha do usuário e escreva o que tem na variável senha.
	inputSenha = driver.find_element_by_xpath("//input[contains(@name, 'session[password]')]")
	inputSenha.send_keys(senha)

	# Encontre o botão para entrar e clique.
	botaoEntrar = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div/div")
	botaoEntrar.click()

	# Bota o prograna em espera por 4 segundos.
	sleep(4)

	# Encerra o navegador.
	driver.close()


# Função principal, onde serão chamadas todas as outras funções.
def main():

	# Chama a função para fazer o login no Twitter, passando os parâmetros que vc escolher.
	email = ""
	senha = ""

	twitterBot(email, senha)


if __name__ == "__main__":
	main()