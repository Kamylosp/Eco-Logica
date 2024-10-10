import pandas as pd
import serial
import time
#Class to ease the implementation
class TrashVerifier:
    def __init__(self, trash_number=5, trash_scenarios=1, port='COM5', baud_rate=9600, byte_number=10, csv_file="trash.csv"):
        self.trash_number = trash_number #Number of trashes per scenario
        self.trash_scenarios = trash_scenarios #Number of scenarios until the end of the game
        self.port = port #Port for serial communication
        self.baud_rate = baud_rate #Baudrate
        self.byte_number = byte_number #Size of the message sent by the arduino
        self.csv_file = csv_file #Sheet with the trashes
        self.trash_sheet = pd.read_csv(self.csv_file)

        #Serial communication initialization
        self.ser = serial.Serial(self.port, self.baud_rate)

    def __del__(self):
        #Destroy the serial instance when the serial port closes
        if self.ser.is_open:
            self.ser.close()

    def trash_verify(self, data):
        trash_type = int(data[0]) #The first number of the message is the type of the trash is type of trash #1 for organic and #2 for recyclabe
        id = int(''.join(map(str, data[1:10]))) #The rest of the message, which contains the id

        #Searches the id in the CSV, takes the name, scenario and type
        if id in self.trash_sheet['Endereco'].values:
            line = self.trash_sheet[self.trash_sheet['Endereco'] == id]
            name = line['Nome'].values[0]
            scenario = line['Cenario'].values[0]
            type_required = 1 if line['Tipo'].values[0] == 'organico' else 2

            #print("Name: ", name, ",Scenario: ", scenario, ",Type_required: ", type_required)
        else:
            return

        #Verifies if the trash is being read in the correct scenario and if it is being read in the correct bin
        if scenario == self.trash_scenarios:
            #print(self.trash_scenarios, scenario)
            if trash_type == type_required:
                #print(trash_type, type_required)
                self.trash_number -= 1 #To change the scenario when the trashes of that scenario finish
                return 1  #Correct answer
            else:
                return 0  #Correct bin, in the wrong scenario, implement a graphic warn to the user
        else:
            return 0  #Wrong bin, in the Wrong scenario, implement a graphic warn to the user
    
    #Function to send data to the arduino, sends 1 if the answer is correct and 0 if the answer is incorrect
    def send_data(self, servo_situation):
        if self.ser.is_open:
            print("Data Sent, servo situation: ", str(servo_situation).encode())
            self.ser.write(str(servo_situation).encode())
            #self.ser.write(bytes([servo_situation])) 
        else:
            print("A porta serial não está aberta.")
    #Function to get data from the arduino
    def get_data(self):
        #Clears the buffer before start reading
        print("Waiting for start signal ('s') from Arduino...")
        while True:
            if self.ser.in_waiting > 0:  # Verifica se há dados na porta
                start_signal = self.ser.read(1).decode()  # Lê 1 byte
                if start_signal == 's':  # Se o sinal for 's', comece a processar
                    print("Start signal received. Beginning data processing.")
                    break  # Sai do loop após receber o sinal

        while handler.trash_scenarios < 7:
            while handler.trash_number >= 0:
                if self.ser.in_waiting >= self.byte_number:
                    data = self.ser.read(self.byte_number)
                    data_str = data.decode().strip()  # Decodifica os dados
                    trash_type = int(data_str[0])  # Primeiro número
                    id = int(data_str[1:])  # Os outros 9 números
                    print(f"Trash Type: {trash_type}, ID: {id}")
                    self.send_data(self.trash_verify(data_str))
                    time.sleep(2)
                else:
                    time.sleep(0.1)
            handler.trash_number = 5
            #handler.trash_scenarios += 1

if __name__ == "__main__":
    handler = TrashVerifier()
    handler.get_data()