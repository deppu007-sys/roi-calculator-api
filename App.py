from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "ROI Calculator API Running 🚀"

@app.route('/roi')
def roi():
    clicks = int(request.args.get('clicks', 0))
    conversions = int(request.args.get('conversions', 0))
    cpc = float(request.args.get('cpc', 5))
    rpc = float(request.args.get('rpc', 100))

    revenue = conversions * rpc
    cost = clicks * cpc
    profit = revenue - cost
    roi_percent = (profit / cost * 100) if cost > 0 else 0

    return {
        "clicks": clicks,
        "conversions": conversions,
        "revenue": revenue,
        "cost": cost,
        "profit": profit,
        "roi_percent": round(roi_percent, 2)
    }

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
