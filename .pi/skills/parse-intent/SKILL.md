---
name: parse-intent
description: 사용자의 장보기 입력 정보를 구조화된 컨텍스트로 변환하는 Skill
---

# Parse Intent Skill

## 목적

사용자의 장보기 입력을 분석하여 Agent가 사용할 수 있는 구조화된 데이터로 변환한다.

## 입력 정보

- 가족 수
- 알레르기 정보
- 장보기 목적
- 예산

## 처리 규칙

- 가족 수는 정수 값으로 변환한다.
- 알레르기 정보는 쉼표 기준으로 분리한다.
- 장보기 목적은 weekly, diet, birthday, camping 등으로 분류한다.
- 예산은 정수형 금액으로 변환한다.

## 출력 형식

```json
{
  "family_size": 4,
  "allergies": ["milk"],
  "purpose": "weekly",
  "budget": 50000
}