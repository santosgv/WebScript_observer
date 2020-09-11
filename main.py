from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from .Dispara_Alerta import Boottems

## Opcao para rodar o navegador em background
Alertar=Boottems('login','senha')
opcao=Options()
opcao.headless=True
driver = webdriver.Firefox(options=opcao)

## passando o link para o nagevador ##
driver.get("https://flatschart.com/html5/tabelas.html")
print(driver.title)
## Localizando elementos ###

edi=driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[10]/table/tbody/tr/td[1]/code")
nfe=driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[10]/table/tbody/tr/td[1]/code")
gv=driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[10]/table/tbody/tr/td[1]/code")
pessoa=driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[10]/table/tbody/tr/td[1]/code")
routerizador=driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[10]/table/tbody/tr/td[1]/code")

## Convertendo o dado coletado em INT ##

edi=int(edi.text)
nfe=int(nfe.text)
gv=int(gv.text)
pessoa=int(pessoa.text)
routerizador=int(routerizador.text)

## Comparando valores ##

edi_compara=int(10)
nfe_compara=int(10)
gv_compara=int(10)
pessoa_compara=int(10)
routerizador_compara=int(10)


if edi > edi_compara:
    Alertar.disparar()
    pass
if nfe > nfe_compara:
    print()
    pass
if gv > gv_compara:
    print()
    pass
if pessoa > pessoa_compara:
    print()
    pass
if routerizador > routerizador_compara:
    print()
    pass
driver.quit()
## Repitir script