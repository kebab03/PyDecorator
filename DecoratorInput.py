def InpDEco(myInval):
       def MakeupMan(fun):
              print('Befor making Up')
              def IWillMake(*args,**Kwargs):
                     print("decor input:",myInval)
                     deorated=fun(*args,**Kwargs)
                     print("Make up man say's : I'm done with make up")
                     return deorated
              return IWillMake
       return MakeupMan
§
@InpDEco(9)   
def WedingGirl():
       print(" I want to Get Make up")
WedingGirl()
@app.root()
