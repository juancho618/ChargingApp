import Route
import Station
from User import User
from Owner import Owner
import Main2

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 08:37:12 2016

@author: Bram
"""

#All the stations gathered with their reservations etc.        
class Database():
    
    def __init__(self):
        self._users = []
        self._owners = []
        self._stations = []
        self._freeID = 0    # when adding a user to the DB, increment !


    #--------------------------------------------
    # SETTERS AND GETTERS
    #---------------------------------------------
    
    # return the list of users
    def getUsers(self):
        return self._users

    # return the list of owners
    def getOwners(self):
        return self._owners
        
    # return the list of stations
    def getStations(self):
        return self._stations

    #--------------------------------------------
    # OTHER FUNCTIONALITY
    #---------------------------------------------

    '''     def returnPassword(self,name):
        for x in self._users:
            if x.getMail() == name:
                return x.getPassword()'''

    # It is best not to include a returnPassword function, but better a private function authenticate(password), i think
    # also, does this functionality belong in database or in user?

    # add person to one or both of the existing lists : Owners , Users. Also set the ID to be the current freeID
    # afterwards increment freeID
    def addPerson(self, person):
        if type(person) is Owner:
            self._owners.append(person)
            self._users.append(person)      # other possible implementation : create a PersonList, with all the objects
                                            # userList and ownerList only contain the ID
            person.setID(self._freeID)
        elif type(person) is User:
            self._users.append(person)
            person.setID(self._freeID)

        self._freeID += 1

    def removePerson(self,id):
        for person in self._users:
            if person.ID == id:
                self._users.remove(person)
                if type(person) == Owner:
                    self._owners.remove(person)
                    for st in self._stations:
                        if st.getOwnerID == id:
                            st.resetStation()



    # look in list of stations and retrieve all stations with corresponding owner_id
    # change owner-attribute to None


    def removeDefectStations(self):
        # TODO : implement this
        # check how long station has been defect
        # if longer than ..... remove
        # this checks the list given by getAllDefectStations once a day
        # INSIDE MAIN, this function needs to be called (use a timer)


    def addStation(self, station):
        self._stations.append(station)

    # Takes a stationID and looks for it in the list of stations. It returns that Station OR None
    def checkStationExists(self,id):
        for station in self._stations:
            if station.getStationID is id:
                return station
        return None


    # retrieves a list with all defect stations
    def getAllDefectStations(self):
        defects = []
        for st in self.getStations():
                if st.isDefect():
                    defects.append(st)
        return defects


    # retrieves a list with all working stations
    def getAllWorkingStations(self):
        working = []
        for st in self.getStations():
                if not st.isDefect():
                    working.append(st)
        return working