import math

class Helper(object):
    def getAngledPoint(angle,longueur,cx,cy):
        x = (math.cos(angle)*longueur)+cx
        y = (math.sin(angle)*longueur)+cy
        return (x,y)
    getAngledPoint = staticmethod(getAngledPoint)
    
    def calcAngle(x1,y1,x2,y2):
         dx = x2-x1
         dy = y2-y1
         #angle = (math.atan2(dy,dx) % (2*math.pi)) * (180/math.pi)
         angle = (math.atan2(dy,dx) ) #% (2*math.pi)) * (180/math.pi)
         return angle
    calcAngle = staticmethod(calcAngle)
    
    def calcDistance(x1,y1,x2,y2):
         dx = abs(x2-x1)**2
         dy = abs(y2-y1)**2
         distance=math.sqrt(dx+dy)
         return distance
    calcDistance = staticmethod(calcDistance)
    
    def calcRotation(oX, oY, pX, pY, angle):
        #Rotation dans le sens antihoraire
        #angle en radians
        rX = oX + math.cos(angle) * (pX - oX) - math.sin(angle) * (pY - oY)
        rY = oY + math.sin(angle) * (pX - oX) + math.cos(angle) * (pY - oY)
        return rX, rY #resultat
    calcRotation = staticmethod(calcRotation)