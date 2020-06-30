
from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager 

def banner():
	print('''Bem-Vindo''')

def main():
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.get('https://web.whatsapp.com/')

	name = input('Digite o nome do usuário ou do grupo : ') #usuário que irá receber as mensagens
	msg = input('Digite sua mensagem : ')
	count = int(input('Quantas vezes a mensagem será enviada? : '))

	input('Aperte qualquer tecla após a leitura do QR CODE.')

	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name)) #irá procurar na lista de contato a STR digitada em name
	user.click()
	
	
	msg_box = driver.find_element_by_class_name('_3uMse')  #irá selecionar a caixa de texto pelo Class_Name - Pode variar - (f12 no Chrome para descobrir)
		
	for i in range(count):
		msg_box.send_keys(msg)
		button = driver.find_element_by_class_name('_1U1xa') #Class_name do botão de enviar também pode variar - (f12 no Chrome para descobrir)
		button.click() 
	print('Pronto, mensagens enviadas!')

banner()
main()
