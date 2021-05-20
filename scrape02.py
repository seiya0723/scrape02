import bs4
from selenium import webdriver

"""
Seleinumを使う前段階

1 pip intall selenium でライブラリのSeleinumをインストール

2 Seleniumでブラウザを動かすために必要になるドライバーをインストールする。( FirefoxであればFirefox( https://github.com/mozilla/geckodriver/releases )のドライバー、ChormeであればChormeのドライバー( https://chromedriver.chromium.org/downloads )をインストール)

3 下記のコードに倣って webdriver.ブラウザ名() でインスタンスを作り、.get()でアクセスする

参照元1:https://www.seleniumqref.com/introduction/webdriver_intro.html
参照元2:https://qiita.com/hujuu/items/ef89c34fca955cc571ec
"""

URL     = ""
PROFILE = ""


#プロファイルを読み込み(これでログイン情報のチェックができる)
#参照元: https://support.mozilla.org/ja/kb/profiles-where-firefox-stores-user-data

fp      = webdriver.FirefoxProfile(PROFILE)
driver  = webdriver.Firefox(fp)

#アクセスするURLを指定して起動
driver.get(URL)

#BeautifulSoupで解析
soup    = bs4.BeautifulSoup(driver.page_source, "html.parser")
print(soup)


#TIPS:JSによるレンダリングで描画遅延が発生している場合、暗黙的待機、明示的待機のいずれかを行い、要素が表示されるのを待つ



#暗黙的待機とは、開発者が特定の要素が表示されるまでにかかる時間を想定し、time.sleepにて指定して待機させる。実装は簡単だが、少しでも遅延が長引くと動かない。
#明示的待機とは、開発者が特定の要素を指定して、要素が表示されるまで待機する。実装は難しいが、確実に要素が表示されるまでに待機させることができる。

#=========暗黙的な待機=========

import time

time.sleep(10)
soup    = bs4.BeautifulSoup(driver.page_source, "html.parser")

print("\n\n\n=================ここから先、暗黙的待機==================\n\n\n")
print(soup)



#========明示的な待機============

#明示的な待機に必要なものをインポートする。By→要素特定、WebDriverWait→指定した待ち時間まで待機、expected_conditions→指定の状況になれば発動

from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


#特定の要素が視認可能になるまで、指定した秒数だけ待機する。
try:
    driver_wait = WebDriverWait(driver,3)
    target      = driver_wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME, "html")))
except:
    print("HTMLの取得に失敗しました")
else:
    soup    = bs4.BeautifulSoup(driver.page_source, "html.parser")

    print("\n\n\n=================ここから先、明示的待機==================\n\n\n")
    print(soup)

