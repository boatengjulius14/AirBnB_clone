#!/usr/bin/python3
"""Defines the class HBNBCommand
The entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Definition of HBNBCommand Class"""
    prompt = "(hbnb) "
    class_names = ["BaseModel", "User", "State", "City", "Amenity",
                   "Place", "Review"]
    parse_commands = ["all", "count", "show", "destroy", "update"]
    dict_elem_no = 1

    @staticmethod
    def analyze_line(line):
        """Analyzes string and returns _list of arguments or an
        empty list
        """
        _list = []
        if line == "":
            print("** class name missing **")

        elif ' ' in line and line.count(' ') > 0:
            _list = line.split(' ')
            while ('' in _list):
                _list.remove('')

        elif line not in HBNBCommand.class_names:
            print("** class doesn't exist **")

        elif line in HBNBCommand.class_names:
            print("** instance id missing **")
        return _list

    @staticmethod
    def parse_line(line):
        """Analyzes command and returns parsed string
        to precmd module"""
        arg = _command = ""

        symbols = ['.', '(', ')']
        str_symbols = ["\"", "'"]
        dict_symbols = ['{', ':', '}']

        for i in line:
            if i in str_symbols:
                line = line.replace(i, "")

        if all(sym in line for sym in symbols)\
            and line.count('(') == 1 and line.count(')') == 1\
                and line.count('.') == 1:
            _class, _command = line.strip(')').split('.')

            if '(' in _command:
                _command, arg = _command.split('(')
                if ',' in arg:
                    arg_list = arg.split(',')
                    arg = ' '.join(arg_list)

        if all(sym in arg for sym in dict_symbols):
            HBNBCommand.dict_elem_no = arg.count(":")
            for sym in dict_symbols:
                if sym in arg:
                    arg = arg.replace(sym, " ")

        if _command in HBNBCommand.parse_commands:
            line = ' '.join((_command, _class, arg))
        print(line)
        return line

    def do_quit(self, line):
        """quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def help(self):
        """provides info about the command interpreter"""
        pass

    def emptyline(self):
        """Execute when no commands are passed"""
        pass

    def do_create(self, line):
        """Creates a new instance of class, saves it
        (to the JSON file) and prints the id
        """
        if line == "":
            print("** class name missing **")
        elif line not in HBNBCommand.class_names:
            print("** class doesn't exist **")
        else:
            obj = eval(line)()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id
        """
        _list = HBNBCommand.analyze_line(line)
        if _list != []:
            if len(_list) == 2 and _list[0] in HBNBCommand.class_names:
                store_obj = storage.all()
                input = '{}.{}'.format(*_list)
                if input in store_obj:
                    print(store_obj[input])
                else:
                    print("** no instance found **")
            elif _list[0] not in HBNBCommand.class_names:
                print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        _list = HBNBCommand.analyze_line(line)
        if _list != []:
            if len(_list) == 2 and _list[0] in HBNBCommand.class_names:
                store_obj = storage.all()
                input = '{}.{}'.format(*_list)
                if input in store_obj:
                    storage._FileStorage__objects.pop(input)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name
        """
        if line == "":
            print([str(x) for x in storage.all().values()])
        else:
            if line in HBNBCommand.class_names:
                print([str(x) for x in storage.all().values()
                       if line in str(x)])
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """updates an instance based on the class name and id
        by adding or updating attributes(save the change into the JSON file)
        """
        _list = HBNBCommand.analyze_line(line)
        print(_list)
        if _list != []:
            input = f'{_list[0]}.{_list[1]}'
            if input in storage.all():
                if len(_list) == 2:
                    print("** attribute name missing **")
                elif len(_list) == 3:
                    print("** value missing **")
                else:
                    key_idx = 2
                    value_idx = 3
                    obj = storage.all()[input]
                    while (HBNBCommand.dict_elem_no):
                        if _list[key_idx] in obj.__dict__:
                            v_type = type(obj.__dict__[_list[key_idx]])
                            setattr(obj, _list[key_idx],
                                    v_type(_list[value_idx]))
                        else:
                            try:
                                setattr(obj, _list[key_idx],
                                        eval(_list[value_idx]))
                            except NameError:
                                setattr(obj, _list[key_idx], _list[value_idx])
                        key_idx += 2
                        value_idx += 2
                        HBNBCommand.dict_elem_no -= 1

                    HBNBCommand.dict_elem_no = 1

            elif _list[0] not in HBNBCommand.class_names:
                print("** class doesn't exist **")
            else:
                print("** no instance found **")
            storage.save()

    def do_count(self, line):
        """prints the number of instances of a class"""
        if line in HBNBCommand.class_names:
            print(len([x for x in storage.all() if x.count(line)]))
        else:
            print("** class doesn't exist **")

    def precmd(self, line):
        return cmd.Cmd.precmd(self,  HBNBCommand.parse_line(line))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
