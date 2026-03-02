import hashlib
import secrets


class Wallet:
    def __init__(self):
        """
        Generate simple pseudo wallet.
        """
        self.private_key = secrets.token_hex(32)
        self.public_key = hashlib.sha256(self.private_key.encode()).hexdigest()

    def get_address(self):
        """
        Return public wallet address.
        """
        return self.public_key
