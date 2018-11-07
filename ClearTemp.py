# Created By: J.Medlock
# Created On: 10/30/2018
## 10.30.18 -> Created temp removal code with paths included
## 11.01.18 -> Adjusted pathway for C:\Windows\Temp


import os, sys
import base64
import getpass
import re


class DeleteTempFiles(object):


    def __init__(self, path, username, password):
        self.path = path
        self.username = username
        self.password = password


    def deleteUserTemp(path):
        for root, dirs, files in os.walk(path):
            for file in filter(lambda x: re.match(r'^[a-zA-Z0-9]{1,}.*$', x), files):
                try:
                    os.remove(os.path.join(root, file))
                except PermissionError:
                    continue
                except IOError:
                    continue

    def deleteWindozeTemp(path):
        for root, dirs, files in os.walk(path):
            for file in filter(lambda x: re.match(r'^[a-zA-Z0-9]{1,}.*$', x), files):
                try:
                    os.remove(os.path.join(root, file))
                except PermissionError:
                    continue
                except IOError:
                    continue


if __name__ == "__main__":
    username = os.getlogin()
    pathDict = {
        "userPath": "C:\\Users\\" + username + "\\AppData\\Local\\Temp\\",
        "windowsPath": "C:\\Windows\\Temp\\"
    }
    #
    # adminUsername = input("Enter Username: ")
    # adminPassword = getpass.getpass(input("Enter Password: "))
    #
    # if adminUsername in open('credentials.txt').readlines():
    DeleteTempFiles.deleteWindozeTemp(pathDict['windowsPath'])
    # else:
    DeleteTempFiles.deleteUserTemp(pathDict['userPath'])



