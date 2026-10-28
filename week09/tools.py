"""tools.py - 박스오피스 정보를 가져오는 도구 모음"""
import requests
from secret import API_KEY

BASE_URL = ("https://www.kobis.or.kr/kobisopenapi/webservice/"
            "rest/boxoffice/searchDailyBoxOfficeList.json")

def get_boxoffice_rank(date):
    """ docstring 형식
    그 날짜의 박스오피스 5위까지의 영화 제목들을 알려준다.

    받는 것: date (문자열) - "YYYYMMDD" 형태 날짜
    돌려주는 것: (문자열) 1~5위 영화 제목들
    """
    params = {"key": API_KEY, "targetDt": date}
    response = requests.get(BASE_URL, params=params, timeout=10)
    data = response.json()
    movies = data["boxOfficeResult"]["dailyBoxOfficeList"]
    top_movies = [movie["movieNm"] for movie in movies[:5]]
    return top_movies