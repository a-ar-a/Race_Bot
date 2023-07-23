class User:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(self.__str__())
user1 = User('Petr')
val_x = 1
user1.val_x = val_x
user1.display_info()
print(user1.val_x)
