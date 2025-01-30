https://sws0230.github.io/BestBooks/ -> yes24, aladin의 주간 베스트셀러 10위를 모아 볼 수 있는 사이트입니다.


# 25.01.30 Update Log
1. 기존 Repo.WebProject에 있는 파일들을 '실제 웹사이트 배포 목적'인 BestBooks에 옮김(ipynb 파일 등 실제 구동에 쓸모없는 파일 제외)
2. main.py, index.html, script.js(원래 이름 app.js) 최적화(불필요한 코드 삭제) 및 실제 github pages 구동 확인 완료 짝짝짝
3. actions 작동 확인을 위해 매일 09:00에 자동으로 main.py를 실행시키는 워크플로우 작성


일단 가장 기본적인 메커니즘은 구현 완료.
좀 더 든 생각 : 각 서점 사이트들의 주간 베스트셀러를 종합하여 가장 많이 겹치는 것 / 각 사이트에서 주로 나온 키워드 등 분석해보기
-
