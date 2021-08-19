from dotenv import load_dotenv
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests

load_dotenv()


class ServiceGetStudentGradeByToken():
    def get_grade(self, sid):
        """Func get grade."""
        pivot = sid.copy()
        for i, id in enumerate(sid.keys()):
            print(f'Получаем список оценок токенам {i+1} / {len(sid)}')
            service1 = os.getenv('SERVICE1')
            URL = service1 + f'{id}' + '&lang=eng'
            try:
                request = requests.get(url=URL, verify=False, auth=(os.getenv('LOGIN'), os.getenv('PASSWORD')))
                requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            except Exception as err:
                print(f'{err}\n Ошибка при работе сервиса для получения оценок')
                continue
            print(f'\nlist of grade {len(sid)}\n')
            if request.status_code == 200:
                grades = request.json()
                for name in grades:
                    prefix = name
                    for grade in grades[f'{prefix}']:
                        if len(grade['ConrolResult']) == 1:
                            name_discipline = f"{grade['DocumentDate'][:4]} {grade['CourseName']}"
                            pivot[id][name_discipline] = grade['ConrolResult']
            else:
                return f'sorry, not found grade for {sid}'
        return pivot

    def get_course(self, pivot):
        course_list = []
        for i in pivot:
            for keys in pivot[i]:
                disipline = {}
                disipline['CourseName'] = keys
                course_list.append(disipline)
        result = list({d['CourseName']: d for d in course_list}.values())
        newlist = sorted(result, key=lambda k: k['CourseName'])
        return newlist
