from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
import csv

driver=webdriver.Chrome()
driver.get("https://respostadogartic.blogspot.com/2017/10/lista-de-verbos-gartic.html")

buttons = driver.find_elements(By.TAG_NAME, "button")
buttons_text = []

for button in buttons:
    buttons_text.append(button.text)

csv_file = r"C:\Users\victor\Desktop\codigo backup\gartic hack ATUALIZADO 2024\desenhoAnimado.csv"

# Open the CSV file in write mode
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the button texts to the CSV file
    for text in buttons_text:
        writer.writerow([text])

print('done')