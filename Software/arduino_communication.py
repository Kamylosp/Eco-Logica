import serial
import pandas as pd
import time
import random

score = 0
#Data[0] is the number of the bin which the trash was inserted (1 for organic and 2 for recyclabe);
#Data[1:9] is the ID
#Trash is the trash required by the game
def trashVerify(data, trash):
    trashSheet = pd.read_csv("trash.csv")
    #Saves in which bin the trash was inserted
    trashType = data[0]
    #Save the id read by the RFID module
    id = int(''.join(map(str, data[1:9])))
    #Verifies if the ID is in the sheet and then saves its type and name
    if id in trashSheet['Endereco'].values:
        line = trashSheet[trashSheet['Endereco'] == id]
        type = line['Tipo'].values[0]
        name = line['Nome'].values[0]
    else:
        return
    #Search in the sheet the type of the sheet based on the name required
    if trash in trashSheet['Nome'].values:
        line = trashSheet[trashSheet['Nome'] == trash]
        if(line['Tipo'].values[0] == 'organico'):
            typeRequired = 1
        else:
            typeRequired = 2
    else:
        return
    if(trash == name):
        if(trashType == typeRequired):
            score += 10
            #Graphic implementation to a Right answer
            return 1
        else:
            #Graphic implementation to warn that the trash is correct, but in the wrong bin
            score -= 5
            return 0
    else:
        #Graphic implementation to warn that it is not the trash required
        score -= 10
        return 0

if __name__ == "__main__":
    port = 'COM5'  
    baudRate = 9600
    byteNumber = 9
    #csv = pd.read_csv('trash', sep=',')
    adresses = [151615615, 115615666]
    types = ['organico', 'reciclavel']
    names = ['banana', 'plastico']

    csvDataFrame = {
        'Endereco': adresses,
        'Tipo': types,
        'Nome': names,
    }

    trash = pd.DataFrame(csvDataFrame)

    ser = serial.Serial(port, baudRate)
    while True:
        trash
        if ser.in_waiting >= byteNumber:
            data = int(ser.read(byteNumber))
            print(data)
            feedback = trashVerify(data, )
        else:
            time.sleep(0.1)
        