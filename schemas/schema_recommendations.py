schema_recommendations_request = {
    "type": "object",
    "properties": {
        "offerIds": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 1
        },
        "competitivenessFilter": {
            "type": "string",
            "enum": ["OPTIMAL", "GOOD", "BEST"]
        }
    },
    "required": ["offerIds"],
    "$schema": "https://json-schema.org/draft/2020-12/schema"
}


schema_recommendation = {
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "result": {
      "type": "object",
      "properties": {
        "paging": {
          "type": "object"
        },
        "offerRecommendations": {
          "type": "array",
          "items": {}
        }
      },
      "required": [
        "paging",
        "offerRecommendations"
      ]
    }
  },
  "required": [
    "status",
    "result"
  ],
  "$schema": "https://json-schema.org/draft/2020-12/schema"
}