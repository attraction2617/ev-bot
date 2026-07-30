import json
import requests

# 馬會足球即時賠率的底層資料接口
url = "https://bet.hkjc.com/football/ch/football-odds.aspx"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
        " like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": "https://bet.hkjc.com/football/",
    "X-Requested-With": "XMLHttpRequest",
}

try:
    print("⏳ 正在嘗試以 Ajax 方式請求馬會足球數據...")
    response = requests.get(url, headers=headers, timeout=10)
    print(f"📡 HTTP 狀態碼: {response.status_code}")
    print(f"📡 Content-Type: {response.headers.get('Content-Type', '')}")

    if response.status_code == 200:
        raw_text = response.text.strip()
        print("🎉 成功取得回應！內容前 400 字如下：")
        print(raw_text[:400])
    else:
        print(f"❌ 請求失敗，回應內容: {response.text[:200]}")

except Exception as e:
    print(f"💥 發生連線異常: {e}")
