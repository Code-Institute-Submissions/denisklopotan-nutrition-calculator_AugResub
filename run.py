print('*'*80)
print("Welcome user! This simple 'Nutrition Calculator' helps you\
 add calories\nand nutritional values of food and returns total sum.\n")
print("You can enter only 2 articles of food in this version, in sequence.\
 \nThey will be simply called 'Article 1' & 'Article 2'.\n")
print("Enter only round number values or zero (0) of following:\nenergy\
 in calories (cal); fat, carbohydrate and protein content in grams (g).\n")
print("To start over, press 'Restart' button located in top left corner.\
 \nAnd...dont forget to smile! Its healthy and burns calories too! :D\n")
print('*'*80)


def article1():
    """
    Gets nutritional value input from the user as integer, int().
    If other type than int() is submitted while loop raises ValueError
    and asks user to input correct value of round number.
    """
    print("\nArticle 1:\n")
    while True:
        try:
            x = int(input("Enter calories: "))
            y = int(input("How much fat? "))
            z = int(input("Carbohydrates? "))
            w = int(input("And protein? "))
        except ValueError:
            print("This is not a round number! Please provide correct value")
            continue
        else:
            break

    """
    Access a variable outside of a function with syntax 'func.variable'
    Values stored will be used to iterate and calculate sum later on.
    """
    article1.variable = [x, y, z, w]

article1()


def article2():
    """
    Same as for article1()
    """
    print("\nArticle 2:\n")
    while True:
        try:
            x = int(input("Enter calories: "))
            y = int(input("How much fat? "))
            z = int(input("Carbohydrates? "))
            w = int(input("And protein? "))
        except ValueError:
            print("This is not a number! Please provide correct value")
            continue
        else:
            break

    article2.variable = [x, y, z, w]

article2()

"""
Using zip() function to aggregate elements from two iterables or lists.
Getting sum of added values and printing nutritional values by index
with corresponding description inside of f-string.
"""
result = zip(article1.variable, article2.variable)
sum = [x + y for (x, y) in result]
print(f'\nTotal calories: {sum[0]}cal, Fat: {sum[1]}g,\
 Carbohydrates: {sum[2]}g, Protein: {sum[3]}g')
