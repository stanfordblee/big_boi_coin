import hashlib
import datetime

class BigBoiBlock:
    def __init__(self, index, proof_number, previous_hash, data, timestamp=None):
        """
        Args:
            index — this keeps track of the position of the block within the blockchain;
            proof_no — this is the number produced during the creation of a new block (called mining);
            prev_hash — this refers to the hash of the previous block within the chain;
            data—this gives a record of all transactions completed, such as the quantity bought;
            timestamp — this places a timestamp for the transactions.
        """
        self.index = index
        self.proof_number = proof_number
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or datetime.now()

    @property
    def calculate_hash(self):
        block_of_string = f"{self.index}{self.proof_number}{self.previous_hash}{self.data}{self.timestamp}"
        return hashlib.sha256(block_of_string.encode()).hexdigest()

class BigBoiBlockChain: 
    def __init__(self):
        """
        chain — this variable keeps all blocks;
        current_data — this variable keeps all the completed transactions in the block;
        construct_genesis() — this method will take care of constructing the initial block.
        """
        self.chain = []
        self.current_data = []
        self.ndoes = set()
        self.construct_genesis()

    def construct_genesis(self):
        self.construct_block(proof_no=0, prev_hash=0)

    def construct_block(self, proof_no, prev_hash):
        block = BigBoiBlock(
            index=len(self.chain),
            proof_no=proof_no,
            prev_hash=prev_hash,
            data=self.current_data)
        self.current_data = []
        self.chain.append(block)
        return block

    def is_legit(self, block, prev_block):
        if prev_block.index + 1 != block.index:
            return False
        elif prev_block.calculate_hash != block.prev_hash:
            return False
        elif not BigBoiBlockCHain.verifying_proof(block.proof_no, prev_block.proof_no):
            return False
        elif block.timestamp <= prev_block.timestamp:
            return False
        return True

    def new_data(self, sender, recipient, quantity):
        self.current_data.append({
            'sender': sender,
            'recipient': recipient,
            'quantity': quantity
        })
        return True

    @staticmethod
    def proof_of_work(last_proof):
        """
        Proof of work -> Prevents blockchain from abuse.
        Its objective is to identify a number that solves a problem after
        a certain amount of computing work is done. 
        If difficulty levl of identifying number is high - it discourages
        spamming and tampering with blockchain.
        """
        proof_no = 0
        while BigBoiBlockChain.verifying_proof(proof_no, last_proof) is False:
            proof_no += 1

    @staticmethod
    def verifying_proof(last_proof, proof):
        # Verifying the proof does hash(last_proof, proof) contains 4 leading zeroes
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property
    def last_block(self):
        return self.chain[-1]    

if __name__=="__main__":
    """
    Goal: Send Wamford a BigBoiCoin.
    Q: What's in his wallet?
    Q: How does he determine his wallet? 
    -> Do we code our own electronic wallet?
    """
    print("Welcome to BigBoiCoin.") 
