class Interface(): 

    def __init__(self, menuList, default_menu, init_func = None):
        self.__menuList = menuList
        self.__activeMenu = default_menu

    def setActiveMenu(self,menu):
        self.__activeMenu = menu
        
    def run(self):
        while True:

            func = self.__activeMenu.chooseOption()
            func(self)

class Menu():
    def __init__(self, optionList = None):
        self.optionList = optionList

    def makeSetterOption(self,keys,label):
        return Option(keys,lambda i: i.setActiveMenu(self),label)

    def printLabels(self):
        for label in self.optionList.getLabels():
            print(label)

    def chooseOption(self): 
        val = self.optionList.getOptionVal(input("Choose an Option: "))
        while val == None: 
            print("invalid option")
            val = self.optionList.getOptionVal(input("Choose an Option: "))
        return val


class OptionList(list):

    def getLabels(self):
        labels = []
        for option in self:
            labels.append(option.label)
        return labels

    def getOptionVal(self,key):
        for option in self:
            if key in option.keys:
                return option.value
        return None

class Option():
    def __init__(self,keys,value,label):
        self.keys = set(keys)
        self.value = value
        self.label = label 

