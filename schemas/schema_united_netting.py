schema_united_netting_request = {
    "type": "object",
    "properties": {
        "campaignId": {"type": "integer"},
        "businessId": {"type": "integer"},
        "monthOfYear": {
            "type": "object",
            "properties": {
                "year": {"type": "integer"},
                "month": {"type": "integer", "minimum": 1, "maximum": 12}
            },
            "required": ["year", "month"]
        },
        "format": {"type": "string", "enum": ["FILE", "CSV", "JSON"]}
    },
    "required": ["businessId", "monthOfYear", "format"],
    "$schema": "https://json-schema.org/draft/2020-12/schema"
}


schema_united_netting = {
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