def countingletters (text):
    UC = 0  # upper case
    LC = 0  # lower case
    NT = 0  # not a letter

    for char in text:
        if char == char.upper() and char.isalpha():
            UC += 1
        elif char == char.lower() and char.isalpha():
            LC += 1
        else:
            NT += 1

    print("The number of upper case letters is: ", UC)
    print("The number of lower case letters is: ", LC)
    print("The number of ALL letters is: ", UC + LC)
    print("The number of not letters is: ", NT)
    print("The number ALL is: ", UC + LC + NT)

countingletters(r"m)b9gkJ2qAfDdC&+S9K*-n5%?Q_^@gyC~btu~^S(rnm}#atnoF96!8;V<JU3w8YYmP:p,3ps&t81+9L#A%&F;zovwu(Q/aSUb@X")