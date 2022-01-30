'''
CSVの中身を読み込んでURLから必要な画像を保存する
D:\pythonProject\Web_Scraping\venv\Scripts\python.exe Selenium/get_csv_url_image.py
'''
import csv
import screenshot_using_profile_module as screenshot


def csv_to_list(csv_name):
    with open(csv_name,'r',encoding="utf-8_sig") as f:
        reader = csv.reader(f)
        list_csv = [row for row in reader]
    return list_csv

def get_kinokuniya_screenshot(left,right):
    list_csv=csv_to_list('D:/pythonProject/pdfConverter/books.csv')
    # NoとURLを取り出す -> 0 and 1
    # 一番最初の行はタイトル行なので無視する
    #for i in range(1,len(list_csv)):
    for i in range(left,right):
        print(list_csv[i][0],list_csv[i][1])
        screenshot.screenshot_kinokuniya(list_csv[i][1],str(int(list_csv[i][0])-1))
        


if __name__ == "__main__":
    get_kinokuniya_screenshot(50,60)