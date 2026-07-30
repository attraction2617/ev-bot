import json
import requests

url = "https://info.cld.hkjc.com/graphql/base/"

payload = {
    "operationName": "racing",
    "query": """
    query racing {
      raceMeetings(find: {status: "UPCOMING"}, limit: 1) {
        date
        venueCode
        races {
          raceNo
          status
        }
      }
    }
    """,
}

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
        " like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    "Content-Type": "application/json",
}

try:
    print("⏳ 正在嘗試連線馬會 GraphQL API...")
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    print(f"📡 HTTP 狀態碼: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print("✅ 成功取得馬會 JSON 數據！結構範例如下：")
        print(json.dumps(data, indent=2, ensure_ascii=False)[:300])
    else:
        print(f"❌ 請求失敗，回應內容: {response.text}")
except Exception as e:
    print(f"💥 發生連線異常: {e}")
