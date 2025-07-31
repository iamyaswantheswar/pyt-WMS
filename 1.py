import json
with open("data/users.json", "r") as f:
  data = json.load(f)
print(data)