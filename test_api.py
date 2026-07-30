import requests

url = "https://bet.hkjc.com/racing/getJSON.aspx?type=winplaodds&date=latest"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
        " like Gecko) Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept": "*/*",
    "Referer": "https://bet.hkjc.com/racing/",
}

try:
    print("⏳ 正在嘗試連線馬會 REST API...")
    response = requests.get(url, headers=headers, timeout=10)
    print(f"📡 HTTP 狀態碼: {response.status_code}")

    if response.status_code == 200:
        raw_text = response.text.strip()
        print("🎉 成功取得馬會原始回應數據！前 500 個字元如下：")
        print("=" * 50)
        print(raw_text[:500])
        print("=" * 50)
    else:
        print(f"❌ 請求失敗，回應內容: {response.text}")

except Exception as e:
    print(f"💥 發生連線異常: {e}")
