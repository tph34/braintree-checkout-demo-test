import os
from flask import Flask, render_template, request, jsonify, send_from_directory
from dotenv import load_dotenv
import braintree
from flask_cors import CORS

load_dotenv()
app = Flask(__name__)
CORS(app)

#merchant_id = os.getenv("BRAINTREE_MERCHANT_ID")
#print(merchant_id)

# Braintree configuration
gateway = braintree.BraintreeGateway(
    braintree.Configuration(
        braintree.Environment.Sandbox,
        merchant_id=os.getenv('BRAINTREE_MERCHANT_ID'),
        public_key=os.getenv('BRAINTREE_PUBLIC_KEY'),
        private_key=os.getenv('BRAINTREE_PRIVATE_KEY')
    )
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/token', methods=['GET'])
def token():
    try:
        client_token = gateway.client_token.generate()
        return jsonify({'token': client_token})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/checkout', methods=['POST'])
def checkout():
    data = request.get_json(force=True)
    nonce = data.get('payment_method_nonce')
    amount = data.get('amount')

    if not nonce or not amount:
        return jsonify({'success': False, 'error': 'Missing nonce or amount'}), 400

    try:
        result = gateway.transaction.sale({
            'amount': str(amount),
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            return jsonify({'success': True, 'transaction_id': result.transaction.id})
        else:
            # collect errors/messages
            message = getattr(result, 'message', None)
            errors = []
            if result.errors:
                for e in result.errors.deep_errors:
                    errors.append(e.message)
            return jsonify({'success': False, 'error': message, 'errors': errors}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=(os.environ.get('FLASK_ENV')=='development'))
