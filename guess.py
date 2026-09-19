def make_guess(low, high):
    return (low + high) // 2

low = 0
high = 50
print("Think of a number between 0 and 50.")

while low <= high:
    guess = make_guess(low, high)
    answer = input("Is your number " + str(guess) + "? (yes / no): ")
    if answer == "yes":
        print("Very Nice!(~Borat Voice~)")
        break
    answer = input("Is your number higher or lower? ")
    if answer == "higher":
        low = guess + 1
    else:
        high = guess - 1

        #Github link https://github.com/AReverri/SSW540/blob/main/guess.py