shema_campaigns = {
  "type": "object",
  "properties": {
    "campaigns": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "domain": {
            "type": "string"
          },
          "id": {
            "type": "integer"
          },
          "clientId": {
            "type": "integer"
          },
          "business": {
            "type": "object",
            "properties": {
              "id": {
                "type": "integer"
              },
              "name": {
                "type": "string"
              }
            },
            "required": [
              "id",
              "name"
            ]
          },
          "placementType": {
            "type": "string"
          },
          "apiAvailability": {
            "type": "string"
          }
        },
        "required": [
          "domain",
          "id",
          "clientId",
          "business",
          "placementType",
          "apiAvailability"
        ]
      }
    },
    "pager": {
      "type": "object",
      "properties": {
        "total": {
          "type": "integer"
        },
        "from": {
          "type": "integer"
        },
        "to": {
          "type": "integer"
        },
        "currentPage": {
          "type": "integer"
        },
        "pagesCount": {
          "type": "integer"
        },
        "pageSize": {
          "type": "integer"
        }
      },
      "required": [
        "total",
        "from",
        "to",
        "currentPage",
        "pagesCount",
        "pageSize"
      ]
    },
    "paging": {
      "type": "object"
    }
  },
  "required": [
    "campaigns",
    "pager",
    "paging"
  ],
  "$schema": "https://json-schema.org/draft/2020-12/schema"
}

