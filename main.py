# 웹 크롤링 -> BookCsv.csv 작성 코드

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# 좀 더 든 생각 : 각 서점 사이트들의 주간 베스트셀러를 종합하여 가장 많이 겹치는 것 / 각 사이트에서 주로 나온 키워드 등 분석

# yes24, aladin, 영풍문고의 주간 베스트셀러 url 가져오고, 바이트 단위로 content 변수에 저장
page = 1
yes24_url = 'https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001&pageNumber=1&pageSize=24'
aladin_url = 'https://aladin.co.kr/shop/common/wbest.aspx?BestType=Bestseller&BranchType=1&CID=0&page={page}&cnt=1000&SortOrder=1'

yes24_req = requests.get(yes24_url)
aladin_req = requests.get(aladin_url)

yes24_content = yes24_req.content
aladin_content = aladin_req.content

# bs4로 넘기기(soup화)
yes24_soup = bs(yes24_content, 'html.parser')
aladin_soup = bs(aladin_content, 'html.parser')

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

# 영풍문고..는 기존 방식대로 잘 안 되는 것 같다. 아쉬운대로 다른 두 서점 사이트들만이라도 웹페이지에 게시하자.

# pandas 부분
# 표 형태 : 열은 각 서점 사이트(0, 1, 2), 행은 도서 수(10권까지)(0, 1, 2, ..., 10) -> 3 x 11
# 열 : -, 알라딘, yes24 / 행 : -, 1, 2, ..., 10

df_Books = pd.DataFrame({'yes24':[yes24_Book1, yes24_Book2, yes24_Book3, yes24_Book4, yes24_Book5, yes24_Book6, yes24_Book7, yes24_Book8, yes24_Book9, yes24_Book10], 
                         'aladin':[aladin_Book1, aladin_Book2, aladin_Book3, aladin_Book4, aladin_Book5, aladin_Book6, aladin_Book7, aladin_Book8, aladin_Book9, aladin_Book10]})

df_Books.to_csv('BookCsv.csv')

with open('BookCsv.csv', mode='r', newline='', encoding='utf-8') as infile:
  reader = csv.reader(infile, quotechar='"')
  modified_data = []
  for row in reader:
    new_row = [cell.replace(',', '&') if ',' in cell else cell for cell in row]
    modified_data.append(new_row)

with open('BookCsv.csv', mode='w', newline='', encoding='utf-8') as outfile:
  writer = csv.writer(outfile, quotechar='"', quoting=csv.QUOTE_MINIMAL)
  writer.writerows(modified_data)

print('----------------------------')
print('| Bookcsv.csv 최신화 완료! |')
print('----------------------------')
