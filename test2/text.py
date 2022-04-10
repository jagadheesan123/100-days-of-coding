#polimorfisum
class  myclass:
    def fun(self,a,b,c):
        if a!=None and b!=None and c!=None:
            return (a+b+c)
        elif a!=None and b!=None:
            return (a+b)
        else:
            return(a)
obj=myclass()
print(obj.fun(20,4,12))

        