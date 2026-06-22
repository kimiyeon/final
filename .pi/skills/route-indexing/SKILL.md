
---

## `.pi/skills/route-indexing/SKILL.md`

```md
---
name: route-indexing
description: 장보기 재료의 가격을 계산하고 예산 기준으로 구매 계획을 정리하는 Skill
---

# Route Indexing Skill

## 목적

장보기 목록의 예상 가격을 계산하여 예산에 맞는 구매 계획을 생성한다.

## 입력 정보

- 장보기 재료 목록
- 재료별 가격 데이터
- 사용자 예산

## 처리 규칙

- 각 재료의 가격을 조회한다.
- 전체 예상 비용을 계산한다.
- 예산 초과 여부를 확인한다.
- 가격 정보가 없는 재료는 기본 가격을 적용한다.

## 출력 형식

```json
{
  "shopping_list": [
    {
      "item": "rice",
      "price": 9000
    },
    {
      "item": "kimchi",
      "price": 7000
    }
  ],
  "total_cost": 16000,
  "budget": 50000
}