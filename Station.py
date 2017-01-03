from geopy.geocoders import Nominatim

class Station():
    
    #Only stationID and address are mandatory. The others can have default values while waiting for more specific info
    def __init__(self, stationID, address):
        #TODO: specify that a user must pinpoint a charging station by giving the exact ID mentionned on the pole)

        self._stationID = stationID
        self._geolocator = Nominatim()
        self._location = self._geolocator.geocode(address)

        self._ratingList = []        # list of scores that users give (from 0 to 5)

        self._isFast = False   # Boolean: 2 different charging speeds 3.3 kW/h = SLOW or 6.6 kW/h = FAST
        self._price = 0.0 # price in EURO per kWh
        self._ownerID = 0
        self._defect = False    # TODO: this should be linked to the OWNER (notification)

    def __str__(self):
        return "ID:%i , address:%s , Fast: %r, price: %f, defect: %r, avg_rating: %f, number of votes: %i" % (self._stationID, self._address, self._isFast
                                                                         , self._price, self._defect, self.calcRating(), len(self._ratingList))
    #--------------------------------------------
    # SETTERS AND GETTERS
    #---------------------------------------------

    def setStationID(self, ID):
        self._stationID = ID

    def getStationID(self):
        return self._stationID

    def setLocation(self, address):
        self._location = self._geolocator.geocode(address)

    def getLocation(self):
        return self._location

    # accepts a boolean, to set isFast to True or False
    def setSpeed(self, isFast):
        self._isFast = isFast

    def getSpeed(self):
        return self._isFast

    def _setRatingList(self,ratingList):
        self._ratingList = ratingList

    def _getRatingList(self):
        return self._ratingList

    def setPrice(self,price):
        self._price = price

    def getPrice(self):
        return self._price

    def setOwnerID(self, ownerID):
        self._ownerID = ownerID

    def getOwnerID(self):
        return self._ownerID

    def setDefect(self, isDefect):
        self._defect = isDefect

    def isDefect(self):
        return self._defect

    def resetStation(self):
        self._isFast = False
        self._price = 0.0
        self._ownerID = 0
        # defect is not reset because if it was defect, it will stay defect



    #--------------------------------------------
    # OTHER FUNCTIONALITY
    # ---------------------------------------------

    def calcRating(self):
        result = 0
        if len(self._ratingList) > 0:
            for x in self._ratingList:
                result += x
            result /= len(self._ratingList)
        return result

    # checks if the given user already rated this station
    # if a rating of that user already exists, the value is changed
    # if not, a new rating (tuple UserID, Rating) is appended to the ratingList
    def _checkIfRated(self, userID):
        for ratingTuple in self._ratingList:
            if ratingTuple[0] is userID:
                return ratingTuple
        return  None

    def setRating(self, userID, rating):
        ratingTuple = self.checkIfRated(userID)             # checkIfRated returns [userID,rating]
        if 5 >= rating >= 0 :
            if ratingTuple is None:
                self._ratingList.append([userID,rating])    # create a ratingTuple and append to ratingList
            else:
                ratingTuple[1] = rating;                    # update the rating value




#---------------------------------------------------
# TEST
#-----------


station1 = Station(1232, "Pleinlaan 6,Etterbeek")

print(station1.getLocation().address)
print(station1.getLocation().latitude, station1.getLocation().longitude)
station1.setRating(453,5)
station1.setRating(453,9)
print(station1.calcRating())
station1.setRating(454,3)
print("New Rating: ", station1.calcRating())

