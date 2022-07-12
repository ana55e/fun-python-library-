def str2int(a):
    l=0
    for i in a:
        l+=ord(i)
    return l

def compare(a,b):
    if( str2int(a) < str2int(b)):
        print("le plus grand est:",a)
    elif( str2int(b) < str2int(a)):
        print("le plus grand est:",b)
    else:
        print("egaux")




def Upper(a):
    p=str2int(a)
    p=p-32
    return chr(p)

def lower(a):
    p=str2int(a)
    p=p+32
    return chr(p)







class superstr:
    def __init__(self,x):
        p=0
        for i in x:
            p+=ord(i)
        self.numbre=p
        self.value=chr(p)
    def superstrer(self):
        return self.value
    def supersommeur(self):
        q=0
        n=input("donner str ou int avec qui sommer , si non entrer 0 : ")
        if(n=='0'):
            return -1
        else:
           for i in str(n):
               q=q+ord(i)
        k=q+self.numbre
        return chr(k)
    def superminus(self):
        q=0
        n=input("donner str ou int avec qui minuse , si non entrer 0 : ")
        if(n=='0'):
            return -1
        else:
           for i in str(n):
               q=q+ord(i)
        k=q-self.numbre
        return chr(k)

    def supermultiplier(self):
        q=0
        n=input("donner str ou int avec qui multiplier , si non entrer 0 : ")
        if(n=='0'):
            return -1
        else:
           for i in str(n):
               q=q+ord(i)
        k=q*self.numbre
        return chr(k)

    def superdivider(self):
        q=0
        n=input("donner str ou int avec qui multiplier , si non entrer 0 : ")
        if(n=='0'):
            return -1
        else:
           for i in str(n):
               q=q+ord(i)
        k=q//self.numbre
        return chr(k)


    def mathifier(self):
        import math as m
        n=input("donner le nom de la fct voulue")
        if(str2int(n)==422):
            return chr(m.acos(self.numbre))
        if(str2int(n)==470):
            return chr(int(m.atan2(self.numbre)))
        if(str2int(n)==330):
            return chr(int(m.sin(self.numbre)))
        if(str2int(n)==526):
            return chr(int(m.acosh(self.numbre)))
        if(str2int(n)==524):
            return chr(int(m.atanh(self.numbre)))
        if(str2int(n)==434):
            return chr(int(m.sinh(self.numbre)))
        if(str2int(n)==427 and n[0]=='a'):
            return chr(int(m.asin(self.numbre)))
        if(str2int(n)==325):
            return chr(int(m.cos(self.numbre)))
        if(str2int(n)==458):
            return chr(int(m.sqrt(self.numbre)))
        if(str2int(n)==470):
            return chr(int(m.atan2(self.numbre)))
        if(str2int(n)==333):
            return chr(int(m.exp(self.numbre)))
        if(str2int(n)==531):
            return chr(int(m.asinh(self.numbre)))
        if(str2int(n)==323):
            return chr(int(m.tan(self.numbre)))
        if(str2int(n)==420):
            return chr(int(m.atan(self.numbre)))
        if(str2int(n)==429):
            return chr(int(m.cosh(self.numbre)))
        if(str2int(n)==427 and n[0]=='t'):
            return chr(int(m.tanh(self.numbre)))
        if(str2int(n)==949):
            return chr(int(m.factorial(self.numbre)))
        if(str2int(n)==322):
            return chr(int(m.log(self.numbre)))
        if(str2int(n)==515):
            return chr(int(m.gamma(self.numbre)))









#try it use for example d=superstr('string that you want')
#try it functions for example d.supersommeur()







