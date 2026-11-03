# week09 - 박스오피스 순위 조회

## 무엇을 하는 코드인가
영화진흥위원회(KOBIS) 오픈 API로 특정 날짜의 일별 박스오피스 1~5위 영화 제목을 가져와 출력합니다.

## 설치
```bash
pip install -r requirements.txt
```

## 실행
1. [KOBIS 오픈 API](https://www.kobis.or.kr/kobisopenapi/)에서 키를 발급받고, 이 폴더에 `secret.py`를 만듭니다.
   ```python
   API_KEY = "발급받은_키"
   ```
2. 실행합니다.
   ```bash
   python main.py
   ```
   조회할 날짜는 `main.py`에서 `"YYYYMMDD"` 형식으로 바꿀 수 있습니다.
