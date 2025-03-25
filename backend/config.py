# config.py

class Config:
    # M-Pesa API Credentials (replace with your actual credentials)
    CONSUMER_KEY = 'LIhme2t9PEBqvyQsvy8PA56WIMtGDIS2ekMs5KkxoGkGdDg6'  # Replace with your M-Pesa Consumer Key
    CONSUMER_SECRET = 'VlvaSERcMQLyFg9v1IP4AYo7dR2JZeOGlwxJogeHhFTsE8nTulfKjM2RckWnnQPd'  # Replace with your M-Pesa Consumer Secret

    # M-Pesa Shortcode and other details (replace with your actual details)
    BUSINESS_SHORTCODE = 'YOUR_BUSINESS_SHORTCODE'  # Replace with your Business Shortcode
    BUSINESS_SHORTCODE_PASSWORD = 'YOUR_BUSINESS_SHORTCODE_PASSWORD'  # Replace with your Shortcode Password
    LIPA_NA_MPESA_SHORTCODE = 'YOUR_LIPA_NA_MPESA_SHORTCODE'  # Replace with your Lipa Na M-Pesa Shortcode
    LIPA_NA_MPESA_SHORTCODE_PASSWORD = 'YOUR_LIPA_NA_MPESA_SHORTCODE_PASSWORD'  # Replace with your Shortcode Password for Lipa Na M-Pesa

    # M-Pesa STK Push URL (sandbox URL for testing)
    LIPA_NA_MPESA_URL = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'  # Use the sandbox URL for testing
    OAUTH_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'  # OAuth endpoint

