# Smart Grocery Agent (스마트 장보기 에이전트)

Pi 기반 멀티 에이전트 구조를 활용한 AI 장보기 도우미 서비스입니다.

---

# 1. 프로젝트 소개

Smart Grocery Agent는 사용자의 장보기 상황을 분석하여 자동으로 장보기 목록을 생성해주는 AI Agent 웹 서비스입니다.

다음 정보를 기반으로 개인화된 장보기 리스트를 생성합니다.

- 가족 구성
- 알레르기 및 기저 질환
- 장보기 목적
- 예산
- 냉장고 재고
- 기존 영수증 구매 내역

AI 에이전트들이 역할을 분담하여 상황 분석, 식단 생성, 중복 제거, 가격 비교를 수행합니다.

---

# 2. 문제 정의

기존 장보기에는 다음과 같은 문제가 있습니다.

- 냉장고에 이미 있는 재료를 다시 구매함
- 가족의 건강 조건이 반영되지 않음
- 예산 초과
- 행사/목적에 맞는 식단 구성의 어려움

본 프로젝트는 이러한 문제를 AI Agent와 외부 도구(MCP)를 활용해 해결합니다.

---

# 3. 서비스 대상 사용자

다음과 같은 사용자를 대상으로 합니다.

- 주간 장보기를 하는 가정
- 아이 식단을 관리하는 부모
- 알레르기가 있는 가족
- 예산 관리가 필요한 사용자
- 캠핑 / 여행 / 파티 준비 사용자

---

# 4. 핵심 기능

## 4.1 Context Analysis

사용자 입력에서 다음 정보를 추출합니다.

- 가족 수
- 알레르기
- 쇼핑 목적
- 예산

---

## 4.2 Menu Planning

사용자 상황에 맞는 식단을 생성합니다.

예시:

- Chicken Salad
- Pasta
- Soup

---

## 4.3 Inventory Filtering

냉장고 재고 MCP 서버와 연동하여 이미 보유한 재료를 제거합니다.

예시:

냉장고 보유 재료:

- egg
- milk
- tomato

→ 장보기 목록에서 제외

---

## 4.4 Price Optimization

마트별 가격을 비교하여 최적 가격을 선택합니다.

비교 대상:

- Coupang
- Emart
- Homeplus

---

## 4.5 Receipt Analysis Extension

기존 영수증을 분석하여 최근 구매 품목을 파악합니다.

중복 구매 방지에 활용됩니다.

---

# 5. 시스템 구조

```text
Web UI
   ↓
FastAPI Backend
   ↓
Pi Runtime (Multi-Agent Architecture)
   ├── Context Analyzer Agent
   ├── Menu Planner Agent
   ├── Inventory Filter Agent
   └── Price Optimizer Agent
          ↓
      MCP Servers
      ├── fridge-inventory-mcp
      └── price-comparison-mcp

Extensions
└── receipt-ocr-extension# Smart Grocery Agent (스마트 장보기 에이전트)

Pi 기반 멀티 에이전트 구조를 활용한 AI 장보기 도우미 서비스입니다.

---

# 1. 프로젝트 소개

Smart Grocery Agent는 사용자의 장보기 상황을 분석하여 자동으로 장보기 목록을 생성해주는 AI Agent 웹 서비스입니다.

다음 정보를 기반으로 개인화된 장보기 리스트를 생성합니다.

- 가족 구성
- 알레르기 및 기저 질환
- 장보기 목적
- 예산
- 냉장고 재고
- 기존 영수증 구매 내역

AI 에이전트들이 역할을 분담하여 상황 분석, 식단 생성, 중복 제거, 가격 비교를 수행합니다.

---

# 2. 문제 정의

기존 장보기에는 다음과 같은 문제가 있습니다.

- 냉장고에 이미 있는 재료를 다시 구매함
- 가족의 건강 조건이 반영되지 않음
- 예산 초과
- 행사/목적에 맞는 식단 구성의 어려움

본 프로젝트는 이러한 문제를 AI Agent와 외부 도구(MCP)를 활용해 해결합니다.

---

# 3. 서비스 대상 사용자

다음과 같은 사용자를 대상으로 합니다.

- 주간 장보기를 하는 가정
- 아이 식단을 관리하는 부모
- 알레르기가 있는 가족
- 예산 관리가 필요한 사용자
- 캠핑 / 여행 / 파티 준비 사용자

---

# 4. 핵심 기능

## 4.1 Context Analysis

사용자 입력에서 다음 정보를 추출합니다.

- 가족 수
- 알레르기
- 쇼핑 목적
- 예산

---

## 4.2 Menu Planning

사용자 상황에 맞는 식단을 생성합니다.

예시:

- Chicken Salad
- Pasta
- Soup

---

## 4.3 Inventory Filtering

냉장고 재고 MCP 서버와 연동하여 이미 보유한 재료를 제거합니다.

예시:

냉장고 보유 재료:

- egg
- milk
- tomato

→ 장보기 목록에서 제외

---

## 4.4 Price Optimization

마트별 가격을 비교하여 최적 가격을 선택합니다.

비교 대상:

- Coupang
- Emart
- Homeplus

---

## 4.5 Receipt Analysis Extension

기존 영수증을 분석하여 최근 구매 품목을 파악합니다.

중복 구매 방지에 활용됩니다.

---

# 5. 시스템 구조


Web UI
   ↓
FastAPI Backend
   ↓
Pi Runtime (Multi-Agent Architecture)
   ├── Context Analyzer Agent
   ├── Menu Planner Agent
   ├── Inventory Filter Agent
   └── Price Optimizer Agent
          ↓
      MCP Servers
      ├── fridge-inventory-mcp
      └── price-comparison-mcp

Extensions
└── receipt-ocr-extension