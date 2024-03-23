#
# File: Superhero_Scoreboard.py
# Author: Nathan Foale
# Description:This is about the battle game between heroes and villains. There will be summary table which 
#                           includes the information of battles fought, battles won, battles lost, battles drawn, and a health value.
#                           Everytime,if there are batlles or any changes in the character members. the summary table will be automatically updated.

import random

# Reading characters file.
def read_file(filename):
    # Creating a new list in order to store all the information of battles fought, battles won, battles lost, battles drawn, and a health value of heroes and  villains.
    character_list = []

    infile = open(filename, "r")

    index = 0

    # Reading first line of characters file.
    line = infile.readline()

    # While the end of the text file has not been reached
    while line != '':
        # Get name
        name = line.strip('\n')

        # Read in next line
        line = infile.readline()

        # Get secret_identity
        secret_id = line.strip('\n')

        # Read in next line
        line = infile.readline()

        # Split line into no battles, no won, no lost, etc.
        info_list = line.split()
        is_hero = info_list[0]
        no_battles = int(info_list[1])
        no_won = int(info_list[2])
        no_lost = int(info_list[3])
        no_drawn = int(info_list[4])
        health = int(info_list[5])

        # Create new list to store individual character information
        new_character = [name, secret_id, is_hero, no_battles, no_won, no_lost, no_drawn, health]

        # Add new character to character_list (creating a list of lists)
        character_list.append(new_character)

        # Read next line of file.
        line = infile.readline()

    return character_list


# Displaying the hereos and villains' sumary of battles fought, battles won, battles lost, battles drawn, and a health value
def display_characters(character_list, display_type):
    print('\n===================================================')
    print('-     Character (heroes and villains) Summary     -')
    print('===================================================')
    print('-                             P  W  L  D  Health  -')
    print('---------------------------------------------------')
    if display_type == 1:
        for index in range(len(character_list)):
            print('-  ' + "{0:<20}".format(character_list[index][0]) + "{0:>8}".format(character_list[index][3]) + "{0:>3}".format(character_list[index][4]) + "{0:>3}".format(character_list[index][5]) + "{0:>3}".format(character_list[index][6]) + "{0:>8}".format(character_list[index][7]) + '  -')
    elif display_type == 2:
        for index in range(len(character_list)):
            if character_list[index][2] == 'h':
                print('-  ' + "{0:<20}".format(character_list[index][0]) + "{0:>8}".format(character_list[index][3]) + "{0:>3}".format(character_list[index][4]) + "{0:>3}".format(character_list[index][5]) + "{0:>3}".format(character_list[index][6]) + "{0:>8}".format(character_list[index][7]) + '  -')
    elif display_type == 3:
        for index in range(len(character_list)):
            if character_list[index][2] == 'v':
                print('-  ' + "{0:<20}".format(character_list[index][0]) + "{0:>8}".format(character_list[index][3]) + "{0:>3}".format(character_list[index][4]) + "{0:>3}".format(character_list[index][5]) + "{0:>3}".format(character_list[index][6]) + "{0:>8}".format(character_list[index][7]) + '  -')
    print('---------------------------------------------------')
    print('===================================================')

# Function write_to_file() - place your own comments here...  : )
def write_to_file(filename, character_list):
    outfile = open(filename, "w")
    for index in range(len(character_list)):
        # write character's name to file
        outfile.write(character_list[index][0] + "\n")
        # write character's secret name to file
        outfile.write(character_list[index][1] + "\n")
        # write battle stat to file
        outfile.write(character_list[index][2] + " " + str(character_list[index][3]) + " " + str(character_list[index][4]) + " " + str(character_list[index][5]) + " " + str(character_list[index][6]) + " " + str(character_list[index][7]) + "\n")
    outfile.close()

# Function find_character() - place your own comments here...  : )
def find_character(character_list, name):
    pos = -1
    for index in range(len(character_list)):
        if character_list[index][0] == name:
            pos = index
    return pos

# Function add_character() - place your own comments here...  : )
def add_character(character_list, name, secret_id, is_hero):
    flag = find_character(character_list, name)
    if flag == -1:
        character_list.append([name, secret_id, is_hero, 0, 0, 0, 0, 100])
        print('Successfully added ' + name + ' to character list.')
    else:
        print("\n" + name + " already exists in character list.")
    return character_list

