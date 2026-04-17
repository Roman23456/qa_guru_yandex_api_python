schema_auth_token = {
  "type": "object",
  "properties": {
    "status": {
      "type": "string"
    },
    "result": {
      "type": "object",
      "properties": {
        "apiKey": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "authScopes": {
              "type": "array",
              "items": {
                "type": "string"
              }
            }
          },
          "required": [
            "name",
            "authScopes"
          ]
        }
      },
      "required": [
        "apiKey"
      ]
    }
  },
  "required": [
    "status",
    "result"
  ],
  "$schema": "https://json-schema.org/draft/2020-12/schema"
}
