import os
import time
import pandas as pd
import datetime
import common.common as common
import common.selenium_amazon as sele_amazon
from dotenv import load_dotenv
load_dotenv() #環境変数のロード

# 定数を定義
LOG_FILE_PATH = './log/log_{export_at}.log'
AMAZON_ID = os.environ["A_USER_ID"]
AMAZON_PASS = os.environ["A_PASS"]

def get_table_data(elements,word):
    # テーブルの情報取得
    tr_elements = elements.find_elements_by_css_selector('.tableCondition tr')
    td_txt = "不明"
    for tr_elem in tr_elements:
        th_value = tr_elem.find_element_by_tag_name('th').text
        if th_value == word:
            td_txt = tr_elem.find_element_by_tag_name('td').text
    return td_txt

# main処理
def main():
    # search_keyword = input("キーワードを入力：")
    # driverを起動
    if os.name == 'nt': #Windows
        driver = common.set_driver("chromedriver.exe", False)
    elif os.name == 'posix': #Mac
        driver = common.set_driver("chromedriver", False)

    # ログイン
    sele_amazon.Amazon_login(driver,AMAZON_ID,AMAZON_PASS)
    time.sleep(3)
    # 入力されたキーワードのWebサイトを開く
    driver.get("https://www.amazon.co.jp/gp/cart/view.html?app-nav-type=none&dc=df")
    time.sleep(5)

    # 検索結果の件数を取得
    content_num = len(driver.find_elements_by_css_selector("#sc-active-cart .sc-list-item"))
    print(content_num)

    driver.close()

# 直接起動された場合はmain()を起動(モジュールとして呼び出された場合は起動しないようにするため)
if __name__ == "__main__":
    main()
