'''
各サイトに応じた画像のスクリーンショットを行う関数
D:\pythonProject\Web_Scraping\venv\Scripts\python.exe Selenium/screenshot_using_profile_module.py
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def screenshot_kinokuniya(URL,file_name_output):
    profile_path="C:/Users/xxbia/AppData/Local/Google/Chrome/User Data/Profile 2"
    chrome_driver_path="D:/pythonProject/Web_Scraping/ver_97/chromedriver.exe"
    #認証の情報を残すためにprofileを指定して開く 
    #optionsにchromeのアカウントと紐づけた情報を渡している
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=" + profile_path)
    driver=webdriver.Chrome(executable_path=chrome_driver_path,options=options)

    #urlを開く
    driver.get(URL)

    # ほしい情報を取り出す
    # https://kurozumi.github.io/selenium-python/locating-elements.html
    # 明示的に待機時間を指定する　→複数回ループを回すのできちんと読み込まれた後に情報を抜き出すようにする
    # https://office54.net/python/scraping/selenium-wait-time
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[1]/figure/img')))
    # XPATHで指定するのが楽　開発者ツールでコピペ可能
    # https://www.octoparse.jp/blog/xpath-introduction/
    img2 = driver.find_element(By.XPATH,'//*[@id="root"]/div[2]/div[1]/figure/img')
    #スクリーンショットで記録
    with open(f"C:/Users/xxbia/Downloads/"+file_name_output+".png", 'wb') as f:
        f.write(img2.screenshot_as_png)

    driver.quit()


def screenshot_maruzen(URL,file_name_output):
    profile_path="C:/Users/xxbia/AppData/Local/Google/Chrome/User Data/Profile 2"
    chrome_driver_path="D:/pythonProject/Web_Scraping/ver_97/chromedriver.exe"
    #認証の情報を残すためにprofileを指定して開く 
    #optionsにchromeのアカウントと紐づけた情報を渡している
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=" + profile_path)
    driver=webdriver.Chrome(executable_path=chrome_driver_path,options=options)

    #urlを開く
    driver.get(URL)
    driver.implicitly_wait(10)
    test_app_dynamics_job(driver,URL)

    driver.get(URL)
    # ほしい情報を取り出す
    # https://kurozumi.github.io/selenium-python/locating-elements.html
    driver.implicitly_wait(30)
    # 完全なXPATHだと上手くいく
    img2 = driver.find_element(By.XPATH,'/html/body/div[1]/div[4]/div/a/img')
    #スクリーンショットで記録
    with open(f"C:/Users/xxbia/Downloads/"+file_name_output+".png", 'wb') as f:
        f.write(img2.screenshot_as_png)

    driver.quit()

# seleniumの拡張機能でコード生成と調整
yourID="v21e0000"
yourPASS="passwords"
def test_app_dynamics_job(driver,url="https://elib.maruzen.co.jp/elib/html/GuestLogin?1"):   
    driver.get(url)
    driver.find_element(By.ID,"id2c").click()
    driver.find_element(By.ID,"username").click()
    driver.find_element(By.ID,"username").clear()
    driver.find_element(By.ID,"username").send_keys(yourID)
    driver.find_element(By.ID,"password").clear()
    driver.find_element(By.ID,"password").send_keys(yourPASS)
    driver.implicitly_wait(5)
    driver.find_element(By.NAME,"_eventId_proceed").click()
    

if __name__ == "__main__":
    screenshot_kinokuniya("https://kinoden.kinokuniya.co.jp/oitauniv/bookdetail/p/KP00004921/","0")
    #そもそも丸善はURLと画像が対応しているかも
    screenshot_maruzen("https://elib.maruzen.co.jp/elib/html/BookDetail/Id/3000003265","11")
    