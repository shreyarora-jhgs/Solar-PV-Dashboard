from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Allow browser access

# --- CONFIG ---
TOKEN = "20241014173051679020793"
SN = "SNCFEQ7HZP"
SOLAX_API_URL = "https://global.solaxcloud.com/proxyApp/proxy/api/getRealtimeInfo.do"

@app.route("/live")
def live_data():
    try:
        # Fetch data from Solax Cloud
        response = requests.get(SOLAX_API_URL, params={"tokenId": TOKEN, "sn": SN}, timeout=10)
        data = response.json().get("result", {})

        # Convert values to kW/kWh
        result = {
            "pv_power_kw": round((data.get("acpower", 0) or 0) / 1000, 3),
            "yield_today_kwh": round(data.get("yieldtoday", 0) or 0, 3),
            "consumption_kwh": round((data.get("consumeenergy", 0) or 0) / 1000, 3),
            "imported_kwh": round((data.get("feedinenergy", 0) or 0) / 1000, 3),
            "last_update": data.get("uploadTime")
        }
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
