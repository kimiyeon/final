import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  ListToolsRequestSchema,
  CallToolRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "price-mcp",
    version: "1.0.0",
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "compare_prices",
        description: "Compare grocery prices across stores",
        inputSchema: {
          type: "object",
          properties: {
            item: {
              type: "string",
              description: "Grocery item name",
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
    const mockPrices = {
      chicken: {
        coupang: 12000,
        emart: 13500,
        homeplus: 12800,
      },
      egg: {
        coupang: 6000,
        emart: 6500,
        homeplus: 6200,
      },
      milk: {
        coupang: 3200,
        emart: 3500,
        homeplus: 3300,
      },
      tomato: {
        coupang: 2500,
        emart: 2700,
        homeplus: 2600,
      },
      cheese: {
        coupang: 5000,
        emart: 5500,
        homeplus: 5200,
      },
    };

    const item = args.item.toLowerCase();
    const result = mockPrices[item];

    if (!result) {
      return {
        content: [
          {
            type: "text",
            text: `No pricing data found for ${args.item}`,
          },
        ],
      };
    }

    return {
      content: [
        {
          type: "text",
          text: JSON.stringify({
            item: args.item,
            prices: result,
          }),
        },
      ],
    };
  }

  throw new Error("Unknown tool");
});

const transport = new StdioServerTransport();
await server.connect(transport);