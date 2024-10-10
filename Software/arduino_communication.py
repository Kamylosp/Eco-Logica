import serial
import pandas as pd
import time

trashNumber = 5 #Trashes per scenario
trashScenarios = 1 #Current scenario
port = 'COM5' #Port for serial communication
baudRate = 9600 #Baud rate for serial communication
byteNumber = 9
    
#Data[0] is the number of the bin which the trash was inserted (1 for organic and 2 for recyclabe);
#Data[1:9] is the ID
def trash_verify(data):
    trashSheet = pd.read_csv("trash.csv")
    #Saves in which bin the trash was inserted
    trashType = data[0]
    #Save the id read by the RFID module
    id = int(''.join(map(str, data[1:9])))
    #Verifies if the ID is in the sheet and then saves its type and name
    if id in trashSheet['Endereco'].values:
        line = trashSheet[trashSheet['Endereco'] == id]
        name = line['Nome'].values[0]
        scenario = line['Cenario'].values[0]
        if(line['Tipo'].values[0] == 'organico'):
            typeRequired = 1
        else:
            typeRequired = 2
    else:
        return
    if(scenario == trashScenarios):
        if(trashType == typeRequired):
            trashNumber -= 1
            #Graphic implementation to a Right answer
            return 1
        else:
            #Graphic implementation to warn that the trash is correct, but in the wrong bin
            return 0
    else:
        #Graphic implementation to warn that it is not the trash required
        return 0
    
def send_data(servoSituation):
    ser = serial.Serial(port, baudRate)
    ser.write(str(servoSituation))

#This function has to be subcalled in a loop.
def get_data():
    ser = serial.Serial(port, baudRate)
    if ser.in_waiting >= byteNumber:
        data = int(ser.read(byteNumber))
        send_data(trash_verify(data))
    else:
        time.sleep(0.1)

#For testint
if __name__ == "__main__":
    while(trashScenarios < 7):
        while(trashNumber >= 0):
            get_data()
        trashNumber = 5
        trashScenarios += 1
                    

        