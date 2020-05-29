from datetime import datetime

class Start_code():

    def __init__(self, log_path):
        self.log_path = log_path

    def __enter__(self):
        self.start_time = datetime.now()
        self.log = open(self.log_path, 'a', encoding='utf-8')
        self.log.write(f'Время старта: {datetime.now()}\n')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.log.write(f'Дата открытия файла: {datetime.now()}\n')
        self.log.write(f'Дата закрытия файла: {datetime.now() - self.start_time}\n')
        self.log.close()
