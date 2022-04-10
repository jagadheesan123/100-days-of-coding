
from unicodedata import name


def myfun(name):
    print('welcome'+ name)
myfun(' rajesh' )
def myvalue(x):
    return x+5
a=myvalue(5)
print(a)
def myroule(condition):
   print ('submit the mobile'+ condition)
b=myroule(' jagadheesh')
print(b)

def mycompation(sports):
    print(sports + ' sport')  
mycompation('volly ball')
mycompation('foot ball')
mycompation('cricket')
def  mycal(x):
    return x *x
c=(mycal(5))
print(c)
def mycalculation(list):
    return list*5
w=mycalculation([2,4,6,8,10])
print(w)
data=lambda num:num%2==0
z=data(22)
print(z)
if z==True:
    print('the number is even')
else:
    print('ythe number is odd')
x=lambda a,b:a*b
f=x(8,9)
print(f)
def myplay(value):
    return value*5
total=myplay(2)
print(total)
def value1(n):
    return n-10
n=(20,30,40,50)
result=map(value1,n)
print(list(result))
def mylist(n):
    return n*5
n=(94,6,9,2,70)
sum=map(mylist,n)
print(list(sum))

class Person:
    def __init__(self,  name,age,qulification):
        self.name=name
        self.age=age
        self.qulification=qulification
p1= Person ('jaga',23,'chemistry')
print(p1.name)
print(p1.age)
print(p1.qulification)

#class value():

def collection(name):   
    print('welcome'+ name)
    a=int(10)
    
obj=collection('jaga')
def add(a,b):
    return (a+b)
if __name__=='__main__':
    print(add(2,3))
    print(add(3,46))
    print(__name__)
class parent:
    def parent(self):
        print('hello world')
        print('there is a plane')
class child(parent):
    def child(self):
        print('you can catch the plane' )
class gson(child):
    def gson(self):
        print('lift your bag in plane')
if __name__=='__main__':
    app=gson()
    app.parent()
    app.child()
    app.gson()

    
        
    

    


 