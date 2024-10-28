# Cindy Hernandez
# Mod 1.3
#10/27/24
# Function should take the input and count backwards to 1 while displaying the number of remaining bottles of beer on the wall.

def countdown_bottles(n):
    for i in range(n, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print("Take one down, pass it around,")
            print(f"{i - 1} bottles of beer on the wall.\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down, pass it around,")
            print("No more bottles of beer on the wall.\n")

def main():
    while True:
        try:
            bottles = int(input("How many bottles of beer are on the wall (enter 0 to quit)? "))
            if bottles == 0:
                print("Goodbye!")
                break
            elif bottles > 0:
                countdown_bottles(bottles)
            else:
                print("Please enter a positive number or 0 to quit.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
