def muliply(a,b):
       print(a*b)
muliply(5,6)

def MyDecor(function):
       def IwillDecor(x,p):
              print("I'm decorating the "+str(function))
              function(x,p)
       return IwillDecor
Newfunc=MyDecor(muliply)
Newfunc(3,6)

