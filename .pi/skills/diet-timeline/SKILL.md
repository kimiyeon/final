
---

## `.pi/skills/diet-timeline/SKILL.md`

```md
---
name: diet-timeline
description: 사용자의 목적과 제약 조건에 따라 식단 후보를 생성하는 Skill
---

# Diet Timeline Skill

## 목적

사용자의 장보기 목적과 가족 정보를 바탕으로 적절한 식단 후보를 생성한다.

## 입력 정보

- 가족 수
- 알레르기 정보
- 장보기 목적
- 예산
- 레시피 데이터

## 처리 규칙

- 주간 장보기는 일반 식사 중심으로 구성한다.
- 다이어트 목적은 상대적으로 가벼운 식단을 우선한다.
- 생일 파티는 파티용 메뉴를 우선한다.
- 캠핑 목적은 조리하기 쉬운 메뉴를 우선한다.
- 알레르기 재료가 포함된 메뉴는 제외한다.

## 출력 형식

```json
{
  "meal_plan": [
    "Kimchi Fried Rice",
    "Tteokbokki",
    "Fruit Platter"
  ],
  "ingredients": [
    "rice",
    "kimchi",
    "egg",
    "rice_cake",
    "gochujang"
  ]
}