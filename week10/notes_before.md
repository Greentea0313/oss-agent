# week09/tools.py 함수 정리 (변경 전)

## 개요
`tools.py`는 영화진흥위원회(KOBIS) 오픈 API로 박스오피스 정보를 가져오는 도구 모음입니다.

- 의존성: `requests`, `secret.API_KEY`
- 상수 `BASE_URL`: KOBIS 일별 박스오피스 조회 API 주소 (`searchDailyBoxOfficeList.json`)

## 함수 목록

### `get_boxoffice_rank(date)`
지정한 날짜의 일별 박스오피스 1~5위 영화 제목을 돌려줍니다.

| 항목 | 내용 |
|------|------|
| 인자 | `date` (str) — `"YYYYMMDD"` 형식 날짜 |
| 반환 | 1~5위 영화 제목 (`movieNm`) |

동작 순서:
1. `key`(API 키)와 `targetDt`(날짜)를 파라미터로 KOBIS API에 GET 요청 (timeout 10초)
2. 응답 JSON에서 `boxOfficeResult.dailyBoxOfficeList`를 꺼냄
3. 앞의 5개 항목에서 영화 제목만 뽑아 리스트로 반환

## 참고 사항
- docstring에는 반환값이 "문자열"이라고 되어 있지만, 실제로는 **문자열 리스트**(`list[str]`)를 반환합니다.
- HTTP 오류나 API 오류 응답(키 오류, 잘못된 날짜 등)에 대한 예외 처리가 없어, 이 경우 `KeyError` 등이 발생할 수 있습니다.
