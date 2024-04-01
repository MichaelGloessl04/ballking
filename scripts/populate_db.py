import requests


def get_students_from_xlsx(file_path: str):
    import pandas as pd
    df = pd.read_excel(file_path)
    students = []
    for i, row in df.iterrows():
        student = {
            'name': row['Vorname'],
            'surname': row['Nachname'],
            'classes': row['Klasse'],
            'points': 0
        }
        students.append(student)
    return students


def add_students_to_db(students: list):
    for student in students:
        response = requests.post('http://localhost:80/students',
                                 json=student)
        response = requests.get(
            f'http://localhost:80/students/{response.json()["id"]}')
        if response.status_code != 200:
            raise Exception(f'Error adding {student} to db')
        print(f'Added {student} to db')


if __name__ == '__main__':
    students = get_students_from_xlsx(
        "C:\\Users\\MGloe\\Desktop\\Klassenlisten_aktuell_8.2..xlsx")
    add_students_to_db(students)
    print('done')
