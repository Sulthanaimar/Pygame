import os

listfile = os.listdir()
print(listfile)

sourceFileDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(sourceFileDir)