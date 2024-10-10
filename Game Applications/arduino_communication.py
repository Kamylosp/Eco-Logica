import pandas as pd
import serial
import time

class TrashVerifier:
    def __init__(self, trash_number=5, trash_scenarios=1, port='COM5', baud_rate=9600, byte_number=9, csv_file="trash.csv"):
        self.trash_number = trash_number
        self.trash_scenarios = trash_scenarios
        self.port = port
        self.baud_rate = baud_rate
        self.byte_number = byte_number
        self.csv_file = csv_file
        self.trash_sheet = pd.read_csv(self.csv_file)

    def trash_verify(self, data):
        trash_type = data[0]
        id = int(''.join(map(str, data[1:9])))

        if id in self.trash_sheet['Endereco'].values:
            line = self.trash_sheet[self.trash_sheet['Endereco'] == id]
            name = line['Nome'].values[0]
            scenario = line['Cenario'].values[0]
            type_required = 1 if line['Tipo'].values[0] == 'organico' else 2
        else:
            return

        if scenario == self.trash_scenarios:
            if trash_type == type_required:
                self.trash_number -= 1
                # Graphic implementation to a Right answer
                return 1
            else:
                # Graphic implementation to warn that the trash is correct, but in the wrong bin
                return 0
        else:
            # Graphic implementation to warn that it is not the trash required
            return 0

    def send_data(self, servo_situation):
        with serial.Serial(self.port, self.baud_rate) as ser:
            ser.write(str(servo_situation).encode())

    def get_data(self):
        with serial.Serial(self.port, self.baud_rate) as ser:
            while True:
                if ser.in_waiting >= self.byte_number:
                    data = list(map(int, ser.read(self.byte_number)))
                    self.send_data(self.trash_verify(data))
                else:
                    time.sleep(0.1)
