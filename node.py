from blockchain import Blockchain
from transaction import Transaction
from wallet import Wallet


def main():
    blockchain = Blockchain()

    wallet1 = Wallet()
    wallet2 = Wallet()

    tx1 = Transaction(wallet1.get_address(), wallet2.get_address(), 10)

    blockchain.add_transaction(tx1)
    blockchain.mine_pending_transactions(wallet1.get_address())

    print("Blockchain valid:", blockchain.is_chain_valid())

    for block in blockchain.chain:
        print(vars(block))


if __name__ == "__main__":
    main()
