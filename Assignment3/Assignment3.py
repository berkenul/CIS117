# Homework 3
# Author: Berk Enul
# Date: September 3, 2026

try:
    highway = int(input("Enter a highway number: "))

    if highway <= 0 or highway > 999:
        print("Invalid highway number.")

    elif highway <= 99:
        if highway % 2 == 0:
            print(f"Interstate {highway} runs east/west.")
        else:
            print(f"Interstate {highway} runs north/south.")

    else:
        primary = highway % 100

        if primary == 0:
            print("Invalid highway number.")
        elif primary % 2 == 0:
            print(
                f"Interstate {highway} is an auxiliary highway serving "
                f"I-{primary}, which runs east/west."
            )
        else:
            print(
                f"Interstate {highway} is an auxiliary highway serving "
                f"I-{primary}, which runs north/south."
            )

except ValueError:
    print("Invalid highway number.")