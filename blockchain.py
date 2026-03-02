from block import Block


class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.difficulty = 4

        self.create_genesis_block()

    def create_genesis_block(self):
        """
        Create the first block in the blockchain.
        """
        genesis_block = Block(0, [], "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        """
        Add transaction to pending transactions.
        """
        self.pending_transactions.append(transaction.to_dict())

    def mine_pending_transactions(self, miner_address):
        """
        Mine pending transactions and reward the miner.
        """
        block = Block(
            len(self.chain),
            self.pending_transactions,
            self.get_last_block().hash
        )

        block.mine(self.difficulty)
        self.chain.append(block)

        # Reward transaction
        self.pending_transactions = [{
            "sender": "NETWORK",
            "recipient": miner_address,
            "amount": 1
        }]

    def is_chain_valid(self):
        """
        Validate blockchain integrity.
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.compute_hash():
                return False

            if current.previous_hash != previous.hash:
                return False

        return True
