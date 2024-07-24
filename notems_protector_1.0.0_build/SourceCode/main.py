from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import keyboard

overlay_text=input('请输入要保护的内容:')
targetName = input('请输入要保护页面的名称:')
force_editing = False # 强制修改时为 True

url = f'https://note.ms/{targetName}'
if force_editing:
    url += '?force-editing=true'

print(f'请确认目标剪贴板名称：【{targetName}】、保护内容：【{overlay_text}】    [1.ENTER确认]')

while True:
    if keyboard.is_pressed('enter'):
        break
    
print('等待窗口开启！')

driver = webdriver.Edge()
driver.get(url)
driver.set_window_size(1,210)
driver.minimize_window()

print('note.ms保护脚本已启动！')

while True:
    sleep(0.1)
    driver.refresh()
    sumit=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div[1]/div/div/textarea"))
    )
    if(sumit.text!=overlay_text):
        sumit.clear()
        sumit.send_keys(overlay_text)
        sleep(0.5)
    
    