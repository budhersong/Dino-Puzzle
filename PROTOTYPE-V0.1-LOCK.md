# Dino-Bone Puzzle — 1차 프로토타입 v0.1 LOCK

저장 시각: 2026-09-23 18:58 KST

## 상태

이 문서는 현재 Dino-Bone Puzzle을 **1차 프로토타입 v0.1**로 고정하기 위해 작성되었다.

## 확정된 방향

- 해부학적 골격 부위명은 사용하지 않는다.
- 모든 조각은 `조각 1`, `조각 2`처럼 번호로만 표시한다.
- 공룡별 최종 이미지 라인업은 `FINAL-LINEUP-LOCK.md` / `final-lineup-lock.json` 기준을 따른다.
- 조각화는 단순 퍼즐 게임성을 우선한다.
- 난이도별 조각 수:
  - 쉬움: 6조각
  - 보통: 12조각
  - 어려움: 20조각
- 보통/어려움은 길쭉한 나이테 패턴이나 점 조각이 아니라, 조립 가능한 불규칙 덩어리 조각을 사용한다.
- 빈 조각 PNG가 없어야 한다.

## 현재 구현 파일

- 게임 본체: `index.html`
- 난이도별 조각 결과 확인: `artistic-difficulties-all-species-review.html`
- 조각 생성 스크립트: `scripts/make_artistic_all_difficulties_blobs.py`
- 조각 출력 폴더: `assets/pieces/artistic-difficulties-v1/`
- 기준 문서: `ARTISTIC-PUZZLE-CUT-STANDARD.md`

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

## 1차 프로토타입 한계

- 조각 커팅은 과학적 골격 부위 분리가 아니라 퍼즐 게임용 덩어리 분할이다.
- 일부 길고 얇은 원본 구조, 특히 꼬리/날개/긴 목은 조각이 길어 보일 수 있다.
- 공개 배포 전 각 이미지의 라이선스와 출처 표기를 최종 확인해야 한다.

## 이 버전의 의미

이 상태를 **Dino-Bone Puzzle 1차 프로토타입 v0.1** 기준선으로 삼는다.
이후 수정은 이 기준선에서 기능 개선/시각 개선/게임성 개선으로 진행한다.
