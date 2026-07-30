import json
import requests

# 馬會官方網頁前端用來載入足球賠率的固定 JSON 資料源
url = "https://bet.hkjc.com/football/getJSON.aspx?ext=odds.aspx&matchdate=today"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
        " like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "*/*",
    "Referer": "https://bet.hkjc.com/football/index.aspx",
}

try:
    print("⏳ 正在直接下載馬會足球即時賠率 JSON 檔案...")
    response = requests.get(url, headers=headers, timeout=10)
    print(f"📡 HTTP 狀態碼: {response.status_code}")

    if response.status_code == 200:
        raw_text = response.text.strip()
        print("🎉 成功取得回應！內容前 400 字如下：")
        print(raw_text[:400])
    else:
        print(f"❌ 請求失敗，回應內容: {response.text[:200]}")

except Exception as e:
    print(f"💥 發生連線異常: {e}")
