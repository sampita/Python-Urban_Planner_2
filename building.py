import datetime

class Building:
    def __init__(self, address, stories):
        self.designer = "Sam Pita"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories
        
    def construct(self):
        self.date_constructed = datetime.datetime.now()
        # print("date_constructed", self.date_constructed)
        
    def purchase(self, purchaser):
        self.owner = f'{purchaser}'
        # print("purchaser", self.owner)

    def print_statement(self, address, owner, date_constructed, stories):
        print(f'{self.address} was purchased by {self.owner} on {self.date_constructed} and has {self.stories} stories.')