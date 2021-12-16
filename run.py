def article1():
    
    print("Article 1:\n")
    x = int(input("Enter calories: "))
    y = int(input("How much fat? "))
    z = int(input("Carbs? "))
    w = int(input("And protein? "))
    
    article1_result = [x, y, z, w]
    return article1_result

print(article1())