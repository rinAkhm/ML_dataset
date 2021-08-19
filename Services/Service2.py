from dotenv import load_dotenv
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests
load_dotenv()


class ServiceSearchStudentByEmail():
    def get_data_from_service(self, students):
        """Can get list of students."""
        token_list = []
        url = os.getenv('SERVICE2')
        for num, email in enumerate(students):
            print(f'Получаем список токенов по email {num+1} / {len(students)}')
            try:
                requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                request = requests.post(url=url, auth=(os.getenv('LOGIN'), os.getenv('PASSWORD')), verify=False,
                                        data=f'domainemail={email}&degree=bachelor')
                get_one_answer = request.json()
            except Exception as err:
                print(f'{err}\n Ошибка при поиске токена')
                continue
            for i in get_one_answer[''][1]['collection']:
                if i not in token_list:
                    token_list.append(i)
        temp = self.clear_token_list(token_list)
        return temp

    def clear_token_list(self, list_token):
        """create new dict and send to main file."""
        list_id = []
        for line in list_token:
            list_id.append((line['fullName'], line['group'], line['email'], line['guid']))
        print(f'\nlist of students {len(list_id)}\n')
        return list_id

    def pivot(self, list_person):
        '''create pivot list'''
        pivot = {}
        for num, line in enumerate(list_person):
            if line[3] not in pivot:
                pivot[line[3]] = {}
        return pivot
