from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from flask import Flask, render_template
import os
from models import db

# https://sol-aftercoding.tistory.com/entry/Python-%EA%B5%90%EB%B3%B4-%EB%AC%B8%EA%B3%A0-%ED%81%AC%EB%A1%A4%EB%A7%81-%ED%95%98%EA%B8%B0-with-Selenium-BeautifulSoup?category=1098008
# 위 사이트도 나한테 도움이 될 것 같다

# 좀 더 든 생각 : 각 서점 사이트들의 주간 베스트셀러를 종합하여 가장 많이 겹치는 것 / 각 사이트에서 주로 나온 키워드 등 분석

# yes24, aladin, 영풍문고의 주간 베스트셀러 url 가져오고, 바이트 단위로 content 변수에 저장
page = 1
yes24_url = 'https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001&pageNumber=1&pageSize=24'
aladin_url = 'https://aladin.co.kr/shop/common/wbest.aspx?BestType=Bestseller&BranchType=1&CID=0&page={page}&cnt=1000&SortOrder=1'
ypbooks_url = 'https://www.ypbooks.co.kr/bestseller/week'

yes24_req = requests.get(yes24_url)
aladin_req = requests.get(aladin_url)
# ypbooks_req = requests.get(ypbooks_url)

yes24_content = yes24_req.content
aladin_content = aladin_req.content
# ypbooks_content = ypbooks_req.content

# 기본적으로 requests만 쓰실 거라면 text가 더 좋을 수 있습니다.
# 하지만 대부분의 사람들은 requests만 쓰지 않고 BeautifulSoup라는 모듈과 같이 사용합니다.
# 이때 BeautifulSoup는 바이트 단위의 정보가 필요하기 때문에 content를 사용합니다.

# bs4로 넘기기(soup화)
yes24_soup = bs(yes24_content, 'html.parser')
aladin_soup = bs(aladin_content, 'html.parser')
# ypbooks_soup = bs(ypbooks_content, 'html.parser')

# yes24 주간 베스트셀러 상위 10개 도서 가져오기
# 근데 이거 맞냐? 반복문 쓰면 더 나아질 거 같은데.
yes24_bookName = yes24_soup.select('a.gd_name')

yes24_Book1 = yes24_bookName[0].text
yes24_Book2 = yes24_bookName[1].text
yes24_Book3 = yes24_bookName[2].text
yes24_Book4 = yes24_bookName[3].text
yes24_Book5 = yes24_bookName[4].text
yes24_Book6 = yes24_bookName[5].text
yes24_Book7 = yes24_bookName[6].text
yes24_Book8 = yes24_bookName[7].text
yes24_Book9 = yes24_bookName[8].text
yes24_Book10 = yes24_bookName[9].text

print(yes24_Book1)
print(yes24_Book2)
print(yes24_Book3)
print(yes24_Book4)
print(yes24_Book5)
print(yes24_Book6)
print(yes24_Book7)
print(yes24_Book8)
print(yes24_Book9)
print(yes24_Book10)

print('\n')

# 모르겠다 일단 알라딘이랑 영풍문고도 가져오자

# 알라딘
aladin_bookName = aladin_soup.select('a.bo3')

aladin_Book1 = aladin_bookName[0].text
aladin_Book2 = aladin_bookName[1].text
aladin_Book3 = aladin_bookName[2].text
aladin_Book4 = aladin_bookName[3].text
aladin_Book5 = aladin_bookName[4].text
aladin_Book6 = aladin_bookName[5].text
aladin_Book7 = aladin_bookName[6].text
aladin_Book8 = aladin_bookName[7].text
aladin_Book9 = aladin_bookName[8].text
aladin_Book10 = aladin_bookName[9].text

print(aladin_Book1)
print(aladin_Book2)
print(aladin_Book3)
print(aladin_Book4)
print(aladin_Book5)
print(aladin_Book6)
print(aladin_Book7)
print(aladin_Book8)
print(aladin_Book9)
print(aladin_Book10)

# 영풍문고..는 기존 방식대로 잘 안 되는 것 같다. 아쉬운대로 다른 두 서점 사이트들만이라도 웹페이지에 게시하자.
# 근데 파이썬 코드를 js랑 연동하려면..? Flask나 Django 같은 파이썬 웹 프레임워크를 사용해야 한단다.

# 근데 굳이 연동할 필요가 있나? 여기서 가져온 정보들을 csv 파일 등으로 저장해놓고, 그 파일을 JS에서 읽게끔 하면 되잖아?

# ypbooks_bookName = ypbooks_soup.select('a.book__title')

# ypbooks_Book1 = ypbooks_bookName[0].text
# ypbooks_Book2 = ypbooks_bookName[1].text
# ypbooks_Book3 = ypbooks_bookName[2].text
# ypbooks_Book4 = ypbooks_bookName[3].text
# ypbooks_Book5 = ypbooks_bookName[4].text
# ypbooks_Book6 = ypbooks_bookName[5].text
# ypbooks_Book7 = ypbooks_bookName[6].text
# ypbooks_Book8 = ypbooks_bookName[7].text
# ypbooks_Book9 = ypbooks_bookName[8].text
# ypbooks_Book10 = ypbooks_bookName[9].text

# print(ypbooks_Book1)
# print(ypbooks_Book2)
# print(ypbooks_Book3)
# print(ypbooks_Book4)
# print(ypbooks_Book5)
# print(ypbooks_Book6)
# print(ypbooks_Book7)
# print(ypbooks_Book8)
# print(ypbooks_Book9)
# print(ypbooks_Book10)

# pandas 부분
# 표 형태 : 열은 각 서점 사이트(0, 1, 2), 행은 도서 수(10권까지)(0, 1, 2, ..., 10) -> 3 x 11
# 열 : -, 알라딘, yes24 / 행 : -, 1, 2, ..., 10

df_Books = pd.DataFrame({'yes24':[yes24_Book1, yes24_Book2, yes24_Book3, yes24_Book4, yes24_Book5, yes24_Book6, yes24_Book7, yes24_Book8, yes24_Book9, yes24_Book10], 
                         'aladin':[aladin_Book1, aladin_Book2, aladin_Book3, aladin_Book4, aladin_Book5, aladin_Book6, aladin_Book7, aladin_Book8, aladin_Book9, aladin_Book10]})


df_Books.to_csv('BookCsv.csv')

# https://ealuuu.tistory.com/13 -> 이건 별개인데, replit run을 눌러도 실행이 안되는 경우 이렇게 하면 된다.

# app = Flask(__name__)

# @app.route('/')
# def index():
#   bookDf = pd.read_csv('BookCsv.csv')

#   table_html = bookDf.to_html(classes = 'table table-striped')
#   return render_template('index.html', table=table_html)

# if __name__ == '__main__':
#   app.run(debug=True)
