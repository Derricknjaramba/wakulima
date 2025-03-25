import requests
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from datetime import datetime
from flask_cors import CORS
from config import Config
from models import Product  # Assuming Product class exists in models.py

app = Flask(__name__)
api = Api(app)

# Enable CORS for localhost:3000
CORS(app, origins=["http://localhost:3000"])

# In-memory data storage for products and inventory (for demonstration purposes)
products = {}

# Authenticate and get access token from Safaricom M-Pesa API
def authenticate():
    auth = (Config.CONSUMER_KEY, Config.CONSUMER_SECRET)
    response = requests.get(Config.OAUTH_URL, auth=auth)
    if response.status_code == 200:
        auth_response = response.json()
        return auth_response.get('access_token', None)
    else:
        return None

# Endpoint to trigger STK push payment
class STKPush(Resource):
    def post(self):
        data = request.get_json()
        amount = data.get('amount')
        phone_number = data.get('phone_number')
        account_reference = data.get('account_reference')
        transaction_description = data.get('transaction_description')

        access_token = authenticate()

        if access_token:
            headers = {
                'Authorization': f'Bearer {access_token}',
                'Content-Type': 'application/json',
            }

            payload = {
                'BusinessShortcode': Config.BUSINESS_SHORTCODE,
                'Password': Config.BUSINESS_SHORTCODE_PASSWORD,
                'LipaNaMpesaOnlineShortcode': Config.LIPA_NA_MPESA_SHORTCODE,
                'LipaNaMpesaOnlineShortcodePassword': Config.LIPA_NA_MPESA_SHORTCODE_PASSWORD,
                'Amount': amount,
                'PhoneNumber': phone_number,
                'AccountReference': account_reference,
                'TransactionDescription': transaction_description
            }

            # Sending the request to M-Pesa STK Push API
            response = requests.post(Config.LIPA_NA_MPESA_URL, json=payload, headers=headers)

            if response.status_code == 200:
                return jsonify({'message': 'Payment initiated successfully', 'response': response.json()}), 200
            else:
                error_message = response.json().get('errorMessage', 'Unknown error')
                return jsonify({'message': 'Error initiating payment', 'error': error_message}), 400
        else:
            return jsonify({'message': 'Authentication failed, unable to initiate payment.'}), 401

# Stock tracking endpoint: Provides real-time stock levels
class StockTracking(Resource):
    def get(self):
        stock_levels = {}
        for product_name, product in products.items():
            stock_levels[product_name] = {
                'stock_level': product.stock_level,
                'sales': product.sales
            }
        return jsonify(stock_levels)

# Low stock alert endpoint: Alerts when stock is low
class LowStockAlert(Resource):
    def get(self):
        low_stock = {}
        for product_name, product in products.items():
            if product.stock_level < 10:  # Define low stock threshold
                low_stock[product_name] = product.stock_level
        return jsonify(low_stock)

# Replenishment automation: Automatically place order for low stock
class ReplenishmentAutomation(Resource):
    def get(self):
        low_stock_orders = []
        for product_name, product in products.items():
            if product.stock_level < 10:  # Threshold for low stock
                low_stock_orders.append({
                    'product': product_name,
                    'needed_quantity': 100 - product.stock_level  # Example: order enough to replenish to 100
                })
        return jsonify(low_stock_orders)

# Batch tracking endpoint: View batch info (FIFO)
class BatchTracking(Resource):
    def get(self):
        batch_info = {}
        for product_name, product in products.items():
            batch_info[product_name] = [{
                'batch_number': batch['batch_number'],
                'quantity': batch['quantity'],
                'expiry_date': batch['expiry_date'].strftime('%Y-%m-%d')
            } for batch in product.batch_data]
        return jsonify(batch_info)

# Shelf-life management: Ensure no expired products are sold
class ExpiryManagement(Resource):
    def get(self):
        expired_products = {}
        for product_name, product in products.items():
            expired_batches = product.check_expiry()
            if expired_batches:
                expired_products[product_name] = [{
                    'batch_number': batch['batch_number'],
                    'expiry_date': batch['expiry_date'].strftime('%Y-%m-%d')
                } for batch in expired_batches]
        return jsonify(expired_products)

# Stock audit: Perform periodic stock audit and reconcile with system
class StockAudit(Resource):
    def get(self):
        audit_report = {}
        for product_name, product in products.items():
            audit_report[product_name] = {
                'stock_level': product.stock_level,
                'sold': product.sales
            }
        return jsonify(audit_report)

api.add_resource(STKPush, '/stkpush')
api.add_resource(StockTracking, '/stocktracking')
api.add_resource(LowStockAlert, '/lowstock')
api.add_resource(ReplenishmentAutomation, '/replenishment')
api.add_resource(BatchTracking, '/batchtracking')
api.add_resource(ExpiryManagement, '/expiry')
api.add_resource(StockAudit, '/stockaudit')

if __name__ == '__main__':
    app.run(debug=True)

