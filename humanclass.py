class Human:
    def __init__(self,profession):
        self.profession = profession
    def set_profession(self,new_profession):
        self.profession = new_profession
#man = Human()
#man.set_profession("Manager")
#print (man.profession)

# assign attribute runtime

man = Human("Lead")
print (man.profession)

