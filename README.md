# Smart Grocery Agent (스마트 장보기 에이전트)

Pi 기반 Agent Architecture와 MCP(Model Context Protocol)를 활용하여 구현한 AI 장보기 도우미 서비스입니다.

사용자의 가족 구성, 알레르기 정보, 장보기 목적, 예산을 분석하여 식단과 장보기 목록을 자동 생성합니다.

---

# 1. 프로젝트 소개

Smart Grocery Agent는 장보기 계획 수립 과정을 자동화하기 위한 AI Agent 기반 웹 서비스입니다.

사용자는 가족 수, 알레르기, 장보기 목적, 예산 등의 정보를 입력할 수 있으며, 시스템은 이를 분석하여 적절한 식단과 장보기 목록을 생성합니다.

또한 외부 레시피 데이터베이스(TheMealDB)를 활용하여 메뉴 정보를 가져오고, MCP 서버를 통해 재료 및 가격 정보를 관리합니다.

---

# 2. 문제 정의

일반적인 장보기 과정에서는 다음과 같은 문제가 발생합니다.

* 어떤 식단을 준비해야 할지 결정하기 어렵다.
* 가족 구성원이나 알레르기를 고려하지 못한다.
* 예산 관리가 어렵다.
* 필요한 재료를 일일이 계산해야 한다.

본 프로젝트는 이러한 문제를 Agent 기반 구조를 통해 해결하는 것을 목표로 한다.

---

# 3. 서비스 대상

다음과 같은 사용자를 대상으로 한다.

* 주간 장보기를 계획하는 가정
* 알레르기가 있는 가족 구성원을 둔 사용자
* 식단 계획이 필요한 사용자
* 예산 관리를 중요하게 생각하는 사용자
* 캠핑, 파티 등 특정 목적의 장보기가 필요한 사용자

---

# 4. 주요 기능

## 4.1 사용자 정보 분석 (Context Analysis)

사용자 입력을 분석하여 장보기 컨텍스트를 생성한다.

입력 정보

* 가족 수
* 알레르기
* 장보기 목적
* 예산

예시

```json
{
  "family_size": 4,
  "allergies": ["milk"],
  "purpose": "weekly",
  "budget": 50000
}
```

---

## 4.2 식단 추천 (Menu Planning)

장보기 목적에 따라 메뉴를 추천한다.

예시

* 주간 장보기
* 다이어트
* 생일 파티
* 캠핑

레시피 정보는 TheMealDB API 및 로컬 레시피 데이터를 활용한다.

---

## 4.3 알레르기 필터링

사용자가 입력한 알레르기 정보를 기반으로 위험한 재료가 포함된 메뉴를 제외한다.

예시

입력

```text
알레르기: 닭고기
```

결과

```text
Chicken Salad 제외
Grilled Chicken 제외
```

---

## 4.4 장보기 목록 생성

추천된 메뉴에 필요한 재료를 분석하여 장보기 목록을 생성한다.

예시

```text
양파
계란
상추
돼지고기
김치
```

---

## 4.5 가격 계산

재료 가격 데이터를 이용하여 예상 구매 금액을 계산한다.

출력 예시

```text
총 예상 금액: ₩43,500
```

---

# 5. 시스템 구조

```text
사용자
 ↓
Web UI
 ↓
FastAPI Backend
 ↓
Master Agent
 ├── Context Agent
 │     └── parse-intent Skill
 │
 ├── Menu Planner Agent
 │     └── recipe-mcp
 │
 ├── Inventory Filter Agent
 │     └── fridge-inventory-mcp
 │
 └── Price Optimizer Agent
       └── price-comparison-mcp
 ↓
Shopping Plan
```

---

# 6. Pi 활용 내용

본 프로젝트는 Pi Agent Architecture의 개념을 기반으로 구현되었다.

## Skill

### parse-intent

사용자 입력을 구조화된 컨텍스트 정보로 변환한다.

분석 항목

* 가족 수
* 알레르기
* 장보기 목적
* 예산

출력 예시

```json
{
  "family_size": 4,
  "allergies": [],
  "purpose": "weekly",
  "budget": 50000
}
```

---

## MCP

### recipe-mcp

레시피 정보를 제공한다.

데이터 출처

* TheMealDB API
* 로컬 레시피 데이터

---

### fridge-inventory-mcp

냉장고 재고 정보를 관리한다.

기능

* 보유 재료 조회
* 중복 구매 방지

---

### price-comparison-mcp

재료 가격 정보를 제공한다.

기능

* 가격 조회
* 예상 구매 비용 계산

---

## Agent

### Context Agent

사용자 정보를 분석한다.

### Menu Planner Agent

메뉴를 추천한다.

### Inventory Filter Agent

재고 정보를 기반으로 구매 목록을 정리한다.

### Price Optimizer Agent

예산과 가격 정보를 계산한다.

---

# 7. 기술 스택

## Backend

* Python
* FastAPI

## Frontend

* HTML
* CSS
* JavaScript

## Agent Architecture

* Pi Skill
* MCP
* Multi-Agent Architecture

## External Data

* TheMealDB API

---

# 8. 실행 방법

저장소 클론

```bash
git clone https://github.com/kimiyeon/Smart-Grocery-Agent.git

cd Smart-Grocery-Agent
```

가상환경 생성

```bash
python3 -m venv venv

source venv/bin/activate
```

패키지 설치

```bash
pip install -r requirements.txt
```

서버 실행

```bash
uvicorn app:app --reload
```

브라우저 접속

```text
http://127.0.0.1:8000
```

---

# 9. 향후 개선 사항

* 실제 마트 API 연동
* 실시간 가격 비교
* 영양 성분 분석
* OCR 기반 영수증 분석
* AI 기반 개인 맞춤 식단 추천

---

# 10. 프로젝트 정보

오픈소스소프트웨어 기말 프로젝트

Smart Grocery Agent
