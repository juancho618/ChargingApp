from geopy.distance import great_circle
from MergeSort import mergeSort

from Station import Station

#Standard user
class User():
    
    def __init__(self, name, mail, password):
        self._ID = 0;       #what did we say about
        self._name = name
        self._mail = mail
        self._password = password

    def __str__(self):
        return "UserID:%i , name:%s , mail: %s" % (self._userID, self._name, self._mail)

    #--------------------------------------------
    # SETTERS AND GETTERS
    #---------------------------------------------

    def setID(self,id):
        self._ID = id

    def getID(self):
        return self._ID

    def setName(self,name):
        self._name = name

    def setMail(self, mail):
        self._mail = mail

    def getMail(self):
        return self._mail

    def setPassword(self, pwd):
        self._password = pwd
        
    def getPassword(self):  # IS THIS WISE TO INCLUDE THIS FUNCTION?? // MAYBE REPLACE WITH AUTHENTICATE()
        return self._password

    #--------------------------------------------
    # OTHER FUNCTIONALITY
    #---------------------------------------------


    # Check if stationID already exists in list of stations. It receives a tuple from the db function
    # if it does not exist, make a new station
    def addStation(self,db, ID, address):
        st = db.checkStationExists(ID)  # checkStationExists gives back a station

        if st is None:
            newStation = Station(ID, address)  # create new station
            db.addStation(newStation)

    # check if the stationID exists. If not, do nothing, else:
    # set Rating. Implementation of setRating() depends on whether or not the user has already given a rating or not
    # cf. Station class
    def rateStation(self, db,stationID, rating):
        st = db.checkStationExists(stationID)   #checkStationExists returns a station
        if not st is None:
            st.setRating(self._ID,rating)

    def defectAlert(self,db,stationID):
        st = db.checkStationExists(stationID)   #checkStationExists returns a station
        if not st is None:
            st.setDefect(True)

    def getNearbyStation(self,currentAddress,db):
        listStation = db.getAllWorkingStations()
        listMeasured = []
        smallest = []

        for st in listStation[:]:
            listMeasured.append([st,self.measureDistance(currentAddress,st.getLocation() )])

        listMeasured = mergeSort(listMeasured)

        for i in range(10):
            smallest.append(listMeasured.get(i))

        return smallest



    #returns the distance in METERS
    def measureDistance(self,location1, location2):
        return great_circle(location1, location2).meters




#----TESTING----------------
myUser = User("I am a poor user","jefke@gmail.com", "pwd1")
print(myUser)

# listStation = [ 0 , 1, ........, 19] = all working stations in db
# listMeasured = []
# loop over all first 10 stations in listStation:
#  listMeasured = [ (0, 2.5) , (1, 3.4) , (2, 2.23) , (....) , (9,5.7)] = tuple of (st , distance to current)
# SORT
