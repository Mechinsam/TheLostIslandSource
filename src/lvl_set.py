from pickle import dump

lvl = input("_$ ")
dump(lvl, open("DATA/save.dat", "wb"))