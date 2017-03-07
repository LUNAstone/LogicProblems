# Sweets and Bags code

def main():
    print("Sweets and Bags", end="\n\n")
    # Get the inputs
    bags = int(input("How many bags are there? "))
    sweets = int(input("How many sweets are there? "))
    # Check that there aren't more bags than sweets.
    if sweets < bags:
        print("You need more sweets than there are bags.")
        main()
    else:
        # Then go onto the next step
        does_it_work(sweets, bags)


"""
See if is able to split up the sweets into
the bags evenly, with an odd number of sweets
in each bag.
"""
def does_it_work(sweets, bags):
    working = sweets - (bags - 1)
    working = working % 2 == 1

    # If the number is odd
    if working == True:
        print("It works.")
        best_possible(sweets, bags)
    else:
        # or quit out of the program.
        print("It does not work.")
        quit()

        
"""
Displays the most amount of sweets that can
be evenly spread to each bag.
So that it doesn't end up as
[1, 1, 1, 1, 1, 1, 1, 1, 21]
"""
def best_possible(sweets, bags):
    leftover_sweets = sweets - bags
    extras = leftover_sweets // 2

    bag_base = []
    for bag in range(0, bags):
        bag_base.append(1)

    bag_extras = []
    while leftover_sweets > 0:
        for bag in range(0, bags):
            if extras > 0:
                bag_extras.append(bag_base[bag] + 2)
                extras -= 1
            else:
                bag_extras.append(bag_base[bag])

        total = 0
        for bag in bag_extras:
            total += bag

        bag_base = bag_extras
        bag_extras = []
        leftover_sweets = sweets - total
        extras = leftover_sweets // 2

        if leftover_sweets % 2 == 1:
            print("Not possible.")
            break
        
    if leftover_sweets % 2 != 1:
        print(bag_base)
        type1 = bag_base[0]
        type1_count = 0
        type2_count = 0

        for bag in bag_base:
            if bag == type1:
                type1_count += 1
            else:
                type2 = bag
                type2_count += 1

        print("%s bags with %s sweets in, and %s bags with %s sweets in."
              % (str(type1_count), str(type1), str(type2_count), str(type2)))
        
        
if __name__ == "__main__":
    main()