# Function remove_character() - place your own comments here...  : )
def remove_character(character_list, name):
    removed_list = []
    if find_character(character_list, name) == -1:
        print("\n" + name + " is not found in characters.")
    else:
        for index in range(len(character_list)):
            if index != find_character(character_list, name):
                removed_list.append(character_list[index])
        print("\nSuccessfully removed " + name + " from character list")
    return removed_list

# Function display_highest_battles_won() - place your own comments here...  : )
def display_highest_battles_won(character_list):
    # Place your code here
    max_win_pos = 0
    flag = 0
    for index in range(len(character_list)):
        if character_list[index][4] > character_list[max_win_pos][4]:
            max_win_pos = index
            flag = 1
        elif character_list[index][4] == character_list[max_win_pos][4] and character_list[index][3] > character_list[max_win_pos][3]:
            max_win_pos = index
            flag = 1
    if flag == 0:
        if (character_list[0][4] > character_list[1][4]):
            print("\nHighest number of battles won => " + character_list[max_win_pos][0] + " with " + str(character_list[max_win_pos][4]) + " opponents defeated!")
        else:
            print("\nNo one had the highest of number of winnings.")
    else:
        print("\nHighest number of battles won => " + character_list[max_win_pos][0] + " with " + str(character_list[max_win_pos][4]) + " opponents defeated!")

# Function do_battle() - place your own comments here...  : )
# Parameters: character_list - list of characters (list of lists).
#             opponent1_pos  - position/index of character in character_list.
#             opponent2_pos  - position/index of character in character_list.

print("File     : assignment2.py")
print("Author   : Nathan Foale")
print("Email ID : foany001")
print("This is my own work as defined by the University's Academic Misconduct policy. ")

### Define list to store character information
character_list = read_file("characters.txt")
choice = ''
while choice != 'quit':
    print("\n\nPlease enter choice")
    choice = input("[list, heroes, villains, search, reset, add, remove, high, battle, health, quit]: ")
    if choice == 'list':
        display_characters(character_list, 1)

    elif choice == 'heroes':
        display_characters(character_list, 2)

    elif choice == 'villains':
        display_characters(character_list, 3)

    elif choice == 'search':
        name = input("\nPlease enter name: ")
        index = find_character(character_list, name)
        if index != -1:
            print("All about " + name + " ==> ", end='')
            if character_list[index][2] == 'h':
                print("HERO")
            elif character_list[index][2] == 'v':
                print("VILLAIN")
            elif character_list[index][2] == 'n/a':
                print("N/A")

            print("\nSecret identity: " + character_list[index][1])
            print("\nBattles fought: " + str(character_list[index][3]))
            print("\t> No won:" + "{0:>5}".format(character_list[index][4]))
            print("\t> No lost:" + "{0:>4}".format(character_list[index][5]))
            print("\t> No drawn:" + "{0:>3}".format(character_list[index][6]))
            print("\nCurrent health: " + str(character_list[index][7]) + '%')
        else:
            print('\n' + name + ' is not found in character (heroes and villains) list.')

    elif choice == 'reset':
        reset_health = input('Please enter character who\'s health you would like to reset: ')
        if reset_health != 'Wonder Woman' or 'Batman' or 'The Joker' or 'Superman' or 'Catwoman' or 'Aquaman' or 'Iron Man' or 'Hulk' or 'Thanos':
            print('Character not found in list of characters')
            reset_health = input('Please enter character who\'s health you would like to reset: ')
        elif reset_health == 'Wonder Woman':
            character_list[0][7] = '100'
        elif reset_health == 'Batman':
            character_list[1][7] = '100'
        elif reset_health == 'The Joker':
            character_list[2][7] = '100'
        elif reset_health == 'Superman':
            character_list[3][7] = '100'
        elif reset_health == 'Catwoman':
            character_list[4][7] = '100'
        elif reset_health == 'Aquaman':
            character_list[5][7] = '100'
        elif reset_health == 'Iron Man':
            character_list[6][7] = '100'
        elif reset_health == 'Hulk':
            character_list[7][7] = '100'
        elif reset_health == 'Thanos':
            character_list[8][7] = '100'
        print(display_characters(character_list, 1))

    elif choice == 'health':
        sort_by_health(character_list)
                       

#elif choice == 'reset':

#elif choice == 'add':

#elif choice == 'remove':

#elif choice == 'high':

#elif choice == 'battle':

#elif choiice == 'health':

#elif choice == 'quit':

    

    


