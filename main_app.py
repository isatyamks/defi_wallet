from flask import Flask, render_template, jsonify, request
# import models.price_forecast as pf
# import models.trade_detection as td
# import models.threat_detection as thd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/analyze-patterns')
def analyze_patterns():
    patterns = thd.analyze_patterns()
    return jsonify(patterns)

@app.route('/forecast-price', methods=['POST'])
def forecast_price():
    data = request.json
    predicted_price = pf.predict(data)  
    return jsonify({'predicted_price': predicted_price})

@app.route('/suspicious-trades')
def suspicious_trades():
    suspicious_trades = td.detect_suspicious_trades()
    return jsonify(suspicious_trades)

@app.route('/optimize-smart-contract', methods=['POST'])
def optimize_contract():
    contract_code = request.form['contract_code']  
    optimization_suggestions = thd.optimize_contract(contract_code)
    return render_template('optimize_contract.html', suggestions=optimization_suggestions)

if __name__ == '__main__':
    app.run(debug=True)
