#!/usr/bin/python
#  main.py
# ===================================================================
# Wed Jun 19 15:54:45 CEST 2019

import readline
import json
from aw_log import logger

try:
    input = raw_input
except NameError:
    pass

class unit(object):
    def __init__(self, name='Brenner', classe='Gunlugger'):
        self.name=name
        self.classe=classe
        self.active=True
        return
    def found(self, s):
        return (self.active and (s.lower() in self.name.lower()))
    def display(self):
        if self.active: return self.name+" "+self.classe

class character(unit):
    def __init__(self, n, c, hard=0, sharp=0, hot=0, cool=0, weird=0, sk=''):
        unit.__init__(self, n,c)
        self.level = 1
        self.hp = 10
        self.countdown = {}
        self.stats = [hard, sharp, hot, cool, weird] # str(hard)0, int(sharp)1, chm(hot)2, dex(cool)3, psi(weird)4
        self.skill = sk
        return
    def display(self):
        r = unit.display(self)
        r+= '['+str(self.level)+']['+str(self.hp)+']'
        r+= 'stats:'+','.join(str(self.stats[i]) for i in range(len(self.stats)))
        r+= 'skill:'+self.skill
        return r

class player():
    def __init__(self):
        self.characters = []
        self.countdowns = {}
        return
    def starterPack(self, awcls):
        chList=[]
        for c in awcls:
            chList.append(c)
        for i, k in enumerate(chList):
            self.characters.append(character('name='+str(i), k, awcls[k]['stat'][0],awcls[k]['stat'][1],0,0,0))
        return

def listing(ul):
    for i in ul:
        print(i.display())
    return

def main():
    try:
        with open('AW-db/aw_classes.json') as f:
            awcl=json.load(f)
    except IOError:
        print(IOError)
    p = player()
    p.starterPack(awcl)
    listing(p.characters)
    return

if __name__ == "__main__":
    main()
