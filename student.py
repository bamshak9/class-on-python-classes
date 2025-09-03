class Student:
    school_fees=100_000
    def __init__(self, firstname, lastname):
        self.firstname=firstname
        self.lastname=lastname
        self.fullname=firstname +" "+ lastname
        self.score=[]
    def add_score(self):
        running =True
        while running:
            add_score=int(input("What score do you want to add(Enter 1000 to close)?"))
            if add_score==1000:
                running=False
            else:
                self.score.append(add_score)
    def total_score(self):
        return sum(self.score)
    def lowest_score(self):
        lowest_score=10**10
        for i in self.score:
            if i<lowest_score:
                lowest_score=i
            else:
                continue
        return lowest_score
    def highest_score(self):
        highest_score=0
        for i in self.score:
            if i>highest_score:
                highest_score=i
            else:
                continue
        return highest_score
Jerry= Student("Jerry", "Biggs")
print(Jerry.firstname)
print(Jerry.fullname)
print(Jerry.score)
Jerry.add_score()
print(Jerry.highest_score())
print(Jerry.lowest_score())
print(Jerry.total_score())
print(Jerry.score)