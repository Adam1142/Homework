class animal:
    speices = "dog"
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

Jack = animal("Jack", "bull dog")
Bingo = animal("Bingo", "golden shepherd")

print("Jack is a {}".format(Jack.speices))
print("Bingo is a {}".format(Bingo.speices))

print("{} is a {}".format(Jack.name,Jack.breed))
print("{} is a {}".format(Bingo.name,Bingo.breed))