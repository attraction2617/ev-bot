import requests

# 你的專屬金鑰
TELEGRAM_BOT_TOKEN = "8960910029:AAHqYWwICbrcSAj4a-rFSkldpUWWeGyQmSk"
TELEGRAM_CHAT_ID = "1360322970"
ODDS_API_KEY = "e75ff8b4a75f6755f6e583ff19d30500"

print("正在測試 Telegram Bot...")
url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": TELEGRAM_CHAT_ID,
    "text": "🟢 測試成功！雷達已經可以順利呼叫你的 Telegram。",
    "parse_mode": "Markdown",
}
res = requests.post(url, json=payload)
if res.ok:
  print("✅ Telegram 測試成功！請檢查手機有沒有收到訊息。")
else:
  print(f"❌ Telegram 測試失敗: {res.text}")

print("\n正在測試 The Odds API...")
# 測試抓取英超賽事
api_url = f"https://api.the-odds-api.com/v4/sports/soccer_epl/odds/?apiKey={ODDS_API_KEY}&regions=pinnacle&markets=h2h"
res_odds = requests.get(api_url)

if res_odds.status_code == 200:
  data = res_odds.json()
  print(
      f"✅ The Odds API 測試成功！目前英超可抓取的賽事數量: {len(data)} 場"
  )
  if len(data) > 0:
    print(f"   範例比賽: {data[0]['home_team']} vs {data[0]['away_team']}")
else:
  print(
      f"❌ The Odds API 測試失敗 (Status {res_odds.status_code}):"
      f" {res_odds.text}"
  )
