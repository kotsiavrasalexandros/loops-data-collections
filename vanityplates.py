from collections import Counter
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if len(plate) >= 2 and len(plate) <= 6:
        pass
    if plate[1] == "0":
        return False
    if plate[1].isalpha() and plate[2].isdigit():
        return False
    elif len(plate) >= 2 and len(plate) <= 6:
        return True


main()