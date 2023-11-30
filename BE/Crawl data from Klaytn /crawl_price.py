import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine


engine = create_engine("mysql+pymysql://dioxtfeq_haods:Syhaobn123@localhost/dioxtfeq_db")
chain_id = "1001"
api_key = "KASKZXCSXPNIND81RVA6DNSC"
api_secret = "X94rvIK5-2VDOvGHpaOWA83JGMKNsFNgnUgl73vA"


def get_realtime_price_klay(chain_id: str):
    url = "https://th-api.klaytnapi.com/v2/cryptocurrency/klay"
    headers = {
        "x-chain-id": chain_id,
        "Authorization": "Basic S0FTS1pYQ1NYUE5JTkQ4MVJWQTZETlNDOlg5NHJ2SUs1LTJWRE92R0hwYU9XQTgzSkdNS05zRk5nblVnbDczdkE=",
        "Content-Type": "application/json",
    }
    response = requests.get(url, headers=headers, auth=(api_key, api_secret))

    json_data = response.json()

    return json_data
    
    
df = pd.DataFrame(columns=["symbol", "krw", "usd", "volume24H", "percentChange24H", "createdAt"])

json_data = get_realtime_price_klay(chain_id)

idx = len(df)
df.loc[idx, "symbol"] = json_data["symbol"]
df.loc[idx, "krw"] = json_data["krw"]
df.loc[idx, "usd"] = json_data["usd"]
df.loc[idx, "volume24H"] = json_data["volume24H"]
df.loc[idx, "percentChange24H"] = json_data["percentChange24H"]
df.loc[idx, "createAt"] = json_data["createdAt"]

print(df)
df.to_sql("klaytn_price", index=False, con=engine, if_exists="append")