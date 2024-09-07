class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_dict(self):
        return {"sender": self.sender, "recipient": self.recipient, "amount": self.amount}

    def sign_transaction(self, private_key):
        transaction_data = f"{self.sender}{self.recipient}{self.amount}".encode()
        self.signature = private_key.sign(transaction_data)

    def verify_transaction(self, public_key):
        transaction_data = f"{self.sender}{self.recipient}{self.amount}".encode()
        try:
            public_key.verify(self.signature, transaction_data)
            return True
        except:
            return False
    def displayblocks():
        print(f'block is blocked due to the error of the macine learing anf 
        
        
        try:
            static:
            if thr gillwnj