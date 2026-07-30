import json
import requests

url = "https://info.cld.hkjc.com/graphql/base/"

# 馬會現行標準 GraphQL Query (針對排位賽事)
payload = {
    "operationName": "raceMeetings",
    "query": """
    query raceMeetings {
      raceMeetings {
        date
        venueCode
        status
      }
    }
    """,
}

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
        " like Gecko) Chrome/122.0.0.0 Safari/537.36"
    ),
    "Content-Type": "application/json",
    "Origin": "https://racing.hkjc.com",
    "Referer": "https://racing.hkjc.com/",
}

try:
    print("⏳ 正在嘗試連線馬會 GraphQL API...")
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    print(f"📡 HTTP 狀態碼: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print("✅ 100% 成功取得馬會 JSON 數據！數據範例：")
        print(json.dumps(data, indent=2, ensure_ascii=False)[:400])
    else:
        print(f"❌ 請求失敗，回應內容: {response.text}")
except Exception as e:
    print(f"💥 發生連線異常: {e}")
