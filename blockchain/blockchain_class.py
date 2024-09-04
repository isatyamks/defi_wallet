import hashlib
import time

class Block:
    def __init__(self, previous_hash, transactions):
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_content = f"{self.timestamp}{self.transactions}{self.previous_hash}"
        return hashlib.sha256(block_content.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        previous_hash = self.get_latest_block().hash
        new_block = Block(previous_hash, transactions)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True
