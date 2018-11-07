# Created By: J.Medlock
# Created On: 11/2/2018
import os

x = 0
os.chdir("C:\\Users\\jbmedlock\\AppData\\Local\\Temp\\")
for y in range(0, 100):
    with open("TestFiles_%d.test" % y, "w") as f:
        f.write("Test")
        f.close()
# with open("C:\\Users\\jbmedlock\\AppData\\Local\\Temp\\TestFiles_%d.test" % x, "w") as f:
#     f.write("Test")
#     f.close()
