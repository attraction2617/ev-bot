import json
import requests

# 建立一個 Session 物件，用來自動保存馬會發給我們的 Cookies
session = requests.Session()

# 模擬正規瀏覽器的 Headers
session.headers.update(
    {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
            " like Gecko) Chrome/124.0.0.0 Safari/537.36"
        ),
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://bet.hkjc.com",
        "Referer": "https://bet.hkjc.com/football/index.aspx",
    }
)

url = "https://info.cld.hkjc.com/graphql/base/"

# 馬會標準的足球賽事與賠率查詢 Query
payload = {
    "operationName": "matches",
    "query": """
    query matches {
      matches(product: "football") {
        matchId
        matchDate
        homeTeam {
          teamName
        }
        awayTeam {
          teamName
        }
      }
    }
    """,
}

try:
    print("⏳ 正在透過 Session 連線馬會 GraphQL 總部...")

    # 步驟 1：先訪問主頁拿到 Cookie 授權
    session.get("https://bet.hkjc.com/football/index.aspx", timeout=10)

    # 步驟 2：帶著 Cookie 發送 GraphQL POST 請求
    response = session.post(url, json=payload, timeout=10)
    print(f"📡 HTTP 狀態碼: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print("🎉 成功取得數據！內容如下：")
        print(json.dumps(data, indent=2, ensure_ascii=False)[:600])
    else:
        print(f"❌ 請求失敗，回應內容: {response.text[:200]}")

except Exception as e:
    print(f"💥 發生連線異常: {e}")
