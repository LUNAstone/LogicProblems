def main():
    print("Sweets and Bags", end="\n\n")
    bags = int(input("How many bags are there? "))
    sweets = int(input("How many sweets are there? "))
    if sweets < bags:
        print("You need more sweets than there are bags.")
        main()
    else:
        does_it_work(sweets, bags)

        
def does_it_work(sweets, bags):
    working = sweets - (bags - 1)
    working = working % 2 == 1

    if working == True:
        print("It works.")
        best_possible(sweets, bags)
    else:
        print("It does not work.", end="\n\n")
        quit()

        
def best_possible(sweets, bags):
    pass
        
        
if __name__ == "__main__":
    main()
