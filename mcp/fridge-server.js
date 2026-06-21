import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
  ListToolsRequestSchema,
  CallToolRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";

const server = new Server(
  {
    name: "fridge-mcp",
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
        name: "get_inventory",
        description: "Get fridge inventory items",
        inputSchema: {
          type: "object",
          properties: {
            user_id: {
              type: "string",
              description: "User ID",
            },
          },
          required: ["user_id"],
        },
      },
    ],
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  if (name === "get_inventory") {
    const inventory = ["egg", "milk", "tomato", "cheese"];

    return {
      content: [
        {
          type: "text",
          text: JSON.stringify({
            user_id: args.user_id,
            inventory,
          }),
        },
      ],
    };
  }

  throw new Error("Unknown tool");
});

const transport = new StdioServerTransport();
await server.connect(transport);