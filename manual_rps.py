import random


def play():
    score = {'computer wins' : 0, 'player wins' : 0}
    ####---- this function asks the computer for a choice
    
    
    def get_comp_choice():
        choices = ['rock', 'scissors', 'paper']
        comp_choice = random.choice(choices)
        return comp_choice
    
    

    ####---- this function asks the user for a choice

    def get_user_choice():
        user_choice = input( '\n' 'choose between rock, scissors, paper:  ')
        while True:
            if user_choice == 'paper' or user_choice == 'scissors' or user_choice == 'rock':
                return user_choice
            else: 
                
                print('\n' 'Invalid input')
                break


    
    ####---- this function finds the winner
    def get_winner(comp_choice , user_choice):
        ####--- draw:
        
        if comp_choice == user_choice:
            print('Draw')
            
        ####--- computer wins:
        elif (user_choice == 'rock' and comp_choice == 'paper') or (user_choice == 'paper' and comp_choice == 'scissors') or (user_choice == 'scissors' and comp_choice == 'rock'):

            print('\n' 'computer choice is {} and your choice is {}, you ve lost '.format(comp_choice, user_choice))
            score['computer wins'] +=1 
            

        elif (user_choice == 'paper' and comp_choice == 'rock') or (user_choice == 'scissors' and comp_choice == 'paper') or (user_choice == 'rock' and comp_choice == 'rock'):
            print('\n' 'computer choice is {} and your choice is {}, you ve WON!!!'.format(comp_choice, user_choice))
            
            score['player wins'] +=1 
            

        else:
            pass
    print(score)
    

    get_winner(comp_choice = get_comp_choice(), user_choice = get_user_choice() )

# get_winner(get_comp_choice(), get_user_choice())


def replay (num_times):
     for i in range(num_times):
        
        if i < num_times:
            play()
        else:
            exit()

 
replay(num_times = 20)