# Deploying to Render (recommended)

1. Push the project to GitHub.
2. Sign in to https://render.com and create a new **Web Service**.
3. Connect your GitHub repo and choose the branch.
4. Build Command:
   ```
   pip install -r requirements.txt
   ```
5. Start Command:
   ```
   gunicorn app:app
   ```
6. Under Environment, add the following env vars (from your Braintree sandbox):
   - BRAINTREE_MERCHANT_ID
   - BRAINTREE_PUBLIC_KEY
   - BRAINTREE_PRIVATE_KEY
7. Deploy and copy the public URL. That's your demo link to share.
