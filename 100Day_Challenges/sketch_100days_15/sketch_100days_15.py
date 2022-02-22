def std_weight(height, gender): # height = m, gender "man"/"woman"
    if gender == "man":
        return height * height *22
    else:
        return height * height *21

height = 175 #cm
gender= "man"
weight = round(std_weight(height / 100, gender), 2)
print("Height {0}cm {1}'s average weight {2}kg.".format(height, gender, weight))
