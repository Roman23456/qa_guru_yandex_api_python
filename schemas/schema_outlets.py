schema_outlet_error = {
    "type": "object",
    "properties": {
        "status": {"type": "string"},
        "errors": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "code": {"type": "string"},
                    "message": {"type": "string"}
                },
                "required": ["code", "message"]
            }
        }
    },
    "required": ["status", "errors"],
    "$schema": "https://json-schema.org/draft/2020-12/schema"
}

