def serializeDict(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "author": item["author"],
        "genre": item["genre"],
        "year": item["year"],
        "in_stock": "Yes" if item["in_stock"] else "No"
    }


def serializelist(entity) -> list:
    return [serializeDict(item) for item in entity]