import hashlib
class Block:
    base_hash = {}
    hash = hashlib.sha256("a".encode()).hexdigest()
    parent_hash = {}
    transactions = {}
    blocks = {}
    last_transaction_number = {}
    #def taille():
        
    #def nom():

   # def parent():

   # def listeDesTransactions():

   # def check_hash():

   # def add_transaction():

   # def get_transaction():

   # def get_weight():

   # def save(hash):

   # def load(hash):

    def generate_hash(self, previous_block_hash, transaction_list):
        a = input("Entrer du texte : ")
        b = input("Entrer du texte : ")
        self.a = previous_block_hash
        self.b = transaction_list

        self.block_data = "-".join(b) + "-" + a
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        
        
        print(self.block_hash)
        
  #  def verify_hash():

  #  def add_block():

 #   def get_block():

   # def add_transaction():

