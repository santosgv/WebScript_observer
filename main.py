from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://flatschart.com/html5/tabelas.html")
print(driver.title)
Dado=driver.find_element_by_xpath("/html/body/div[5]/div[2]/div[10]/table/tbody/tr/td[1]/code")
a=int(Dado.text)
compara=int(10)

if a != compara:
    print(a)
    print('Ta diferente')
    pass
elif a == compara:
    print('Ta igual')
    driver.quit()