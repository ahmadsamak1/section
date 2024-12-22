class  person :
    unoverstoe="mnu"
    def __init__ (self, age,name):
        self.age =age
        self.name= name
        
p1=person(18,"samak")   
print (p1 .age)
print(p1 .name )   
print(person.unoverstoe)







class person:
    def greet(self):
        print ("hallo my class 1") 
        
        
        
class child(person):        
    def  greet(self):
        super().greet()
        print ("hallo my class 2")   
c =person()    
c1=child()
c1.greet()
c.greet()














def sum(a,d):
    sum1=a+d
    print(sum1)

def sum(a,d,h):
    sum1=a+d+h
    print(sum1)

sum(3,5,7)





def add(datatype,*arg):
    if datatype=="int":
        answer=0
    if datatype=="str":
        answer=" "
    for i in arg:
        answer = answer + i    
    print(answer)

add("int",5,4)        
add("str","ahmed","samak")        




from  abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod 
    def aree (self):
        pass
    
    
    @abstractmethod 
    def premier (self):
        pass
    
class cercal(shape):
    def __init__ (self, r):
        self.r =r
        
    
    def aree(self): 
        return (f'aree;{3.14*self.r*self.r};')
    def premier (self):
        return (f'premier;{2*3.14*self.r};')
c=cercal(5)
print(c.aree())
print(c.premier())





















