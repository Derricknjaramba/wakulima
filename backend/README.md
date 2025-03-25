# Milk Shop Backend API

This Flask-based backend API manages a retail milk shop's inventory and integrates with M-Pesa for payment processing. The system includes features like stock tracking, replenishment automation, batch tracking, shelf-life management, and stock audits.

## Features

- **Stock Tracking**: Monitors inventory levels in real-time.
- **Low Stock Alerts**: Notifies when stock falls below a defined threshold.
- **Replenishment Automation**: Automatically triggers orders for low stock.
- **Batch Tracking (FIFO)**: Manages batches of perishable items, ensuring FIFO is followed.
- **Shelf-life Management**: Ensures perishable products are sold before expiration.
- **Stock Audits**: Facilitates periodic stock checks to reconcile physical inventory with system data.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/milk_shop_backend.git
    cd milk_shop_backend
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up M-Pesa credentials in `config.py` by replacing the placeholders with your actual API keys and secrets.

4. Run the Flask app:
    ```bash
    python app.py
    ```

5. Use Postman or similar tools to test the API endpoints.

## Endpoints

- **POST /stkpush**: Initiates an STK Push payment.
- **GET /stocktracking**: Retrieves real-time stock levels.
- **GET /lowstock**: Alerts when stock is low.
- **GET /replenishment**: Retrieves automatic replenishment recommendations.
- **GET /batchtracking**: Views batch info with FIFO management.
- **GET /expiry**: Manages perishable product expiry.
- **GET /stockaudit**: Conducts a stock audit and reconciliation.

## License

MIT License
