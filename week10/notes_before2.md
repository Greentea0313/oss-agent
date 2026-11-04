# week09/tools.py 함수 설명

## 개요
`tools.py`는 영화진흥위원회(KOBIS) 오픈 API를 이용해 박스오피스 정보를 가져오는 도구 모음입니다.

- 사용 라이브러리: `requests`
- API 키: `secret.py`의 `API_KEY`에서 불러옴
- `BASE_URL`: KOBIS 일별 박스오피스 조회 API 주소 (`searchDailyBoxOfficeList.json`)

## 함수 목록

### `get_boxoffice_rank(date)`
지정한 날짜의 일별 박스오피스 1~5위 영화 제목을 알려줍니다.

| 항목 | 내용 |
|------|------|
| 매개변수 | `date` (str) - `"YYYYMMDD"` 형식 날짜 (예: `"20261103"`) |
| 반환값 | 1~5위 영화 제목들 |

**동작 순서**
1. `key`(API 키)와 `targetDt`(날짜)를 파라미터로 묶음
2. `requests.get()`으로 API 호출 (타임아웃 10초)
3. 응답 JSON에서 `boxOfficeResult` → `dailyBoxOfficeList` 추출
4. 상위 5개 영화의 `movieNm`(영화 제목)만 리스트로 만들어 반환

**참고**
- docstring에는 반환값이 "문자열"이라고 되어 있지만, 실제로는 **문자열의 리스트**(`list[str]`)를 반환합니다.
- 네트워크 오류나 잘못된 날짜·API 키에 대한 예외 처리는 없습니다.
