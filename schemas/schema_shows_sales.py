schema_shows_sales_request = {
    "type": "object",
    "properties": {
        "businessId": {"type": "integer"},
        "dateFrom": {"type": "string"},
        "dateTo": {"type": "string"},
        "grouping": {"type": "string", "enum": ["CATEGORIES", "OFFERS"]}
    },
    "required": ["businessId", "dateFrom", "dateTo", "grouping"],
    "$schema": "https://json-schema.org/draft/2020-12/schema"
}

schema_shows_sales = {
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "result": {
      "type": "object",
      "properties": {
        "reportId": {
          "type": "string",
          "format": "uuid"
        },
        "estimatedGenerationTime": {
          "type": "integer"
        }
      },
      "required": [
        "reportId",
        "estimatedGenerationTime"
      ]
    }
  },
  "required": [
    "status",
    "result"
  ],
  "$schema": "https://json-schema.org/draft/2020-12/schema"
}


