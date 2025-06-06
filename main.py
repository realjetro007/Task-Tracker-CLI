import sys
from datetime import *
import cmd
import json

def ID_Gen():       #Generates ID's For ToDo List Items
    l=[]
    count=0
    with open("items.json", "r") as f:
        text = json.load(f)
    for each_item in range(len(text)):
        l.append(text[each_item]["id"])
    if not l:
        return count

    if l:
        while count in l:
            count += 1
        return count




class MyCLI(cmd.Cmd):
    def __init__(self):
        super(MyCLI, self).__init__()

        with open("items.json", "r") as f:
            self.data = json.load(f)


    prompt = '>= '
    intro = 'Welcome to my Task Tracker. Type "help" for available commands.'

    def do_add(self, line):

        item={
            "id": ID_Gen(),
            "description": line,
            "status": "todo",
            "CreatedAt": str(datetime.today()),
            "UpdatedAt": str(datetime.today())
        }
        self.data.append(item)
        with open("items.json", "w") as out_file:
            json.dump(self.data, out_file)
        print("Task added successfully ID",item["id"])
    def do_delete(self, value):
        for each_item in range(len(self.data)):
            if self.data[each_item-1]["id"] == int(value):
                del self.data[each_item-1]
        with open("items.json", "w") as out_file:
            json.dump(self.data, out_file)

    def do_update(self, value):
        for each_item in range(len(self.data)):
            if self.data[each_item]["id"] == int(value[:1]):
                self.data[each_item].update({"description": value[2:]})
                self.data[each_item].update({"UpdatedAt": str(datetime.today())})
        with open("items.json", "w") as out_file:
            json.dump(self.data, out_file)

    def do_mark_todo(self, value):
        for each_item in range(len(self.data)):
            if self.data[each_item]["id"] == int(value[:1]):
                self.data[each_item].update({"status": "todo"})
                self.data[each_item].update({"UpdatedAt": str(datetime.today())})
        with open("items.json", "w") as out_file:
            json.dump(self.data, out_file)

    def do_mark_in_progress(self, value):
        for each_item in range(len(self.data)):
            if self.data[each_item]["id"] == int(value):
                self.data[each_item].update({"status": "in-progress"})
                self.data[each_item].update({"UpdatedAt": str(datetime.today())})
        with open("items.json", "w") as out_file:
            json.dump(self.data, out_file)

    def do_mark_done(self, value):
        for each_item in range(len(self.data)):
            if self.data[each_item]["id"] == int(value):
                self.data[each_item].update({"status": "done"})
                self.data[each_item].update({"UpdatedAt": str(datetime.today())})
        with open("items.json", "w") as out_file:
            json.dump(self.data, out_file)

    def do_list(self, stat):
        templ = []
        if stat == '':
            for each_item in range(len(self.data)):
                templ.append(self.data[each_item]["description"])
            txt = ','.join(templ)
            print(txt)
        elif stat == "done":
            for each_item in range(len(self.data)):
                if self.data[each_item]["status"] == "done":
                    templ.append(self.data[each_item]["description"])
            txt=','.join(templ)
            print(txt)
        elif stat == "todo":
            for each_item in range(len(self.data)):
                if self.data[each_item]["status"] == "todo":
                    templ.append(self.data[each_item]["description"])
            txt = ','.join(templ)
            print(txt)
        elif stat == "in-progress":
            for each_item in range(len(self.data)):
                if self.data[each_item]["status"] == "in-progress":
                    templ.append(self.data[each_item]["description"])
            txt = ','.join(templ)
            print(txt)
        with open("items.json", "w") as out_file:
            json.dump(self.data, out_file)

    def do_clear(self, none):
        self.data=[]
        with open("items.json", "w") as out_file:
            json.dump(self.data, out_file)

    def do_end(self, none):
        sys.exit()

if __name__ == '__main__':
    app = MyCLI()

    MyCLI().cmdloop()











