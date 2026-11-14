from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

# Tells Flask to look for HTML files inside the 'templates' folder
app = Flask(__name__, template_folder="templates")
CORS(app)


# This now serves your website directly at http://localhost:5000
@app.route("/")
def home():
  return render_template("index.html")


@app.route("/api/sync-broker", methods=["POST"])
def sync_broker():
  req_data = request.json or {}
  email = req_data.get("email")
  password = req_data.get("password")

  if not email or not password:
    return jsonify(
        {"status": "error", "message": "Email and password are required."}
    ), 400

  # Simulated broker closed order synchronization payload
  fetched_trades = [
      {
          "id": 101,
          "date": "2026-11-13",
          "asset": "EUR/USD",
          "direction": "Long",
          "result": "Win",
          "netPnL": 450.0,
      },
      {
          "id": 102,
          "date": "2026-11-14",
          "asset": "GBP/JPY",
          "direction": "Short",
          "result": "Win",
          "netPnL": 300.0,
      },
  ]

  return jsonify({"status": "success", "trades": fetched_trades}), 200


if __name__ == "__main__":
  print("QuantEdge Pro Server running on http://localhost:5000")
  app.run(host="0.0.0.0", port=5000, debug=True)
