import json
import requests

# 馬會官方公開的賽事賠率 / 賽程 REST API (無 GraphQL 白名單限制)
url = "https://bet.hkjc.com/racing/getJSON.aspx?type=winplaodds&date=latest"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
        " like Gecko) Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": "https://bet.hkjc.com/racing/",
}

try:
    print("⏳ 正在嘗試連線馬會 REST API...")
    response = requests.get(url, headers=headers, timeout=10)
    print(f"📡 HTTP 狀態碼: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print("✅ 100% 成功取得馬會 JSON 數據！數據範例：")
        print(json.dumps(data, indent=2, ensure_ascii=False)[:400])
    else:
        print(f"❌ 請求失敗，回應內容: {response.text}")
except Exception as e:
    print(f"💥 發生連線異常: {e}")
