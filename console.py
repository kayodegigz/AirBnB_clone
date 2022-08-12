#!/usr/bin/python3
"""
Entry point of the command interpreter
"""

import cmd
from models.__init__ import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage  # in the init file


class HBNBCommand(cmd.Cmd):
    """
    command interpreter class
    """
    prompt = '(hbnb) '
    classes = {"BaseModel", "State", "City",
               "Amenity", "Place", "Review", "User"}

    def do_quit(self, line):
        """Exit the program"""
        return True

    def do_EOF(self, line):
        """Exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing"""
        pass

    def do_create(self, line):
        """creates a new instance of basemodel class"""
        line_list = line.split()
        if len(line_list) < 1:
            print("** class name missing **")
            return
        if line_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_inst = eval(line)()
        new_inst.save()
        print(new_inst.id)

    def do_show(self, line):
        """Print string representation: name and id"""
        line_list = line.split()
        if len(line_list) < 1:
            print("** class name missing **")
            return
        if line_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        try:
            if line_list[1]:
                obj_key = ".".join(line_list)
                if obj_key not in storage.all().keys():  # this too
                    print("** no instance found **")
                    return
                print(storage.all()[obj_key])
        except IndexError:
            print("** instance id missing **")

    def do_destroy(self, line):
        """Destroy instance specified by user; Save changes to JSON file"""
        line_list = line.split()
        if len(line_list) < 1:
            print("** class name missing **")
            return
        if line_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(line_list) < 2:
            print("** instance id missing **")
            return
        try:
            if line_list[1]:
                obj_key = ".".join(line_list)
                if obj_key not in storage.all().keys():  # this too
                    print("** no instance found **")
                    return
                del storage.all()[obj_key]
                storage.save()
        except IndexError:
            print("** instance id missing **")

    def do_all(self, line):
        """Print all objects or all objects of specified class"""
        line_list = line.split()
        if len(line_list) == 0:  # if no arg is passed to all command
            print([str(v) for v in storage.all().values()])
            return
        if line_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        elif len(line_list) > 0:
            print([str(v) for v in storage.all().values()
                  if type(v).__name__ == line_list[0]])

    def do_count(self, line):
        """Count all instances of a class"""
        if line not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        print(len(storage.all().keys()))

    def do_update(self, line):
        """Update if given exact object, exact attribute"""
        line_list = line.split()
        if len(line_list) < 1:
            print("** class name missing **")
            return
        if line_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(line_list) < 2:
            print("** instance id missing **")
            return
        key = f"{line_list[0]}.{line_list[1]}"
        if key not in storage.all().keys():
            print("** no instance found **")
            return
        if len(line_list) < 3:
            print("** attribute name missing **")
            return
        if len(line_list) < 4:
            print("** value missing **")
            return
        if isinstance(eval(line_list[3]), int):  # strip off str ndcheck if int
            line_list[3] = int(line_list[3])
        elif isinstance(eval(line_list[3]), float):  # or if float
            line_list[3] = float(line_list[3])
        else:
            line_list[3] = line_list[3]

        obj = storage.all()[key]  # check for d particular inst
        setattr(obj, line_list[2], line_list[3])
        storage.all()[key].save()

    def default(self, line):
        """
        every other case
        """
        if "." not in line:
            print("*** Unknown syntax: {}".format(line))
            return
        try:
            line_list = line.split('.')
            arg = line_list[0]
            cmd = line_list[1].replace('(', '').replace(')', '')
            if cmd == 'all':
                HBNBCommand.do_all(self, arg)
            elif cmd == 'count':
                HBNBCommand.do_count(self, arg)
            elif 'show' in cmd:
                cmd = cmd[4:].replace('"', '').replace("'", '')
                arg = arg + ' ' + cmd
                HBNBCommand.do_show(self, arg)
            elif 'destroy' in cmd:
                cmd = cmd[7:].replace('"', '').replace("'", '')
                arg = arg + ' ' + cmd
                HBNBCommand.do_destroy(self, arg)
            elif 'update' in cmd:
                cmd = cmd.split(',')
                id = cmd[0][6:].replace('"', '').replace("'", '')
                if cmd[1][0] == '{':
                    name = cmd[1]
                else:
                    name = cmd[1].replace('"', '').replace("'", '')
                value = cmd[2].replace(
                     '"', '').replace("'", '') if len(cmd) > 2 else ""
                arg = arg + ' ' + id + ' ' + name + ' ' + value
                HBNBCommand.do_update(self, arg)
            else:
                print("*** Unknown syntax: {}".format(line))
        except IndexError:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
