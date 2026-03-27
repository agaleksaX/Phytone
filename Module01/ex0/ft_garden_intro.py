def ft_garden_intro():
    name: str = input("Enter name plant: ")
    height: int = int(input("Enter size plant: "))
    age: int = int(input("Enter age plant: "))

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("=== End of Program ===")

if __name__ == "__main__":
    ft_garden_intro()
