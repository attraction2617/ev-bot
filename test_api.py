import json
import requests

# 馬會公開且穩定的賽事行事曆 API (無需登入、無白名單限制)
url = "https://racing.hkjc.com/zh-hk/local/information/calendar"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
        " like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": "https://racing.hkjc.com/",
}

try:
    print("⏳ 正在連線馬會公開賽事行事曆 API...")
    response = requests.get(url, headers=headers, timeout=10)
    print(f"📡 HTTP 狀態碼: {response.status_code}")

    if response.status_code == 200:
        print("🎉 成功連線！伺服器正常回應。")
        # 檢查是不是拿到網頁或 JSON
        print(response.text[:300])
    else:
        print(f"❌ 請求失敗，回應內容: {response.text}")

except Exception as e:
    print(f"💥 發生連線異常: {e}")
