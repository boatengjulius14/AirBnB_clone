#!/usr/bin/python3
"""Defines the class HBNBCommand
The entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Definition of HBNBCommand Class"""
    prompt = "(hbnb)"

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
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
