import json

class StudentDB:

    def __init__(self):
        self.__data = None

    # Establish connection between json file
    def connect(self, data_file_path):
        with open(data_file_path) as json_file:
            self.__data = json.load(json_file)

    # gets data from the json file
    def get_data(self, name):
        for student in self.__data['students']:
            if student['name'] == name:
                # returns the student dict
                return student

    def close(self):
         pass
