# Project Report — Smart Grocery AI Agent

## 1. Selected Scenario

Scenario Category: Shopping / Commerce
Project Topic: Automatic Shopping List Generation Agent

This project focuses on building an AI agent system that automatically generates personalized grocery shopping lists based on user context such as recipes, family composition, allergies, and budget constraints.

---

## 2. Problem Definition

Modern households often face several grocery-related inefficiencies:

* Purchasing duplicate ingredients already available at home
* Difficulty planning meals for the week
* Ignoring allergies or dietary restrictions
* Exceeding grocery budgets
* Spending time manually comparing grocery items

These problems become more difficult for families with children, pets, or special dietary requirements.

The goal of this project is to automate grocery planning using an AI agent architecture.

---

## 3. Target Users

The service targets users who regularly manage grocery shopping.

Primary users include:

* Busy working families
* Parents with children
* Health-conscious users
* Diet-focused individuals
* Budget-sensitive shoppers

Example user:
A family of three (two adults and one child) planning weekly groceries with allergy restrictions and budget constraints.

---

## 4. Core Features

### 4.1 Context Analysis

The system collects and analyzes user input:

* Family composition
* Allergies
* Shopping purpose
* Budget

Example:

* Family: adult, child
* Allergy: peanut
* Purpose: weekly shopping
* Budget: ₩100,000

---

### 4.2 Meal Planning

The AI generates a personalized meal plan.

Example meals:

* Chicken Salad
* Pasta
* Soup

Meal planning considers:

* User goals
* Allergies
* Diet restrictions

---

### 4.3 Inventory Filtering

The system checks existing fridge inventory.

Example:
Fridge contains:

* Milk
* Egg
* Onion

If ingredients already exist, they are removed from the shopping list.

This reduces duplicate purchases.

---

### 4.4 Price Optimization

The system compares item prices from a pricing database.

It calculates:

* Individual item prices
* Total cost
* Budget compliance

This helps users minimize grocery spending.

---

## 5. System Architecture

The service follows a multi-agent AI architecture.

Architecture:

Web UI
↓
Master Agent
├── Context Analyzer Agent
├── Menu Planner Agent
├── Inventory Filter Agent
└── Price Optimizer Agent
↓
MCP Tools
↓
Data Sources

---

### 5.1 Master Agent

The Master Agent orchestrates the workflow.

Responsibilities:

* Receive user input
* Trigger sub-agents
* Collect outputs
* Generate final result

---

### 5.2 Context Analyzer Agent

Responsibilities:

* Parse user intent
* Extract family information
* Detect allergies
* Parse budget

Input:
Raw user form data

Output:
Structured context JSON

---

### 5.3 Menu Planner Agent

Responsibilities:

* Generate meal plan
* Determine required ingredients

Input:
Context information

Output:
Meal plan + ingredient list

---

### 5.4 Inventory Filter Agent

Responsibilities:

* Compare ingredients with fridge inventory
* Remove duplicates

Input:
Ingredient list

Output:
Filtered shopping list

---

### 5.5 Price Optimizer Agent

Responsibilities:

* Retrieve product prices
* Calculate total cost
* Optimize budget

Input:
Shopping list

Output:
Final priced cart

---

## 6. Skill Usage

Skills are reusable instruction modules that guide agent behavior.

Implemented skills:

### Parse Intent Skill

Used by Context Analyzer Agent.

Purpose:

* Parse user intent
* Extract shopping requirements

---

### Diet Timeline Skill

Used by Menu Planner Agent.

Purpose:

* Generate meal schedules
* Respect health restrictions

---

### Fridge Dedup Skill

Used by Inventory Filter Agent.

Purpose:

* Remove duplicate ingredients

---

### Route Indexing Skill

Used by Price Optimizer Agent.

Purpose:

* Minimize shopping cost

---

## 7. MCP Usage

MCP tools connect agents to external tools and databases.

Implemented MCP tools:

### fridge-inventory-mcp

Simulates smart fridge inventory database.

Stores:

* Remaining ingredients
* Available inventory

---

### recipe-ingredient-mcp

Recipe database containing:

* Meal templates
* Ingredient mappings

---

### price-mcp

Pricing database containing:

* Product prices
* Shopping cost data

These MCP modules simulate real-world APIs.

---

## 8. Pi Extension Usage

Extensions are modular components used to expand system functionality.

Implemented extensions:

### receipt-ocr-extension

Simulates OCR-based receipt analysis.

Future capability:

* Parse past grocery receipts
* Predict frequently purchased items

---

### grocery-extension

Provides store recommendation.

Future capability:

* Recommend cheapest grocery store
* Support route optimization

---

## 9. Web UI

A simple web interface was implemented.

Input components:

* Family members
* Allergies
* Shopping purpose
* Budget

Output components:

* Meal plan
* Shopping list
* Total cost

The UI allows users to interact with the AI agent system directly.

---

## 10. Implementation Results

Example input:

* Family: adult, child
* Allergy: peanut
* Purpose: weekly
* Budget: ₩100,000

Example output:

Meal Plan:

* Chicken Salad
* Pasta
* Soup

Shopping List:

* chicken
* lettuce
* tomato
* pasta
* tomato_sauce
* cheese
* potato
* carrot

Total Cost:
₩35,500

The system successfully generated personalized grocery recommendations.

---

## 11. Limitations

Current prototype has several limitations:

* Uses mock databases instead of real APIs
* No real retailer integration
* No production OCR pipeline
* No IoT smart fridge connection
* Pi SDK not fully integrated

---

## 12. Future Improvements

Potential improvements include:

* Real Pi SDK integration
* Real grocery retailer APIs
* OCR-based receipt parsing
* Smart fridge IoT integration
* LLM-powered advanced meal recommendation
* Personalized long-term grocery prediction

---

## 13. Conclusion

Smart Grocery AI Agent demonstrates how multi-agent AI systems can improve grocery planning.

By combining:

* Pi-style agent architecture
* Skills
* MCP tools
* Extensions
* Web UI

the system successfully provides personalized and budget-aware grocery recommendations.

This project demonstrates the practical potential of AI agents in everyday shopping scenarios.
