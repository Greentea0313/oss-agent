작성: Claude Code / 확인: 황인하

# week09/tools.py 함수 정리

## 개요
- 영화진흥위원회(KOBIS) 오픈 API로 박스오피스 정보를 가져오는 도구 모음임
- `requests` 로 HTTP 요청을 보냄
- API 키는 `secret.py` 의 `API_KEY` 에서 가져옴
- 요청 주소는 상수 `BASE_URL` (일별 박스오피스 조회 API) 로 정의돼 있음

## 함수 목록

### `get_boxoffice_rank(date)`
- 역할: 지정한 날짜의 일별 박스오피스 1~5위 영화 제목을 돌려줌
- 입력: `date` (문자열) - `"YYYYMMDD"` 형식 날짜
- 출력: 1~5위 영화 제목 리스트 (`list[str]`)
- 동작 순서
  - `key`, `targetDt` 파라미터로 `BASE_URL` 에 GET 요청 보냄 (타임아웃 10초)
  - 응답 JSON 에서 `boxOfficeResult` → `dailyBoxOfficeList` 를 꺼냄
  - 앞 5개 항목의 `movieNm` (영화 제목) 만 모아 리스트로 반환함

## 참고 사항
- docstring 에는 반환값이 "문자열" 이라고 적혀 있으나 실제로는 리스트를 반환함
- 요청 실패나 응답 형식 오류 (HTTP 오류, 키 누락 등) 에 대한 예외 처리는 없음
