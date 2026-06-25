# C__len__ metho call when we call len(obj) function 

class Team:
    def __len__(self):
        return 5

obj = Team()

print(len(obj))