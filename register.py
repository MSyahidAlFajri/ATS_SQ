from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Konfigurasi opsi Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

# Inisialisasi WebDriver dengan opsi yang telah dikonfigurasi
driver = webdriver.Chrome(options=options)

# Maksimalkan jendela browser ke mode layar penuh
driver.maximize_window()

# Open the website
driver.get('https://trensentimen.my.id')
time.sleep(3)

#klik tombol menuju ke register
button_register = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='register.html']")))
button_register.click()
time.sleep(3)

#masukan label name 
label_name = driver.find_element(By.ID, 'name') 
label_name.click()

name = 'Syahid AF'
for character in name:
    label_name.send_keys(character)
    time.sleep(0.05)

label_name.send_keys(Keys.ENTER)

#masukan label username
label_username = driver.find_element(By.ID, 'email')  
label_username.click()

username = 'msyahid2503@gmail.com'
for character in username:
    label_username.send_keys(character)
    time.sleep(0.05)

label_username.send_keys(Keys.ENTER)

#masukan label password
label_password = driver.find_element(By.ID, 'password') 
label_password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))

label_password.click()

password = 'syahid25'
for character in password:
    label_password.send_keys(character)
    time.sleep(0.05)

label_password.send_keys(Keys.ENTER)

#masukan label no wa
label_no_wa = driver.find_element(By.ID, 'nohp')
label_no_wa.click()

no_wa = '6285784718312'
for character in no_wa:
    label_no_wa.send_keys(character)
    time.sleep(0.05)

label_no_wa.send_keys(Keys.ENTER)

#masukan label kkonfirmasi password
label_confirm_password = driver.find_element(By.ID, 'confirm-password')  
label_confirm_password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'confirm-password')))

label_confirm_password.click()

confirm_password = 'syahid25'
for character in password:
    label_confirm_password.send_keys(character)
    time.sleep(0.05)

label_confirm_password.send_keys(Keys.ENTER)

#klik tombol daftar untuk menyelesaikan proses registrasi
register_button = driver.find_element(By.ID, 'button')  
register_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'button')))
register_button.click()

#delay beberapa waktu
time.sleep(15)

#close  browser
driver.quit()
