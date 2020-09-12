from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from WebScript_observer.Dispara_Alerta import Boottems
import schedule
import time

def Job():
    #Opcao para rodar o navegador em background
    Alertar=Boottems('login','senha')
    opcao=Options()
    opcao.headless=True
    driver = webdriver.Firefox(options=opcao)

    ## passando o link para o nagevador ##
    driver.get("http://admin:admin@172.31.0.10:8161/admin")
    print(driver.title)
    time.sleep(3)
    fila=driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/div[2]/div[1]/a[2]');fila.click()

    Logistica=driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/table/tbody/tr/td[1]/div/table[2]/tbody/tr[1]/td[2]')

    Averbacao=driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/table/tbody/tr/td[1]/div/table[2]/tbody/tr[2]/td[2]')
    B_prioridade=driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/table/tbody/tr/td[1]/div/table[2]/tbody/tr[3]/td[2]')
    Cad_edi=driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/table/tbody/tr/td[1]/div/table[2]/tbody/tr[4]/td[2]')
    Cte=driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/table/tbody/tr/td[1]/div/table[2]/tbody/tr[5]/td[2]')
    Edi_nfe=driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/table/tbody/tr/td[1]/div/table[2]/tbody/tr[6]/td[2]')
    Gv=driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/table/tbody/tr/td[1]/div/table[2]/tbody/tr[7]/td[2]')
    Merli=driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/table/tbody/tr/td[1]/div/table[2]/tbody/tr[8]/td[2]')
    Mobile=driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/table/tbody/tr/td[1]/div/table[2]/tbody/tr[9]/td[2]')
    Padrao=driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/table/tbody/tr/td[1]/div/table[2]/tbody/tr[10]/td[2]')
    Portal=driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/table/tbody/tr/td[1]/div/table[2]/tbody/tr[11]/td[2]')
    Roterizador=driver.find_element_by_xpath('/html/body/div/div[2]/div/div/div/table/tbody/tr/td[1]/div/table[2]/tbody/tr[12]/td[2]')

    ## Convertento string em int ##

    Logistica=int(Logistica.text)
    Averbacao=int(Averbacao.text)
    B_prioridade=int(B_prioridade.text)
    Cad_edi=int(Cad_edi.text)
    Cte=int(Cte.text)
    Edi_nfe=int(Edi_nfe.text)
    Gv=int(Gv.text)
    Merli=int(Merli.text)
    Mobile=int(Mobile.text)
    Padrao=int(Padrao.text)
    Portal=int(Portal.text)
    Roterizador=int(Roterizador.text)

    ## comparando
    Logistica_com=int(1000)
    Averbacao_com=int(1000)
    B_prioridade_com=int(1000)
    Cad_edi_com=int(1000)
    Cte_com=int(1000)
    Edi_nfe_com=int(1000)
    Gv_com=int(1000)
    Merli_com=int(1000)
    Mobile_com=int(1000)
    Padrao_com=int(1000)
    Portal_com=int(1000)
    Roterizador_com=int(1000)

    if Logistica > Logistica_com:
        print('A fila Logistica esta com %s registros'%(Logistica))
        pass
    if Averbacao >Averbacao_com:
        print('A fila Averbacao esta com %s registros'%(Averbacao))
        pass
    if B_prioridade > B_prioridade_com:
        print('A fila de baixa prioridade esta com %s Registros'%(B_prioridade))
        pass
    if Cad_edi > Cad_edi_com:
        print('A fila de Cad-edi esta com %s Registros'%(Cad_edi))
        pass
    if Cte > Cte_com:
        print('A fila de CTE esta com %s Registros'%(Cte))
        pass
    if Edi_nfe > Edi_nfe_com:
        print('A fila de NFE esta com %s Registros'%(Edi_nfe))
        pass
    if Gv > Gv_com:
        print('A fila do GV esta com %s Registros'%(Gv))
        pass
    if Mobile > Mobile_com:
        print('A fila do mobile esta com %s Registros'% (Mobile))

    if Merli > Merli_com:
        print('A fila da Merli esta com %s Registros'% (Merli))
        pass
    if Padrao > Padrao_com:
        print('A fila Padrao esta com %s Registros'%(Padrao))
        pass
    if Portal > Portal_com:
        print('A fila do Portal esta com %s Registros'%(Portal))
        pass
    if Roterizador > Roterizador_com:
        print('A fila do Routerizador esta com %s Registros'%(Roterizador))
    else:

        driver.quit()

    driver.quit()

## Repitir script

schedule.every(10).minutes.do(Job)
while True:
    Job()
    schedule.run_pending()
