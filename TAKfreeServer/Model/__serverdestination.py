#######################################################
# 
# __serverdestination.py
# Python implementation of the Class __serverdestination
# Generated by Enterprise Architect
# Created on:      11-Feb-2020 11:08:10 AM
# Original author: Corvo
# 
#######################################################


class __serverdestination:
# default constructor       def __init__(self):  

    # string composed by IP:port: protocol:machineID. e.g. 192.168.0.103:4242:tcp:
    # ANDROID-R52JB0CDC4E
    destinations = "" 
     # destinations getter 
     def getdestinations(self): 
      return self.destinations 
 
     # destinations setter 
     def setdestinations(destinations=0):  
     self.destinations=destinations 
     