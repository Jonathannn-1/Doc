import os
import requests

API_KEY = os.environ.get("OUTLINE_API_KEY", "ol_api_8VkUci9pHpEU63oGiWgrg9Yt845F2MPelJWUhN")
BASE_URL = "https://app.getoutline.com/api"

session = requests.Session()
session.headers.update({
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "Accept": "application/json",
})


def call(method, **params):
    r = session.post(f"{BASE_URL}/{method}", json=params)
    data = r.json()
    if not r.ok or not data.get("ok", False):
        raise RuntimeError(f"Error en '{method}': {data.get('error', r.text)}")
    return data.get("data"), data.get("pagination")


# 1. Verificar conexión
me, _ = call("auth.info")
print(f"Conectado como: {me['user']['name']} ({me['user']['email']})")
print(f"Workspace: {me['team']['name']}\n")

# 2. Listar todas las colecciones
collections = []
offset = 0
while True:
    result, pagination = call("collections.list", limit=100, offset=offset)
    collections.extend(result)
    if len(result) < 100:
        break
    offset += 100

print(f"Colecciones encontradas: {len(collections)}\n")
for c in collections:
    print(f"- {c['name']}  (id: {c['id']})")