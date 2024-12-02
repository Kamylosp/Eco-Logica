import pandas as pd
import serial
import time

trash_number = int(0)
verify = 0
trash_scenarios = 1
port = 'COM8'
baud_rate = 9600
byte_number = 13
csv_file = "C:/Users/italo/OneDrive/Documentos/Integrador/Eco-Logica/Game Applications/trash.csv"

trash_sheet = pd.read_csv(csv_file)

ser = serial.Serial(port, baud_rate)

def trash_verify(data, verify):
    global trash_number
    trash_type = data[0]
    id = int(''.join(map(str, data[1:])))

    if id in trash_sheet['Endereco'].values:
        line = trash_sheet[trash_sheet['Endereco'] == id]
        name = line['Nome'].values[0]
        scenario = line['Cenario'].values[0]
        type_required = 1 if line['Tipo'].values[0] == 'organico' else 2
    else:
        return 0  
    # print(scenario)
    # print(trash_scenarios)
    if int(scenario) == int(trash_scenarios):
        # print(trash_type)
        # print(type_required)
        if int(trash_type) == int(type_required):
            trash_number+=1
            verify = 1
            return 1 
        else:
            verify = 0
            return 0  
    else:
        verify = 0
        return 0  

def send_data(servo_situation):
    if ser.is_open:
        print(str(servo_situation).encode())
        ser.write(str(servo_situation).encode())
    else:
        print("A porta serial não está aberta.")

def get_data(verify):
    print("Waiting for start signal ('s') from Arduino...")
    while True:
        if ser.in_waiting > 0:
            start_signal = ser.read(1).decode()  
            if start_signal == 's':  
                print("Start signal received. Beginning data processing.")
                break  

    while True:
        if ser.in_waiting >= byte_number:
            data = ser.read(byte_number)
            data_str = data.decode().strip()  
            trash_type = int(data_str[0])  
            id = int(data_str[1:])
            print(f"Trash Type: {trash_type}, ID: {id}")
            # print("trash_verify: ", trash_verify(data_str))
            send_data(trash_verify(data_str, verify))
        else:
            time.sleep(0.1)

if __name__ == "__main__":
    try:
        while trash_scenarios <= 3:
            get_data(verify)
            if(trash_number == 3):
                trash_scenarios += 1
            if(trash_number == 6):
                trash_scenarios += 1
    finally:
        if ser.is_open:
            ser.close()
