#re-learning about class and objects.

class MyClass: #ini class, class adalah blueprint dari object

    var = "blah" #variable ini adalah object didalan class

    def function(self): #ini adalah fungsi didalam class
        print("This is a message inside the class.")

myobjectx = MyClass() #myobjectx adalah variable, yang menyimpan object dari class MyClass() yang isinya berupa var(object) dan function.

myobjectx.var #mengakses var

print(myobjectx.var)
print("####\n")
###################
## 2 object menggunakan class yang sama

myobjecty = MyClass()
myobjectz = MyClass()

myobjectz.var = "zlah" #mendefinisikan var

print(myobjectx.var) #hasilnya tetap blah
print(myobjectz.var) #hasilnya akan menjadi zlah, karena habis di redefinisi

print("####\n")
###################
## mengakses fungsi

myobjectx.function()
print("####\n")


###################
## exercise

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc

car1 = Vehicle()
car1.name = "Fer"
car1.kind = "Convertible"
car1.color = "Red"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.kind = "Van"
car2.color = "Blue"
car2.value = 10000

print(car1.description())
print(car2.description())