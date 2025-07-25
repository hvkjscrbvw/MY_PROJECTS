string1 = "12010120122"
string2 = string1.replace("1", "50%, ")
string3 = string2.replace("0", "0%, ")
string4 = string3.replace("2", "100%, ")
string5 = string4.replace(" %,", "")
print(string1)
print(string5)
