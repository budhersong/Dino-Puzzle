# Dino-Bone Puzzle — 2차 프로토타입 v0.2 LOCK

저장 시각: 2026-09-27 KST

## 상태

이 문서는 현재 Dino-Bone Puzzle을 **2차 프로토타입 v0.2**로 최종 확정하기 위해 작성되었다.

## v0.2 확정 내용

### 게임 방향

- 해부학적 골격 부위명은 사용하지 않는다.
- 모든 조각은 `조각 1`, `조각 2`처럼 번호로만 표시한다.
- 공룡별 최종 이미지 라인업은 `FINAL-LINEUP-LOCK.md` / `final-lineup-lock.json` 기준을 따른다.
- 조각화는 과학적 부위 분리보다 단순 퍼즐 게임성을 우선한다.

### 난이도별 조각 수

- 쉬움: 6조각
- 보통: 12조각
- 어려움: 20조각

### 조각 생성 기준

- 길쭉한 나이테식 패턴 금지.
- 점/가루 조각 금지.
- 빈 조각 금지.
- 보이는 골격 그림 픽셀을 기준으로 조립 가능한 불규칙 덩어리 조각을 생성한다.

## v0.2에서 정리된 이미지

다음 공룡의 불필요한 바/선/범례를 제거했다.

- 이구아노돈
- 디플로도쿠스
- 데이노니쿠스
- 아파토사우루스

제거 내용:

- 회색 하단 바
- scale bar / 기준선
- 범례 텍스트/색상 박스
- 데이노니쿠스 오른쪽 검은 세로 막대
- 데이노니쿠스 상단 수평 기준선 및 잔여 점
- 아파토사우루스 하단 수평 기준선/scale marker

## 배포 방식

v0.2는 압축/로컬 실행 환경에서 이미지 경로가 깨지지 않도록, 단일 HTML에 16종 이미지를 base64로 내장한다.

즉:

- 외부 인터넷 의존 없음
- Wikimedia 원격 URL 런타임 의존 없음
- `assets/source-images/...` 상대 경로 의존 없음
- zip 내부 경로 문제 회피

## 현재 구현 파일

- 게임 본체: `index.html`
- 단일 HTML 배포본: `releases/dino-bone-puzzle-v0.2-standalone.html`
- zip 배포본: `releases/dino-bone-puzzle-v0.2-prototype.zip`
- 난이도별 조각 결과 확인: `artistic-difficulties-all-species-review.html`
- 조각 생성 스크립트: `scripts/make_artistic_all_difficulties_blobs.py`
- 하단 바 제거 스크립트: `scripts/clean_packaged_bottom_artifacts.py`
- 조각 출력 폴더: `assets/pieces/artistic-difficulties-v1/`
- 정리된 패키지 이미지 폴더: `assets/source-images/packaged-v0.1/`

## 전수 검사 결과

검사 대상:

```text
16종 × (쉬움 6 + 보통 12 + 어려움 20) = 608개 조각 PNG
```

검사 결과:

```text
checked_piece_pngs: 608
expected_total: 608
errors: 0
```

확인 항목:

- 조각 수 불일치 없음
- 빈 PNG 없음
- alpha 없는 조각 없음
- ink_pixels 0 조각 없음

## 완료 팝업

각 공룡 퍼즐을 완성하면 다음을 표시한다.

- 공룡 이름
- 간단한 공룡 설명
- 칭찬 메시지
- 완성 문구

## 2차 프로토타입 한계

- 조각 커팅은 퍼즐 게임용 덩어리 분할이다.
- 일부 길고 얇은 원본 구조는 조각 형태가 길어질 수 있다.
- 공개 배포 전 각 이미지의 라이선스와 출처 표기를 최종 확인해야 한다.

## 이 버전의 의미

이 상태를 **Dino-Bone Puzzle 2차 프로토타입 v0.2 최종 확정본**으로 삼는다.
이후 수정은 v0.2 기준선에서 별도 버전으로 진행한다.
