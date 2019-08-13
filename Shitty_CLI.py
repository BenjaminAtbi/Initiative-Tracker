

class Interface(): 

    def __init__(self, menuList, default_menu, init_func = None):
        self.__menuList = menuList
        self.__activeMenu = default_menu
        self.renderer = renderer

    def setActiveMenu(self,menu):
        self.__activeMenu = menu

    def chooseOption(self):
    self.printLables(self.__activeMenu.getLabels())
    val = self.__activeMenu.optionList.getOptionVal(input("Choose an Option: "))
    while val == None: 
        print("invalid option")
        val = self.__activeMenu.optionList.getOptionVal(input("Choose an Option: "))
    return val

    def printLables(self, labels)
    for i, label in enumerate(labels, 1)
        print(i + ") " + label)

    def run(self):
    while True:
#           self.renderer.printlables(self.__activeMenu.getLabels())
        func = self.__activeMenu.chooseOption()
        func(self)

class Menu():
    def __init__(self, optionList = None):
        self.optionList = optionList

    def addOption(option):
        self.optionList.append(option)

    def getLabels(self):
    labels = []
    for option in optionList:
        labels.append(option.label)
    return labels

    def getOptionVal(self,key):
    for i, option in enumerate(optionList, 1):
        if key in option.keys or key == i:
            return option.value
    return None

    # returns function that sets this menu as active menu when called as option value
    # useful when defining options that swap between menus
    def makeSetterFunc(self,):
        return lambda i: i.setActiveMenu(self)

# keys: collection of strings representing commandline inputs corresponding to option
# value: function to be run when option chosen
class Option():
    def __init__(self,keys,value,label):
        self.keys = set(keys)
        self.value = value
        self.label = label 
