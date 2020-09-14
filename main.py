from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from WebScript_observer.Dispara_Alerta import email_alert
import schedule
import time

def Job():
    #Opcao para rodar o navegador em background
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
        email_alert('Alerta BTL_Logistica','A fila Logistica esta com %s Registros'%(Logistica) ,'vitorgomes@patrus.com.br')
        pass
    if Averbacao >Averbacao_com:
        email_alert('Alerta BTL_Averbaçao','A fila Averbaçao esta com %s Registros'%(Averbacao) ,'vitorgomes@patrus.com.br')
        pass
    if B_prioridade > B_prioridade_com:
        email_alert('Alerta BTL_Baixa prioridade','A fila Baixa prioridade esta com %s Registros'%(B_prioridade) ,'vitorgomes@patrus.com.br')
        pass
    if Cad_edi > Cad_edi_com:
        email_alert('Alerta BTL_EDI','A fila EDI esta com %s Registros'%(Cad_edi) ,'vitorgomes@patrus.com.br')
        pass
    if Cte > Cte_com:
        email_alert('Alerta BTL_CTE','A fila CTE esta com %s Registros'%(Cte) ,'vitorgomes@patrus.com.br')
        pass
    if Edi_nfe > Edi_nfe_com:
        email_alert('Alerta BTL_NFE','A fila NFE esta com %s Registros'%(Edi_nfe) ,'vitorgomes@patrus.com.br')
        pass
    if Gv > Gv_com:
        email_alert('Alerta BTL_GV','A fila GV esta com %s Registros'%(Gv) ,'vitorgomes@patrus.com.br')
        pass
    if Mobile > Mobile_com:
        email_alert('Alerta BTL_Mobile','A fila Mobile esta com %s Registros'%(Mobile) ,'vitorgomes@patrus.com.br')

    if Merli > Merli_com:
        email_alert('Alerta BTL_Merli','A fila Merli esta com %s Registros'%(Merli) ,'vitorgomes@patrus.com.br')
        pass
    if Padrao > Padrao_com:
        email_alert('Alerta BTL_Padrao','A fila Padrao esta com %s Registros'%(Padrao) ,'vitorgomes@patrus.com.br')
        pass
    if Portal > Portal_com:
        email_alert('Alerta BTL_Porta','A fila do Portal esta com %s Registros'%(Portal) ,'vitorgomes@patrus.com.br')
        pass
    if Roterizador > Roterizador_com:
        email_alert('Alerta BTL_Roterizador','A fila Roterizador esta com %s Registros'%(Roterizador) ,'vitorgomes@patrus.com.br')
    else:

        driver.quit()

    driver.quit()

## Repitir script

schedule.every(10).minutes.do(Job)
while True:
    schedule.run_pending()
    time.sleep(1)