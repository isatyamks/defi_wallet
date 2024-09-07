import datetime as date
import hashlib


class block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Include data in the hash calculation
        hash_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(hash_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # Genesis block is usually index 0
        return block(0, date.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Validate the hash of the current block
            if current_block.hash != current_block.calculate_hash():
                return False

            # Validate the hash of the previous block
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


# Example of how to use the Blockchain class
blockchain = Blockchain()
blockchain.add_block(block(1, date.datetime.now(), "Block 1 Data", blockchain.get_latest_block().hash))
blockchain.add_block(block(2, date.datetime.now(), "Block 2 Data", blockchain.get_latest_block().hash))


# Iterating over the blockchain and printing details of each block
for block in blockchain.chain:
    print("Block #" + str(block.index))
    print("Timestamp: " + str(block.timestamp))
    print("Data: " + block.data)
    print("Hash: " + block.hash)
    print("Previous Hash: " + block.previous_hash)
    print("\n")
