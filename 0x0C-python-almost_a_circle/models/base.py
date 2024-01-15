#!/usr/bin/python3
"""Module for the base class"""
import json
import csv


class Base:
    """This will be the base for all
    other classes in this project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation"""
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method to return json format of the dict attributes"""

        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Method to return json format of dict attributes into a file"""

        if len(list_objs) != 0:
            objects = [obj.to_dictionary() for obj in list_objs]
            content = cls.to_json_string(objects)
            name = f'{cls.__name__}.json'
        else:
            content = '[]'
            name = 'Base.json'

        with open(name, 'w', encoding='utf-8') as file:
            file.write(content)

    @staticmethod
    def from_json_string(json_string):
        """Method to convert json back to dict format"""

        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Method to convert the json dict into actual instances"""

        class_args = {'Rectangle': ('width', 'height', 'x', 'y'),
                      'Square': ('size', 'x', 'y')}
        if cls.__name__ not in class_args:
            raise ValueError(f"Unsupported class: {cls.__name__}")

        instance = cls(*[dictionary[arg] for arg in class_args[cls.__name__]])
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Method to convert dict in a file to ans instance"""

        name = f'{cls.__name__}.json'
        try:
            with open(name, 'r', encoding='utf-8') as file:
                j_file = file.read()
                lis = cls.from_json_string(j_file)
                if not lis:
                    return []

                inst_list = []
                for dic in lis:
                    inst_list.append(cls.create(**dic))
                return inst_list
        except FileNotFoundError:
            return []

    @staticmethod
    def to_csv_row(obj):
        """Method to convert Rectangle object to a CSV row"""

        return [obj.id, obj.width, obj.height, obj.x, obj.y]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method to serialize into csv format"""

        name = f'{cls.__name__}.csv'
        with open(name, 'w', newline='') as file:
            write_file = csv.writer(file)
            for obj in list_objs:
                write_file.writerow(cls.to_csv_row(obj))

    @classmethod
    def load_from_file_csv(cls):
        """Deserialized from csv to list"""

        name = f'{cls.__name__}.csv'
        try:
            with open(name, 'r') as file:
                csv_list = csv.reader(file)
                if not csv_list:
                    return []

                inst_list = []
                for obj in csv_list:
                    obj_dict = {
                        'id': int(obj[0]),
                        'width': int(obj[1]),
                        'height': int(obj[2]),
                        'x': int(obj[3]),
                        'y': int(obj[4]),
                        }
                    if cls.__name__ == 'Square':
                        obj_dict['size'] = int(obj[1])
                    instance = cls.create(**obj_dict)
                    inst_list.append(instance)
                return inst_list
        except FileNotFoundError:
            return []
