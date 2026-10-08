import os
import requests

API_KEY = "ol_api_8VkUci9pHpEU63oGiWgrg9Yt845F2MPelJWUhN"
BASE_URL = "https://app.getoutline.com/api"

COLLECTION_ID = "e76e4575-d9d8-4044-b8ef-954f98af8ec6"  # "Parametros pruebas"

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


# 1. Listar todos los documentos de la colección
documents = []
offset = 0
while True:
    result, pagination = call(
        "documents.list",
        collectionId=COLLECTION_ID,
        limit=100,
        offset=offset,
    )
    documents.extend(result)
    if len(result) < 100:
        break
    offset += 100

print(f"Documentos encontrados en la colección: {len(documents)}\n")

# 2. Traer el contenido completo (texto en markdown) de cada documento
for i, doc_meta in enumerate(documents, start=1):
    doc, _ = call("documents.info", id=doc_meta["id"])
    title = doc.get("title", "Sin título")
    text = doc.get("text", "")

    print(f"{'='*60}")
    print(f"[{i}] {title}")
    print(f"{'='*60}")
    print(text)
    print("\n")