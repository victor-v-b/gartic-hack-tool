from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time
import threading
import re


print('categorias disponiveis: alimentos, verbos')
#escolhe a categoria
categoria = input("escreva o nome da categoria")

respostas_possiveis = [line.strip() for line in open(fr'c:\Users\victor\Desktop\codigo backup\gartic hack ATUALIZADO 2024\{categoria}.csv', encoding='utf-8')]
toggle = False
index = 0

chrome_options = Options()
chrome_options.add_argument(r"user-data-dir=C:\Users\victor\AppData\Local\Google\Chrome\User Data\Default")  # Replace with actual profile path
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Helps evade detection
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)

driver=webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 13) 

driver.get("https://gartic.com.br/")
driver.maximize_window()
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

path = "/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/form/label/input"

def enviaResposta(res):
    #global index
    #resposta = respostas_possiveis[index] """ 
    try:
        campoResposta = wait.until(EC.element_to_be_clickable((By.XPATH, path)))
        campoResposta.send_keys(res)
        campoResposta.send_keys(Keys.ENTER)
        #index +=1
        time.sleep(0.9)
    except:
        print("espere...")
        time.sleep(2)
        return
        
def inputListerner():
    global index, toggle
    while True:
        user_input = input("Enter - Write // Space - RESET ")
        if user_input.isspace():
            index = 0
        #if enter...
        elif user_input.strip() == "":
            toggle = not toggle
            print("active: ",str(toggle))

def checaAcerto():
    inputField = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/div[2]/form/label/input")
    if inputField.get_attribute("disabled") == "":
        return True
    else:
        return False

def stringProcess(str):
    processedString = re.sub(r'&nbsp;', '.', str)
    compiled_pattern = re.compile(processedString, re.I)
    # Iterate through the word list and check for matches
    matching_words = [word for word in respostas_possiveis if (compiled_pattern != [] and compiled_pattern.fullmatch(word))]
    print('matching words: ', matching_words)
    return matching_words

def observaDica():
    dicaTxt =  driver.find_element(By.CLASS_NAME, "dicaTxt")
    dicaDiv = dicaTxt.find_element(By.TAG_NAME, "div")
    try: 
        spans = dicaDiv.find_elements(By.TAG_NAME, "span")
        concatenated_inner_html = ""
        for span in spans:
            concatenated_inner_html += span.get_attribute("innerHTML")
        
    except NoSuchElementException:
        print('noSuchElement.................')
        return ""
    except StaleElementReferenceException:
        print('staleElement.................')
        return ""
    
    else:
        return stringProcess(concatenated_inner_html)

def mainLoop():

    global toggle
    while True:
        if toggle:
            matchingWords = observaDica()
            for chute in matchingWords:
                if not checaAcerto():
                    enviaResposta(chute)
                else: toggle = not toggle
                print("active: ",str(toggle))

            time.sleep(0.1)

nick = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[1]/div[1]/div[2]/form/div[1]/input[1]')
nick.send_keys("Jony2003")

thread1 = threading.Thread(target=inputListerner)
thread2 = threading.Thread(target=mainLoop)
thread1.start()
thread2.start()

    