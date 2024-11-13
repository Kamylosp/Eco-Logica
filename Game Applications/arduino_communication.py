import pandas as pd
import serial
import time

# Classe para facilitar a implementação
class TrashVerifier:
    def __init__(self, trash_number=4, trash_scenarios=1, port='COM5', baud_rate=9600, byte_number=12, csv_file='trash.csv'):
        self.trash_number = trash_number  # Número de lixos por cenário
        self.trash_scenarios = trash_scenarios  # Número de cenários até o fim do jogo
        self.port = port  # Porta para comunicação serial
        self.baud_rate = baud_rate  # Taxa de transmissão
        self.byte_number = byte_number  # Tamanho da mensagem enviada pelo Arduino
        self.csv_file = csv_file  # Arquivo CSV com os dados dos lixos

        try:
            # Tentativa de leitura do arquivo CSV
            self.trash_sheet = pd.read_csv(self.csv_file)  # Leitura do CSV
        except FileNotFoundError:
            print(f"Erro: O arquivo {self.csv_file} não foi encontrado.")
            self.trash_sheet = pd.DataFrame()  # Cria um DataFrame vazio para evitar outros erros

        try:
            # Inicialização da comunicação serial
            self.ser = serial.Serial(self.port, self.baud_rate)
        except serial.SerialException as e:
            print(f"Erro ao abrir a porta serial: {e}")
            self.ser = None

    def __del__(self):
        # Fecha a instância da comunicação serial quando a porta é fechada, se a porta estiver aberta
        if self.ser and self.ser.is_open:
            self.ser.close()

    def trash_verify(self, data):
        trash_type = int(data[0])  # O primeiro número da mensagem indica o tipo do lixo (1 para orgânico, 2 para reciclável)
        id = int(data[1:])  # O restante da mensagem contém o ID do lixo

        # Pesquisa o ID no CSV e pega o nome, cenário e tipo
        if id in self.trash_sheet['Endereco'].values:
            line = self.trash_sheet[self.trash_sheet['Endereco'] == id]
            name = line['Nome'].values[0]
            scenario = line['Cenario'].values[0]
            type_required = 1 if line['Tipo'].values[0] == 'organico' else 2
        else:
            return  # Retorna sem fazer nada se o ID não for encontrado

        # Verifica se o lixo está sendo lido no cenário correto e no tipo correto
        if scenario == self.trash_scenarios:
            if trash_type == type_required:
                self.trash_number -= 1  # Decrementa o número de lixos restantes
                return 1  # Resposta correta
            else:
                return 0  # Tipo incorreto
        else:
            return 0  # Cenário incorreto

    # Função para enviar dados para o Arduino (1 para resposta correta e 0 para incorreta)
    def send_data(self, servo_situation):
        if self.ser and self.ser.is_open:
            print(f"Data Sent, servo situation: {str(servo_situation)}")
            self.ser.write(bytes([servo_situation]))  # Envia os dados como byte
        else:
            print("A porta serial não está aberta.")

    # Função para obter dados do Arduino
    def get_data(self):
        print("Aguardando sinal de início ('s') do Arduino...")
        while True:
            if self.ser and self.ser.in_waiting > 0:  # Verifica se há dados na porta
                start_signal = self.ser.read(1).decode()  # Lê 1 byte
                if start_signal == 's':  # Se o sinal for 's', começa a processar
                    print("Sinal de início recebido. Iniciando o processamento de dados.")
                    break  # Sai do loop após receber o sinal

        while self.trash_scenarios < 7:
            while self.trash_number > 0:
                if self.ser and self.ser.in_waiting >= self.byte_number:
                    data = self.ser.read(self.byte_number)  # Lê os dados da porta serial
                    data_str = data.decode().strip()  # Decodifica os dados
                    trash_type = int(data_str[0])  # Tipo de lixo
                    id = int(data_str[1:])  # O ID do lixo
                    print(f"Tipo de Lixo: {trash_type}, ID: {id}")
                    self.send_data(self.trash_verify(data_str))  # Envia a resposta ao Arduino
                    time.sleep(2)
                else:
                    time.sleep(0.1)
            self.trash_number = 5  # Reseta o número de lixos para o próximo cenário
            self.trash_scenarios += 1  # Incrementa para o próximo cenário

if __name__ == "__main__":
    handler = TrashVerifier()  # Cria uma instância da classe TrashVerifier
    handler.get_data()  # Inicia o processo de obtenção de dados do Arduino
