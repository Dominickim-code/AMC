# MLA 1.Author (Last,First)
# 2. Title of source.(in quotation marks)
# 3. Title of container,(in italics)
# 4. number (ex)vol.4)
# 5.Publication Date
# 6.Location


# #APA
# 1. Author's surname, initial(s)
# 2. Date published
# 3.Title of Source
# 4.Location of Publisher: publisher(ex: San Francisco, CA)
# 5.Retrieved URL
# 6.
from scholarly import scholarly

# print(next(scholarly.search_author('Steven A. Cholewiak')))
# search_query = scholarly.search_author('Steven A Cholewiak')
# author = scholarly.fill(next(search_query))
#  print(author)
#  print([pub['bib']['title'] for pub in author['publications']])
# pub = scholarly.fill(author['publications'][0])
# print(pub)
# query = scholarly.search_pubs("A density-based algorithm for discovering clusters in large spatial databases with noise")
# pub = next(query)
# scholarly.bibtex(pub)
# print(query)
# search_query = scholarly.search_author('Matthias Fey')
# author = next(search_query).fill()
# print(author)
# search_pubs
# 테스트로 타입 파악 해보기
# TDL
# 형태 분석 화면 출력할수 있게 파이썬 파일 한번 만들어보기
# 프린트 해오는 결과값 바로 나올 수 있게 만들어 보기
# 그다음에 index.html
# 하면 바로 github에 리포지토리
search_query = scholarly.search_pubs('Perception of physical stability and center of mass of 3D objects')
scholarly.pprint(next(search_query))
# 변수 만들기
# 나홀로 메모장- 화면에 있는 url jquery로 가져와서 app.py에 넘겨주는 방식
# get = request
# 나홀로 메모장 api 문서 만들어 보기


# print([citation['bib']['title'] for citation in scholarly.citedby(pub)])
# from scholarly import scholarly
# import pprinter
# print(next(scholarly.search_author('Steven A. Cholewiak')))