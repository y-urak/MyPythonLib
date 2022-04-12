# デスクトップアプリ化
# https://www.wantanblog.com/entry/2020/07/14/224611

import dearpygui.dearpygui as dpg
import time
from bs4 import BeautifulSoup
import requests as req

time_start=time.time()
dpg.create_context()

# ------------------------------------------------------
init_message=""
text_message="Formatted string literals — also called f-strings — have been around since Python 3.6, so we all know what they are and how to use them. There are however some facts and handy features of f-string that you might not know about. So, let’s take a tour of some awesome f-string features that you’ll want to use in your everyday coding."
split_message=text_message.split(" ")
cnt=0
start_flag=False
base_wpm_sec = 0.38 # wpm 160?
# ------------------------------------------------------
# ボタンを押したときの処理
def button_callback(sender, app_data, user_data):
    global start_flag
    print(f"sender is: {sender}")
    print(f"app_data is: {app_data}")
    print(f"user_data is: {user_data}")
    if start_flag:
        start_flag=False
    else:
        start_flag=True

def load_sentence_from_html(sender):
    global split_message
    url=dpg.get_value(sender)
    html = req.get(url).content
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    elems = soup.find_all("p")
    return_sentence=""
    for elem in soup.find_all(["p", "h1", "h2", "h3"]):
        print(elem.name + " " + elem.text.strip())
        return_sentence+=elem.text.strip()+" "
    split_message=return_sentence.split(" ")
    print("change:",split_message)

def load_sentence_from_copy_paste(sender):
    global split_message
    message= dpg.get_value(sender)
    split_message=message.split(" ")
    print("change:",split_message)


def change_wpm(sender):
    global base_wpm_sec
    wpm=dpg.get_value(sender)
    # 一単語を何秒で更新するか
    base_wpm_sec=60/wpm
    print("change:",base_wpm_sec)

def update_progress(sender,data):
    global wpm
    print(sender)
    dpg.set_value("b_bar",wpm/300)
    dpg.configure_item(tag="b_bar",overlay=str(wpm/300))


# フォント系
# https://github.com/hoffstadt/DearPyGui/issues/1380
# 中央揃えはstring.center()をつかうのが王道？
with dpg.font_registry():
    # Download font here: https://fonts.google.com/specimen/Open+Sans
    new_font = dpg.add_font('fonts/OpenSans-Bold.ttf',15*3,tag="OpenSans-font")


with dpg.window(label="Example Window",tag="Primary Window"):
    # https://github.com/hoffstadt/DearPyGui/blob/master/DearPyGui/dearpygui/demo.py
    dpg.add_progress_bar(label="Progress Bar", default_value=0.0, tag="now_progress")
    dpg.add_text(init_message,tag="update_info")
    dpg.bind_item_font(dpg.last_item(), "OpenSans-font")

    dpg.add_button(label="start",callback=button_callback,user_data="unknown")
    dpg.add_slider_int(label=":wpm", default_value=160, min_value=100 ,max_value=300, callback=change_wpm)
    dpg.add_input_text(label=":URL", callback=load_sentence_from_html)
    dpg.add_input_text(label=":Copy and Paste", default_value=text_message, callback=load_sentence_from_copy_paste)

dpg.create_viewport(title='Custom Title', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)

# below replaces, start_dearpygui()
while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
    if start_flag:
        time_now =time.time()
        #秒数と一致
        #print(str(time_now-time_start))
        if time_now-time_start>base_wpm_sec:
            if len(split_message)>cnt:
                dpg.set_value("update_info",split_message[cnt].center(30))
                dpg.set_value("now_progress",cnt/len(split_message))
                cnt+=1
                time_start=time_now
            else:
                dpg.set_value("now_progress", 1)
                dpg.set_value("update_info",str(cnt))
                start_flag=False
                cnt=0
    dpg.render_dearpygui_frame()

dpg.destroy_context()

