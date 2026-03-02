import json


class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_dict(self):
        """
        Convert transaction object to dictionary.
        """
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount
        }

    def __repr__(self):
        return json.dumps(self.to_dict())
