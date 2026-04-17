schema_settings={
  "type": "object",
  "properties": {
    "settings": {
      "type": "object",
      "properties": {
        "countryRegion": {
          "type": "integer"
        },
        "shopName": {
          "type": "string"
        },
        "useOpenStat": {
          "type": "boolean"
        },
        "localRegion": {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            },
            "type": {
              "type": "string"
            },
            "deliveryOptionsSource": {
              "type": "string"
            },
            "delivery": {
              "type": "object",
              "properties": {
                "schedule": {
                  "type": "object",
                  "properties": {
                    "availableOnHolidays": {
                      "type": "boolean"
                    },
                    "customHolidays": {
                      "type": "array",
                      "items": {}
                    },
                    "customWorkingDays": {
                      "type": "array",
                      "items": {}
                    },
                    "period": {
                      "type": "object",
                      "properties": {
                        "fromDate": {
                          "type": "string"
                        },
                        "toDate": {
                          "type": "string"
                        }
                      },
                      "required": [
                        "fromDate",
                        "toDate"
                      ]
                    },
                    "totalHolidays": {
                      "type": "array",
                      "items": {
                        "type": "string"
                      }
                    },
                    "weeklyHolidays": {
                      "type": "array",
                      "items": {
                        "type": "integer"
                      }
                    }
                  },
                  "required": [
                    "availableOnHolidays",
                    "customHolidays",
                    "customWorkingDays",
                    "period",
                    "totalHolidays",
                    "weeklyHolidays"
                  ]
                }
              },
              "required": [
                "schedule"
              ]
            }
          },
          "required": [
            "id",
            "name",
            "type",
            "deliveryOptionsSource",
            "delivery"
          ]
        }
      },
      "required": [
        "countryRegion",
        "shopName",
        "useOpenStat",
        "localRegion"
      ]
    }
  },
  "required": [
    "settings"
  ],
  "$schema": "https://json-schema.org/draft/2020-12/schema"
}

