#from wallet.wallet_key import generate_keys
#from transaction.transaction_logic import Transaction
from blockchain.blockchain_class import Block,Blockchain
import datetime as date


from blockchain.chat_block_link import block,Blockchain
 
from blockchain.new_blockchain_class import block,Blockchain

# x,y = generate_keys()

# print (x)
# print(y)

def block(self,transaction,date,previous_hash,hash):



# blockchain = Blockchain()


# blockchain.add_block(block(1, date.datetime.now(),"Transaction Data 1",""))
# blockchain.add_block(block(2, date.datetime.now(),"Transaction Data 2",""))
# blockchain.add_block(block(3, date.datetime.now(),"Transaction Data 3",""))
# blockchain.add_block(block(4, date.datetime.now(),"Transaction Data 3",""))
# blockchain.add_block(block(5, date.datetime.now(),"Transaction Data 3",""))


# for block in block.chain:
#     print("Block #"+str(block.index))
#     print("Timestamp:"+str(block.Timestamp))
#     print("Data: "+block.data)
#     print("Hash: "+block.hash)
#     print("Previous Hash: "+block.previous_hash)
#     print("\n")





blockchain = Blockchain()
blockchain.add_block(block(1, date.datetime.now(), "Block 1 Data", blockchain.get_latest_block().hash))
blockchain.add_block(block(2, date.datetime.now(), "Block 2 Data", blockchain.get_latest_block().hash))


for block in blockchain.chain:
    print("\n\n\n")
    print("Block #" + str(block.index))
    print("Timestamp: " + str(block.timestamp))
    print("Data: " + block.data)
    print("Hash: " + block.hash)
    print("Previous Hash: " + block.previous_hash)
    print("\n")

