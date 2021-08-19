import os

class WorkList:
    def read_file(self):
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'list_of_student1.txt')
        try:
            with open(f'{path}') as file:
                text = file.read().split('\n')
            return text
        except Exception:
            raise FileVerificationNotFound('Файл не был найден')


class FileVerificationNotFound(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'Ошибка: {self.message}'