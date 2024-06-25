from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inventory')
def inventory():
    return render_template('inventory.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

app.run(debug=True, port=3000)