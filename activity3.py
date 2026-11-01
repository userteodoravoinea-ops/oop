class Parrot:
    species="bird"
    def __init__(self, name, age):
        self.name=name
        self.age=age
coco=Parrot("coco",14)
bluey=Parrot("bluey",10)
print(coco.name,coco.age)
print(bluey.name, bluey.age)