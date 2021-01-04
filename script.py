# Copyright Edwin Sundberg 2021
import xml.etree.ElementTree, os
filepath = f"{os.getenv('APPDATA')}/Bungie/DestinyPC/prefs/cvars.xml"
os.chmod(filepath, 0o777)
tree = xml.etree.ElementTree.parse(filepath)
root = tree.getroot()
tree.find('namespace',)
print("Please select one of the following options:")
print("disable / quick swap / quick swap + heavy")
action = input()
if action == "quick swap" or action == "quick swap + heavy":
    print("What keybind would you like to use?")
    keybind = input()
    keybind = keybind.replace('!','')
if action == "quick swap":
    for elem in tree.iterfind('namespace/cvar'):
        if elem.attrib["name"] == "switch_weapons":
            normal = elem.attrib["value"].split('!')[0]
            elem.set("value", f"{normal}!{keybind}")
        elif elem.attrib["name"] == "next_weapon":
            normal = elem.attrib["value"].split('!')[0]
            elem.set("value", f"{normal}!unused")
        elif elem.attrib["name"] == "move_forward":
            normal = elem.attrib["value"].split('!')[0]
            elem.set("value", f"{normal}!{keybind}")
        elif elem.attrib["name"] == "toggle_sprint":
            normal = elem.attrib["value"].split('!')[0]
            elem.set("value", f"{normal}!{keybind}")
elif action == "quick swap + heavy":
    for elem in tree.iterfind('namespace/cvar'):
        if elem.attrib["name"] == "switch_weapons":
            normal = elem.attrib["value"].split('!')[0]
            elem.set("value", f"{normal}!unused")
        elif elem.attrib["name"] == "next_weapon":
            normal = elem.attrib["value"].split('!')[0]
            elem.set("value", f"{normal}!{keybind}")
        elif elem.attrib["name"] == "move_forward":
            normal = elem.attrib["value"].split('!')[0]
            elem.set("value", f"{normal}!{keybind}")
        elif elem.attrib["name"] == "toggle_sprint":
            normal = elem.attrib["value"].split('!')[0]
            elem.set("value", f"{normal}!{keybind}")
elif action == "disable":
    keybind = "unused"
    for elem in tree.iterfind('namespace/cvar'):
        if elem.attrib["name"] == "switch_weapons":
            normal = elem.attrib["value"].split('!')[0]
            elem.set("value", f"{normal}!{keybind}")
        elif elem.attrib["name"] == "next_weapon":
            normal = elem.attrib["value"].split('!')[0]
            elem.set("value", f"{normal}!{keybind}")
        elif elem.attrib["name"] == "move_forward":
            normal = elem.attrib["value"].split('!')[0]
            elem.set("value", f"{normal}!{keybind}")
        elif elem.attrib["name"] == "toggle_sprint":
            normal = elem.attrib["value"].split('!')[0]
            elem.set("value", f"{normal}!{keybind}")
else:
    print("Invalid option, try again")
tree.write(filepath)
os.chmod(filepath, 0o555)
