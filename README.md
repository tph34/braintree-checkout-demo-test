# Braintree One-Time Checkout Demo

This is a full-stack demo web app showcasing a one-time checkout flow using Braintree's SDK (Drop-in UI).

## What you get
- Flask backend that generates client tokens and creates transactions
- Single-page frontend using Braintree Drop-in UI
- Ready-to-run project you can push to GitHub and deploy (Render, Railway, Heroku)
- `.env.example` for credentials

## Files
- `app.py` - Flask server
- `templates/index.html` - Frontend with Drop-in UI
- `static/style.css` - Simple styling
- `requirements.txt` - Python deps
- `Procfile` - For deployment (gunicorn)
- `.env.example` - example env vars
- `README-deploy.md` - deployment steps for Render

## Run locally
1. Create a Python 3.10+ virtualenv and activate it.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in your Braintree sandbox credentials:
   ```
   BRAINTREE_MERCHANT_ID=your_merchant_id
   BRAINTREE_PUBLIC_KEY=your_public_key
   BRAINTREE_PRIVATE_KEY=your_private_key
   FLASK_ENV=development
   ```
4. Run:
   ```bash
   flask run
   ```
   or
   ```bash
   gunicorn app:app
   ```
5. Open `http://127.0.0.1:5000`

## Sandbox test cards
- Success: `4111 1111 1111 1111`
- Failure: See the transaction amount here: https://developer.paypal.com/braintree/docs/reference/general/testing/python#transaction-amounts
  
Use any future expiry and any cvv.

## How I prepared this
I generated a complete repo archive with working Flask + Braintree Drop-in UI. To publish:
1. Create a new GitHub repo.
2. Unzip this archive and push to your repo.
3. Deploy to Render (instructions in README-deploy.md) and add env vars in the service settings.
# braintree-checkout-demo
