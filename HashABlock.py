from datetime import datetime
from hashlib import sha256

class Block:
  def __init__(self, transactions, previous_hash, nonce = 0):
    self.timestamp = datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = nonce
    self.hash = self.generate_hash()
    
  def print_block(self):
    # prints block contents
    print("timestamp:", self.timestamp)
    print("transactions:", self.transactions)
    print("current hash:", self.generate_hash())
    
  def generate_hash(self):
    # hash the blocks contents
    block_contents = str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
    block_hash = sha256(block_contents.encode())
    return block_hash.hexdigest()

'''
Key terms
Chain: A list that that holds all the blocks inside the blockchain.
Unverified Transactions: A list that represents all the unverified transactions before being passed into a block.
Genesis Block: A block automatically generated when the blockchain is initialized.
'''