import json
import requests

url = "https://info.cld.hkjc.com/graphql/base/"

# 最簡化且符合馬會最新 Schema 的 Query
payload = {
    "operationName": "raceMeetings",
    "query": """
    query raceMeetings {
      raceMeetings {
        date
        venueCode
      }
    }
    """,
}

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
        " like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Origin": "https://racing.hkjc.com",
    "Referer": "https://racing.hkjc.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
}

try:
    print("⏳ 正在帶入新版 Header 連線馬會 GraphQL API...")
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    print(f"📡 HTTP 狀態碼: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print("🎉 100% 成功取得馬會即時賽事 JSON 數據！內容如下：")
        print(json.dumps(data, indent=2, ensure_ascii=False)[:600])
    else:
        print(f"❌ 請求失敗，回應內容: {response.text}")

except Exception as e:
    print(f"💥 發生連線異常: {e}")
