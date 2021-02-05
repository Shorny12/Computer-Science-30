# RPG Continuous Game Play
# Zhixiang Wang
# CS 30 AM class
# Date Created: February 4, 2021
# Date Modified: February 5, 2021

# Set active to True
active = True

# Command list for use
use = ['Use', 'u']
# Command list for run
run = ['Run', 'r']
# Command list for fight
fight = ['fight', 'f']
# Command list for backpack
bag = ['Bag', 'b']
# Command list for use
use = ['Use', 'u']
# Command list to quit the game
quit = ['Quit', 'q']
# Command list to move to foward
foward = ['Foward', 'F']
# Command list to move to back
back = ['Back', 'B']
# Command list to move to left
left = ['Left', 'L']
# Command list to move to right
right = ['Right', 'R']

# print the title
print('''\n\t\t\t>>> The Castle <<<\n\n\t\t\tExplore The Castle!!!\n\n''')
# Choose Direction
print('\nYou can choose one of the following directions:')
# Choose action
print('* Foward (F)\n* Back (B)\n* Left (L)\n* Right (R)')
print('\nYou can choose one of the following actions:')
print('* Use (u)\n* Run (r)\n* Fight (f)\n* View Bag (b)\n* quit (q)')

# while active for direction
while active:
    while True:
        action = '* Action >>>'
        action = input(action)
        # action if go foward
        if action in foward:
            print("\n Go foward")
        # action if go back
        elif action in back:
            print("\n Go back")
        # action if go left
        elif action in left:
            print("\n Go left")
        # action if go right
        elif action in right:
            print("\n Go right")
        # action if use
        elif action in use:
            print('\n- There is nothing you can use in your bag')
        # action if fight
        elif action in fight:
            print('\n Start fight')
        # action if run
        elif action in run:
            print("\n- You ran out of this room.")
        # action if view bag
        elif action in bag:
            print('Map:\n* To show you the way')
            print('The bandoge:\n* Use to restore health"')
            input('\n- Press Enter to go back to the fight.\n>>> ')
        # action if quit
        elif action in quit:
            print('\n\n\t\t\t  >>> Game Over <<<\n\n')
            break
        else:
            # print a message for unexpected command
            print('\n- Invalid command.')

    if active:
        action = input("""\n- Press Enter to play again.\n
        -Press s to stop game.\n>>>""")
        if action in quit:
            # Break the loop and stop the game
            print('\n\n\t\t\t  >>> Stop Game <<<\n\n')
            active = False
