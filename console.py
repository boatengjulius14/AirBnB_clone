#!/usr/bin/python3
"""Defines the class HBNBCommand
The entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User


class HBNBCommand(cmd.Cmd):
    """Definition of HBNBCommand Class"""
    prompt = "(hbnb)"
    CLASS_NAMES = ["BaseModel", "User"]

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
        """Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id
        """
        if line == "":
            print("** class name missing **")
        elif line not in self.CLASS_NAMES:
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            obj.save()
            print(obj.id)

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

        elif line != "BaseModel":
            print("** class doesn't exist **")

        elif line == "BaseModel":
            print("** instance id missing **")
        return _list

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id
        """
        _list = HBNBCommand.analyze_line(line)
        if _list != []:
            if len(_list) == 2 and _list[0] in self.CLASS_NAMES:
                store_obj = storage.all()
                input = '{}.{}'.format(*_list)
                if input in store_obj:
                    print(store_obj[input])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        _list = HBNBCommand.analyze_line(line)
        if _list != []:
            if len(_list) == 2 and _list[0] in self.CLASS_NAMES:
                store_obj = storage.all()
                input = '{}.{}'.format(*_list)
                if input in store_obj:
                    storage._FileStorage__objects.pop(input)
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances
        based or not on the class name
        """
        if line == "":
            print([str(x) for x in storage.all().values()])
        else:
            if line in self.CLASS_NAMES:
                print([str(x) for x in storage.all().values()
                       if line in str(x)])
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """updates an instance based on the class name and id
        by adding or updating attributes(save the change into the JSON file)
        """
        _list = HBNBCommand.analyze_line(line)
        if _list != []:
            input = f'{_list[0]}.{_list[1]}'
            if input in storage.all():
                if len(_list) == 2:
                    print("** attribute name missing **")
                elif len(_list) == 3:
                    print("** value missing **")
                else:
                    obj = storage.all()[input]
                    if _list[2] in obj.__dict__:
                        v_type = type(obj.__dict__[_list[2]])
                        setattr(obj, _list[2], v_type(_list[3]))
                    else:
                        try:
                            setattr(obj, _list[2], eval(_list[3]))
                        except NameError:
                            setattr(obj, _list[2], _list[3])

            else:
                print("** no instance found **")
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
