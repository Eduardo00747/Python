import pandas as pd
import time 

from selenium import webdriver # Abrir navegador 
from selenium.webdriver.common.by import By # Achar os elementos na tela 
from selenium.webdriver.common.keys import Keys # Usar o teclado  


nome_do_arquivo = 'Livro1.xlsx'
url_do_forms = "https://eduardo00747.github.io/Register_System/"  # Site em que o robo irá trabalhar 
df = pd.read_excel(nome_do_arquivo)

# Laço para a logica do ROBO
for index,row in df.iterrows():
    print ("index: " + str(index) + " O nome da pessoa a ser cadastrada é " + str(row ["User Name "]))
    chrome = webdriver.Chrome(executable_path='chromedriver.exe')
    chrome.get(url_do_forms)

    # Tempo para aguardar a pagina carregar 
    time.sleep(3)
    
    # Variaveis para achar os elemetos do site 
    elemento_texto_name = chrome.find_element(By.XPATH,'/html/body/div/div[1]/div/form/input[1]')
    elemento_texto_email = chrome.find_element(By.XPATH,"/html/body/div/div[1]/div/form/input[2]")
    elemento_texto_senha = chrome.find_element(By.XPATH,"/html/body/div/div[1]/div/form/input[3]")
    elemento_texto_repitasenha = chrome.find_element(By.XPATH,"/html/body/div/div[1]/div/form/input[4]")

    # Variaveis para digitar os dados 
    elemento_texto_name.send_keys(row["User Name "])
    elemento_texto_email.send_keys(row["E-mail"])
    elemento_texto_senha.send_keys(row["Password"]) 
    elemento_texto_repitasenha.send_keys(row["Password"])

    # Tempo para fechar o navegador
    time.sleep(0.5)

    # Variavel para assinar o termo 
    elemento_termo = chrome.find_element(By.XPATH, "/html/body/div/div[1]/div/form/div/label/input").click()

    # Tempo para fechar o navegador
    time.sleep(0.5)
    
    # Variavel para enviar o cadastro
    elemento_cadastrar = chrome.find_element(By.XPATH, "/html/body/div/div[1]/div/form/input[5]").click()

    chrome.quit