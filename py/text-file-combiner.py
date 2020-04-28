# text file combiner
import zipfile
import glob
import os

os.chdir("C:\\Users\\darsa\\Desktop\\Furn_Flash")
pw = os.getcwd()
pw
read_files = glob.glob("*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
