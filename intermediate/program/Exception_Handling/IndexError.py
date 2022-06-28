fruits = ["Apple", "Banana", "Watermelon"]

def make_juice(index):
    try:
        fruit = fruits[index]
    except IndexError as error_message:
        print("You can't make this kind of juice")
    else:
        print(fruits + "juice")


make_juice(4)
