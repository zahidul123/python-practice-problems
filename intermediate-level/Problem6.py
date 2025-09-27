### Problem-6: Flatten a Nested JSON
#Flatten a nested dictionary for storage in tabular format or NoSQL DB.
#-   **Input**: `{"a": {"b": 1}}`  
#-   **Output**: `{"a.b": 1}`   
#-   **Hint**: Use recursion.

def flatten_json(nested_json, parent_key='', sep='.'):
    items = []
    for k, v in nested_json.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key).items())
        else:
            items.append((new_key, v))
    return dict(items)

nested_json = {"a": {"b": 1, "c": {"d": 2}}, "e": 3}
flattened_json = flatten_json(nested_json)
print(flattened_json)  