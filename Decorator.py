def MakeupMan(fun):
       print('Befor making Up')
       def IWillMake():    
              fun()
              print("Make up man say's : I'm done with make up")
       return IWillMake
@MakeupMan ##  WedingGirl = MakeupMan(WedingGirl)
def WedingGirl():
       print(" I want to Get Make up")


##WedingGirl = MakeupMan(WedingGirl)
WedingGirl()
##IWillMake()
