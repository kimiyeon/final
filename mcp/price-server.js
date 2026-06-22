import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
ListToolsRequestSchema,
CallToolRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
{
name: "price-mcp",
version: "1.1.0",
},
{
capabilities: {
tools: {},
},
}
);

const PRICE_RULES = [
{
keywords: ["beef"],
category: "meat",
prices: { coupang: 15000, emart: 16500, homeplus: 15800 },
},
{
keywords: ["pork", "pork_belly"],
category: "meat",
prices: { coupang: 12000, emart: 13000, homeplus: 12500 },
},
{
keywords: ["chicken", "chicken_breast"],
category: "meat",
prices: { coupang: 10000, emart: 11500, homeplus: 10800 },
},
{
keywords: ["salmon"],
category: "seafood",
prices: { coupang: 14000, emart: 15000, homeplus: 14500 },
},
{
keywords: ["fish", "tuna", "shrimp", "prawn"],
category: "seafood",
prices: { coupang: 9000, emart: 10000, homeplus: 9500 },
},
{
keywords: ["rice"],
category: "grain",
prices: { coupang: 9000, emart: 9500, homeplus: 9200 },
},
{
keywords: ["egg", "eggs", "egg_yolk", "egg_yolks"],
category: "egg",
prices: { coupang: 6000, emart: 6500, homeplus: 6200 },
},
{
keywords: ["milk"],
category: "dairy",
prices: { coupang: 3200, emart: 3500, homeplus: 3300 },
},
{
keywords: ["cheese"],
category: "dairy",
prices: { coupang: 5000, emart: 5500, homeplus: 5200 },
},
{
keywords: ["butter", "unsalted_butter", "melted_butter"],
category: "dairy",
prices: { coupang: 4500, emart: 5200, homeplus: 4800 },
},
{
keywords: ["flour", "plain_flour", "all_purpose_flour", "self_raising_flour"],
category: "baking",
prices: { coupang: 2500, emart: 2800, homeplus: 2600 },
},
{
keywords: ["sugar", "caster_sugar", "granulated_sugar"],
category: "baking",
prices: { coupang: 2200, emart: 2500, homeplus: 2300 },
},
{
keywords: ["baking_powder", "bicarbonate_of_soda", "cornstarch"],
category: "baking",
prices: { coupang: 1800, emart: 2200, homeplus: 2000 },
},
{
keywords: ["vanilla", "vanilla_extract", "cinnamon", "cardamom"],
category: "seasoning",
prices: { coupang: 2500, emart: 3000, homeplus: 2800 },
},
{
keywords: ["salt"],
category: "seasoning",
prices: { coupang: 1000, emart: 1200, homeplus: 1100 },
},
{
keywords: ["oil"],
category: "pantry",
prices: { coupang: 4500, emart: 5200, homeplus: 4800 },
},
{
keywords: ["pasta"],
category: "grain",
prices: { coupang: 4000, emart: 4500, homeplus: 4200 },
},
{
keywords: ["bread"],
category: "bakery",
prices: { coupang: 3500, emart: 3900, homeplus: 3600 },
},
{
keywords: ["tomato"],
category: "vegetable",
prices: { coupang: 2500, emart: 2700, homeplus: 2600 },
},
{
keywords: ["lettuce"],
category: "vegetable",
prices: { coupang: 3000, emart: 3300, homeplus: 3100 },
},
{
keywords: ["onion"],
category: "vegetable",
prices: { coupang: 2000, emart: 2300, homeplus: 2100 },
},
{
keywords: ["potato"],
category: "vegetable",
prices: { coupang: 3000, emart: 3500, homeplus: 3200 },
},
{
keywords: ["carrot"],
category: "vegetable",
prices: { coupang: 2500, emart: 2800, homeplus: 2600 },
},
{
keywords: ["apple", "apples"],
category: "fruit",
prices: { coupang: 6000, emart: 6500, homeplus: 6200 },
},
{
keywords: ["banana"],
category: "fruit",
prices: { coupang: 4000, emart: 4500, homeplus: 4200 },
},
{
keywords: ["grape"],
category: "fruit",
prices: { coupang: 8000, emart: 9000, homeplus: 8500 },
},
{
keywords: ["lemon", "lemon_zest"],
category: "fruit",
prices: { coupang: 2500, emart: 3000, homeplus: 2700 },
},
{
keywords: ["garlic"],
category: "vegetable",
prices: { coupang: 2500, emart: 2800, homeplus: 2600 },
},
{
keywords: ["sausage"],
category: "processed_meat",
prices: { coupang: 6000, emart: 6500, homeplus: 6200 },
},
{
keywords: ["ham"],
category: "processed_meat",
prices: { coupang: 4500, emart: 5000, homeplus: 4700 },
},
{
keywords: ["chocolate"],
category: "dessert",
prices: { coupang: 3500, emart: 4000, homeplus: 3700 },
},
];

const DEFAULT_PRICE = {
category: "unknown",
prices: { coupang: 3000, emart: 3500, homeplus: 3200 },
reason: "No exact rule matched. Used default grocery estimate.",
};

function findRule(item) {
const normalized = item.toLowerCase().replaceAll(" ", "_");

for (const rule of PRICE_RULES) {
for (const keyword of rule.keywords) {
if (normalized.includes(keyword)) {
return {
...rule,
matchedKeyword: keyword,
confidence: keyword === normalized ? "high" : "medium",
reason: `Matched keyword: ${keyword}`,
};
}
}
}

return {
...DEFAULT_PRICE,
matchedKeyword: null,
confidence: "low",
};
}

function getBestStore(prices) {
let bestStore = null;
let bestPrice = Infinity;

for (const [store, price] of Object.entries(prices)) {
if (price < bestPrice) {
bestStore = store;
bestPrice = price;
}
}

return { bestStore, bestPrice };
}

server.setRequestHandler(ListToolsRequestSchema, async () => {
return {
tools: [
{
name: "compare_prices",
description:
"Estimate and compare grocery ingredient prices across stores using keyword-based price rules.",
inputSchema: {
type: "object",
properties: {
item: {
type: "string",
description: "Grocery item or ingredient name",
},
family_size: {
type: "number",
description: "Number of family members",
},
purpose: {
type: "string",
description: "Shopping purpose such as weekly, diet, birthday, or camping",
},
},
required: ["item"],
},
},
],
};
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
const { name, arguments: args } = request.params;

if (name === "compare_prices") {
const item = args.item;
const rule = findRule(item);
const { bestStore, bestPrice } = getBestStore(rule.prices);

```
return {
  content: [
    {
      type: "text",
      text: JSON.stringify({
        item,
        category: rule.category,
        prices: rule.prices,
        best_store: bestStore,
        estimated_price: bestPrice,
        confidence: rule.confidence,
        reason: rule.reason,
        source: "price-mcp",
      }),
    },
  ],
};
```

}

throw new Error("Unknown tool");
});

const transport = new StdioServerTransport();
await server.connect(transport);
