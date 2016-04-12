def getBool(prompt):
    try:
        return {'y':True,'n':False}[input(prompt + 'Y/N: ').lower()]
    except: 
        print ('not a Y/N response!')
        return getBool(prompt)
def getTemp():
    try:
        return int(input('current Temprature in *F?: '))
    except:
        print ('not a valid remprature')
        return getTemp()

def squirrel():
    temprature = getTemp()
    summer = getBool('Is it summer?')
    if summer == True :
        if 60 <= temprature <= 100 :
            return True
        else:
            return False
    else:
        if 60 <= temprature <= 90 :
            return True
        else:
            return False 
def display():
    if squirrel() == True :
        print ('Squirrels are active today')
    else:
        print ('Squirrels are not active today')
print(display())