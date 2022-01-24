'''
CSVに載っている認証が必要なURLから画像を得るために一度ログインした情報が残っているかどうか確かめる
->確かめたのでついでに画像の保存
1. https://qiita.com/Hidenatsu/items/e43ba04b4b5f710784e6
2. https://engineeeer.com/python-selenium-chrome-login/

D:\pythonProject\Web_Scraping\venv\Scripts\python.exe Selenium/selenium_using_profile.py
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.google.com/"
URL1 = "https://kinoden.kinokuniya.co.jp/oitauniv/bookdetail/p/KP00004920/"

profile_path="C:/Users/xxbia/AppData/Local/Google/Chrome/User Data/Profile 2"
chrome_driver_path="D:/pythonProject/Web_Scraping/ver_97/chromedriver.exe"
#認証の情報を残すためにprofileを指定して開く 
#optionsにchromeのアカウントと紐づけた情報を渡している
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=" + profile_path)
driver=webdriver.Chrome(executable_path=chrome_driver_path,options=options)

driver.implicitly_wait(0.5)
#urlを開く
driver.get(URL1)

# ほしい情報を取り出す
# https://kurozumi.github.io/selenium-python/locating-elements.html
driver.implicitly_wait(10)
body = driver.find_element(By.TAG_NAME,'body')
id_name = body.find_element(By.ID,'root')
img = id_name.find_element(By.CLASS_NAME,'jss5')
#1 画像はタグ名で取得できる
img1 = img.find_element(By.TAG_NAME,'img')
alt = img.find_element(By.TAG_NAME,'img').get_attribute('alt')

print(img)
print(img1)
print(alt)

#スクリーンショットで記録
with open(f"C:/Users/xxbia/Downloads/out.png", 'wb') as f:
    f.write(img1.screenshot_as_png)

driver.quit()