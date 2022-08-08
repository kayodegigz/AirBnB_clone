#!/usr/bin/python3
"""
Entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage  # in the init file


class HBNBCommand(cmd.Cmd):
    """
    command interpreter class
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Do nothing"""
        pass

    def do_create(self, line):
        """creates a new instance of basemodel class"""
        line_list = line.split()
        if len(line_list) < 1:
            print("** class name missing **")
        if line_list[0] != "BaseModel": #we'll have to refactor and make this dynamic
            print("** class doesn't exist **")
       new_inst = BaseModel()
       new_inst.save()
       print(new_inst.obj)

    def do_show(self, line):
        line_list = line.split()
        if len(line_list) < 1:
            print("** class name missing **")
        if line_list[0] != "BaseModel":  # this also has to be dynamic
            print("** class doesn't exist **")
        if len(line_list) < 2:
            print("** instance id missing **")
        obj_key = ".".join(line_list)
        if obj_key not in storage.all():  # this too
            print("** no instance found **")
        print(storage.all()[obj_key])

    def do_destroy(self, line):
        line_list = line.split()
        if len(line_list) < 1:
            print("** class name missing **")
        if line_list[0] != "BaseModel":  # this
            print("** class doesn't exist **")
        if len(line_list) < 2:
            print("** instance id missing **")
        obj_key = ".".join(line_list)
        if obj_key not in storage.all():  # this too
            print("** no instance found **")
        del storage.all()[obj_key]

    def do_all(self, line):
        line_list = list.split()
        if len_list[0] != "BaseModel":
            print("** class doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
