import json
import re
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

        # 嘗試直接解析 JSON；如果包了 JS 變數，就用正則表達式把 JSON 抓出來
        try:
            data = response.json()
        except Exception:
            # 尋找第一個 { 到最後一個 } 之間的 JSON 內容
            json_match = re.search(r"\{.*\}", raw_text, re.DOTALL)
            if json_match:
                data = json.loads(json_match.group())
            else:
                raise ValueError(
                    f"無法從回應中解析 JSON，原始內容前 100 字: {raw_text[:100]}"
                )

        print("🎉 100% 成功取得並解析馬會 JSON 數據！數據範例：")
        print(json.dumps(data, indent=2, ensure_ascii=False)[:500])
    else:
        print(f"❌ 請求失敗，回應內容: {response.text}")

except Exception as e:
    print(f"💥 發生解析/連線異常: {e}")
