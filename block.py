import time
import hashlib
import json


class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        """
        Compute SHA-256 hash of the block contents.
        """
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)

        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine(self, difficulty):
        """
        Perform Proof-of-Work mining.
        """
        prefix = '0' * difficulty

        while not self.hash.startswith(prefix):
            self.nonce += 1
            self.hash = self.compute_hash()

        return self.hash
