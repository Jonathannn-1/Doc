import requests

API_KEY = "ol_api_8VkUci9pHpEU63oGiWgrg9Yt845F2MPelJWUhN"
BASE_URL = "https://app.getoutline.com/api"

response = requests.post(
    f"{BASE_URL}/auth.info",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
)

print(response.status_code)
print(response.json())