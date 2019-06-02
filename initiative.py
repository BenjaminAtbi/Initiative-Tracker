import sys
import json
from enum import Enum


class Tracker(): 

    def __init__(self):
        try:
            datafile = open("data.json","r") 
            self.data = datafile.read()
        except:
            print("data not loaded")
            self.data = Data()
        finally:
            datafile.close()
        
        self.party = None
        if (self.party == None):
            self.state = self.selectParty
        else:
            self.state = self.main
    
    def run(self):
        while True:
            self.state()

    def main(self): 
        consolePrint(["Current Party: "+self.party,"Options:","1 - Roll Initiative (R)","2 - Edit Party (E)","3 - Change Party (C)", ""])

optionlist = {
    
}

def consolePrint(strings):
    print("|------Initiative Tracker------|")
    for string in range(strings):
        print(string)

class Data():
    def __init__(self):
        self.parties = []