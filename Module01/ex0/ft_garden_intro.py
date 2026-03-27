def ft_garden_intro():
    name: str = input("Enter name plant: ")
    height: int = int(input("Enter size plant: "))
    age: int = int(input("Enter age plant: "))

    print("=== Welcome to My Garden ===")
    print("Plant: ", name)
    print("Height: ", height, "cm")
    print("Age: ", age, " days")
    print("=== End of Program ===")

if __name__ == "__main__":
    ft_garden_intro()
