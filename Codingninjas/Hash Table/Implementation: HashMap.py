class myHashMap :

    def __init__(self) :
        self.dct = {}

    def get(self, key) :
        if key in self.dct:
            return self.dct[key]
        return -1
    
    def insert(self, key, value) :
        self.dct[key] = value

    def remove(self, key) :
        if key in self.dct:
            self.dct.pop(key)        
                
    def search(self, key) :
        if key in self.dct:
            return True
        return False

    def getSize(self) :
        return len(self.dct)    
    
    def isEmpty(self) :
        return len(self.dct) == 0
        
# main
myMap = myHashMap()

n = int(input().strip())

for i in range(n) :

    li = input().strip().split(" ")
    typ = int(li[0])
 
    if (typ == 1):
        key = li[1]
        value = int(li[2])
        myMap.insert(key, value)
        
    elif (typ == 2):
        key = li[1]
        myMap.remove(key)
        
    elif (typ == 3):
        key = li[1]
        if (myMap.search(key)):
            print('true')
        else :
            print('false')
              
    elif (typ == 4):
        key = li[1]
        print(myMap.get(key))
    
    elif (typ == 5):
        print(myMap.getSize())
    
    else :
        if(myMap.isEmpty()) :
            print("true")
        else :
            print("false")
    