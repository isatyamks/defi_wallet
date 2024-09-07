#from wallet.wallet_key import generate_keys
#from transaction.transaction_logic import Transaction
#from blockchain.blockchain_class import Block,Blockchain
import datetime as date




from blockchain.new_blockchain_class import block,Blockchain

# x,y = generate_keys()

# print (x)
# print(y)




blockchain = Blockchain()


blockchain.add_block(block(1, date.datetime.now(),"Transaction Data 1",""))
blockchain.add_block(block(2, date.datetime.now(),"Transaction Data 2",""))
blockchain.add_block(block(3, date.datetime.now(),"Transaction Data 3",""))


for block in block.chain:
    print("Block #"+str(block.index))
    print("Timestamp:"+str(block.Timestamp))
    print("Data: "+block.data)
    print("Hash: "+block.hash)
    print("Previous Hash: "+block.previous_hash)
    print("\n")


