import json
import requests

url = "https://info.cld.hkjc.com/graphql/base/"

# 馬會官方前端獲取足球賽事與賠率的標準 GraphQL Query
payload = {
    "operationName": "allMatchList",
    "query": """
    query allMatchList {
      matches(product: "football") {
        matchId
        matchDate
        matchNum
        homeTeam {
          teamName
        }
        awayTeam {
          teamName
        }
        foPools {
          id
          status
          pools {
            id
            status
            results {
              result
            }
          }
        }
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
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://bet.hkjc.com",
    "Referer": "https://bet.hkjc.com/",
}

try:
    print("⏳ 正在透過 GraphQL 獲取馬會足球賠率與賽事數據...")
    response = requests.post(url, json=payload, headers=headers, timeout=10)
    print(f"📡 HTTP 狀態碼: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print("🎉 成功取得足球賽事與賠率 JSON 數據！內容範例：")
        print(json.dumps(data, indent=2, ensure_ascii=False)[:800])
    else:
        print(f"❌ 請求失敗，回應內容: {response.text[:200]}")

except Exception as e:
    print(f"💥 發生連線異常: {e}")
