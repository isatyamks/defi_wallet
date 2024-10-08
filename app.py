from flask import Flask, jsonify, request, render_template


from wallet.wallet_key import generate_keys
from transaction.transaction_logic import Transaction
from blockchain.blockchain_class import Block,Blockchain

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')  

@app.route('/create_wallet', methods=['GET'])


def create_wallet():
    private_key, public_key = generate_keys()
    
    
    
    
    
    return jsonify({
        'private_key': private_key.decode(),
        'public_key': public_key.decode()
    })

@app.route('/new_transaction', methods=['POST'])
def new_transaction():
    values = request.get_json()

   
   
   
   
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    transaction = Transaction(values['sender'], values['recipient'], values['amount'])
    Blockchain.add_block([transaction.to_dict()])

    return 'Transaction added', 201

if __name__ == '__main__':
    app.run(debug=True)
