import matplotlib.pyplot as plt
import numpy as np

def ChangeMassForce(mode, modeNautilus) :
    newMassForce = modeNautilus[mode]
    return newMassForce

def ConvertX(motor, water):
    if motor - water == 750:
        return 0.75
    elif motor - water == 1000 :
        return 1
    else :
        return 0
    
def ConvertY(mass, archimede, y):
    if mass > archimede :
        return -1
    elif mass < archimede and y < 10:
        return 1
    else :
        return 0

def GetNextPoint(lastPointX, lastPointY, mass, archimede, motor, water):
    nextPoint = [lastPointX + ConvertX(motor, water), 
                 lastPointY + ConvertY(mass, archimede, lastPointY)]
    return nextPoint

def BuildNautilus():

    waterLevel = [24,10]
    waterLevel2 = [10,10]

    # Vertical Forces --
    # Mass Force
    modeNautilus = [10000, 12000, 13000]
    massForce = modeNautilus[0]

    # Archimede Force
    archimedeForce = 12000
    # --------------------

    # Horizontal Forces --
    # Motor Force
    motorForce = [0, 1000, 2000]

    # Water Force
    waterForce = [0, 250, 1000]

    speedIndex = 0
    # --------------------
 
    checkpointsMass = [[2,2],[8,1],[9,0],[11,1],[13,0]]
    stageMass = 0

    
    checkpointsSpeed = [[2,1],[4,2],[11,1],[13,0],[14,1],[15,2],[18,0]]
    stageSpeed = 0

    pointsX = [10]
    pointsY = [10]

    for i in range(20) :
        
        if stageMass < len(checkpointsMass) and i == checkpointsMass[stageMass][0] :
            massForce = ChangeMassForce(checkpointsMass[stageMass][1], modeNautilus)
            stageMass = stageMass + 1

        if stageSpeed < len(checkpointsSpeed) and i == checkpointsSpeed[stageSpeed][0] :
            speedIndex = checkpointsSpeed[stageSpeed][1]
            stageSpeed = stageSpeed + 1

        

        nextPoint = GetNextPoint(pointsX[i], pointsY[i], massForce, archimedeForce, motorForce[speedIndex], waterForce[speedIndex])
        pointsX.append(nextPoint[0])
        pointsY.append(nextPoint[1])

    plt.plot(waterLevel, waterLevel2)
    plt.plot(pointsX, pointsY)

    plt.xlabel('Distance parcourue')
    plt.ylabel('Profondeur')

    plt.show()




# Run
BuildNautilus()

# INFORMATIONS :
# masse : 10 000 t (vide), 12 000 t (semi-remplit), 13 000 t (remplit)
# archimède (volume d'eau déplacée) : 12 000 t
# vitesse : 0, 1000, 2000 (selon la puissance utilisée)
# résistance eau : 0, 250, 1000 (selon la vitesse au dessus)