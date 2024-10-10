import pandas as pd
import serial
import time

class TrashVerifier:
    def __init__(self, trash_number=5, trash_scenarios=1, port='COM5', baud_rate=9600, byte_number=10, csv_file="trash.csv"):
        self.trash_number = trash_number
        self.trash_scenarios = trash_scenarios
        self.port = port
        self.baud_rate = baud_rate
        self.byte_number = byte_number
        self.csv_file = csv_file
        self.trash_sheet = pd.read_csv(self.csv_file)

        # Inicializar a porta serial
        self.ser = serial.Serial(self.port, self.baud_rate)  # Abre a porta aqui

    def __del__(self):
        # Certifica-se de que a porta serial é fechada quando a instância é destruída
        if self.ser.is_open:
            self.ser.close()

    def trash_verify(self, data):
        trash_type = int(data[0])
        id = int(''.join(map(str, data[1:10])))  # Ajuste aqui para pegar os 9 IDs

        if id in self.trash_sheet['Endereco'].values:
            line = self.trash_sheet[self.trash_sheet['Endereco'] == id]
            name = line['Nome'].values[0]
            scenario = line['Cenario'].values[0]
            type_required = 1 if line['Tipo'].values[0] == 'organico' else 2

            #print("Name: ", name, ",Scenario: ", scenario, ",Type_required: ", type_required)
        else:
            return

        if scenario == self.trash_scenarios:
            #print(self.trash_scenarios, scenario)
            if trash_type == type_required:
                #print(trash_type, type_required)
                self.trash_number -= 1
                return 1  # Resposta correta
            else:
                return 0  # Lixo correto, mas no recipiente errado
        else:
            return 0  # Lixo não requerido

    def send_data(self, servo_situation):
        if self.ser.is_open:
            print("Data Sent, servo situation: ", str(servo_situation).encode())
            self.ser.write(str(servo_situation).encode())
            #self.ser.write(bytes([servo_situation])) 
        else:
            print("A porta serial não está aberta.")

    def get_data(self):
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