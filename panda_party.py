# Exercise : Panda Party

# Description: 
# This program runs a Panda Game between 3 players in which you start with a number of starting stones 
# that is chosen by the user. The players then have the option to take 1-3 stones if possible until 
# there's 0 stones left. The person who's turn is after the person who chooses the last stone is the 
# winner and the other two players are the losers of the game.

#This function determines if the game is over by checking if the # of stones is 0
#parameters - curr_stones an int that represents the # of stones
#returns - True if the game is over and there are 0 stones left and False if the game is still going
def is_game_over(curr_stones):
    if curr_stones == 0:
        return True
    return False

#This function takes the name of the current player and returns the name of the next player which will be the opposite name
#parameters - curr_player a string that represents the name of the current player; player_1, player_2, and player_3, strings that 
#represent the name of the players
#returns - the  name of the next player
def next_player(curr_player, player_1, player_2, player_3):
    if curr_player == player_1:
        return player_2
    elif curr_player == player_2:
        return player_3
    return player_1

#This function prompts the user to enter the name of the first player
#parameters - n/a
#returns - the name of the Panda who will start the game
def get_first_player():
    user_choice = input("Who should begin the game? ")
    return user_choice

#This function prompts the user to enter the name of the second player
#parameters - n/a
#returns - the name of the Panda who will be the second player
def get_second_player():
    user_choice = input("Who will the next player be? ")
    return user_choice

#This function prompts the user to enter the name of the last player
#parameters - n/a
#returns - the name of the Panda who will be the last player
def get_third_player():
    user_choice = input("Who will the last player be? ")
    return user_choice

#This function displays to the user how many stones are left and prompts the user to take 1-3 stones if there are 3 or more stones left and #if there are less than 3 stones left it alters how much the user can take
#parameters - curr_player a string that represents the current player; curr_stones an in that represents the number of stones currently left
#returns the number of stones the current player chooses to take
def get_choice(curr_player, curr_stones):
    print("{}, it is your turn.".format(curr_player))
    take_choice = int(input("There are {} stones left in the pile. How many will you take? ".format(curr_stones)))
    #sets a max possible number of stones the user can take
    if curr_stones < 3:
        max_take = curr_stones
    else:
        max_take = 3
    #doing a nested loop to make sure that if the user is warned that they have taken too much or little before and choose to do it again,
    #it will still display the right error message.
    while take_choice < 1 or take_choice > max_take:
        while take_choice < 1:
            print("You must take at least one stone.")
            take_choice = int(input("There are {} stones left in the pile. How many will you take? ".format(curr_stones)))
        while take_choice > max_take:
            print("You cannot take more than {} stones.".format(max_take))
            take_choice = int(input("There are {} stones left in the pile. How many will you take? ".format(curr_stones)))
    return take_choice

def main():
    print("Welcome to the panda party!")
    start_stones = int(input("How many stones would you like to start the game with? "))
    start_player = get_first_player()
    player_1 = start_player
    player_2 = get_second_player()
    player_3 = get_third_player()
    replay_ans = 1
    #sets a loop in case the user wants to replay with the same names and starting count
    while replay_ans == 1:
        print()
        num_stones = start_stones
        curr_player = start_player
        #sets up the loop for players to take their turns until the game ends
        while is_game_over(num_stones) == False:
            num_modifier = get_choice(curr_player, num_stones)
            num_stones -= num_modifier
            curr_player = next_player(curr_player, player_1, player_2, player_3)
            print()
        print("Game over!")
        #winner is set to curr_player which would be the person to come after the person before them took the last stone before the loop   
        #ended
        winner = curr_player
        loser_1 = next_player(curr_player, player_1, player_2, player_3)
        loser_2 = next_player(loser_1, player_1, player_2, player_3)
        print("{} wins! {} and {} lose!".format(winner, loser_1, loser_2))
        replay_ans = int(input("Would you like to replay the game from the beginning? Enter 1 for yes or 2 for no: "))

main()