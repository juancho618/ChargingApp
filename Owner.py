from User import User # User is a module, not a class, so import User.User !!
from Station import Station


# Owner has more options than a standard user
class Owner(User):

    def __init__(self,name,mail, pwd):
        super(Owner, self).__init__(name,mail,pwd)

    # Check if stationID already exists in list of stations. It receives a tuple from the db function
    # if it does not exist, make a new station, else, point to the existing station
    # use setters to change values
    def addStation(self, db, ID, address, isFast, price):

        st = db.checkStationExists(ID) # checkStationExists gives back a station

        if st is None:
            newStation = Station(ID, address)   # create new station
            db.addStation(newStation)
        else:
            newStation = st             # don't create a new station but point to the existing one

        newStation.setSpeed(isFast)     # add additional information
        newStation.setPrice(price)

    def rateStation(self, db,stationID, rating):
        st = db.checkStationExists(stationID)   #checkStationExists returns a station
        if not st is None:
            st.setRating(self._ID,rating)
        #TODO Laurent: implement a check to see if user is an owner and if station belongs to that owner

    # retrieves a list with all defect stations corresponding to
    def getMyDefectStations(self,db):
        myDefects = []
        for st in db.getStations():
            if st.getOwneriD == self._ID :
                if st.isDefect() :
                    myDefects.append(st)
        return myDefects

    def removeStation(self):
        pass
        #TODO: only owners can remove stations


    def solveDefect(self,db,stationID):
        st = db.checkStationExists(stationID)   #checkStationExists returns a station
        if not st is None:
            if st.getOwneriD == self._ID :
                st.setDefect(False)
            else:
                print("Action failed: Owner ID does not match with corresponding station")
        print("Action failed: No station found with this stationID")


#---TESTING-----------------
myOwner = Owner("Master Master","jefke@gmail.com", "pwd1")
print(myOwner)