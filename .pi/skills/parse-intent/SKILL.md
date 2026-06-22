---

name: parse-intent
description: Analyze grocery shopping intent and user shopping requirements.
----------------------------------------------------------------------------

# Parse Intent Skill

## Purpose

사용자의 장보기 요청을 분석하여 장보기 계획 수립에 필요한 정보를 추출한다.

## Responsibilities

* 가족 구성원 수 파악
* 알레르기 정보 분석
* 장보기 목적 분류
* 예산 정보 추출

## Input Example

```json
{
  "family_size": 4,
  "allergies": ["egg"],
  "purpose": "weekly",
  "budget": 50000
}
```

## Output Schema

```json
{
  "family_size": 4,
  "allergies": ["egg"],
  "purpose": "weekly",
  "budget": 50000
}
```

## Supported Purposes

* weekly
* diet
* birthday
* camping

## Notes

본 Skill은 사용자 입력을 구조화된 Context로 변환하여 다른 Agent들이 활용할 수 있도록 지원한다.
