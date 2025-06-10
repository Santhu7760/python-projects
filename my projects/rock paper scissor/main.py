#  input required
# user should enter rock or paper or scissor

# output
# winner of the game

import random

class Main:

    def game(self):
        user_win_count=0
        computer_win_count=0
        draw_count=0
        count=0

        choices=['rock','paper','scissor']

        user_input=input("enter rock or paper or scissor (x for exit): ")

        while user_input.lower()!='x':

            computer_choice=random.randint(0,2)

            if(user_input.lower() not in choices):
                print("wrong input")
                break

            if user_input.lower()==choices[computer_choice]:
                print(f"user choice: {choices[computer_choice].upper()} and computer choice: {choices[computer_choice].upper()} \nRESULT IS: DRAW!\n")
                draw_count+=1

            elif(user_input.lower()==choices[0] and computer_choice==1):
                print(f"user choice: {user_input.upper()} and computer choice: {choices[computer_choice].upper()} \nRESULT IS: COMPUTER WON!\n")
                computer_win_count+=1

            elif(user_input.lower()==choices[1] and computer_choice==0):
                print(f"user choice: {user_input.upper()} and computer choice: {choices[computer_choice].upper()} \nRESULT IS: USER WON!\n")
                user_win_count+=1

            elif(user_input.lower()==choices[1] and computer_choice==2):
                print(f"user choice: {user_input.upper()} and computer choice: {choices[computer_choice].upper()} \nRESULT IS: COMPUTER WON!\n")
                computer_win_count+=1

            elif(user_input.lower()==choices[2] and computer_choice==1):
                print(f"user choice: {user_input.upper()} and computer choice: {choices[computer_choice].upper()} \nRESULT IS: USER WON!\n")
                user_win_count+=1

            elif(user_input.lower()==choices[0] and computer_choice==2):
                print(f"user choice: {user_input.upper()} and computer choice: {choices[computer_choice].upper()} \nRESULT IS: USER WON!\n")
                user_win_count+=1

            elif(user_input.lower()==choices[2] and computer_choice==0):
                print(f"user choice: {user_input.upper()} and computer choice: {choices[computer_choice].upper()} \nRESULT IS: COMPUTER WON!\n")
                computer_win_count+=1
            
            else:
                print("SOMETHING WRONG!")
                break

            count+=1
            user_input=input("enter rock or paper or scissor (x for exit): ")
        if count!=0:
            print(f"the winning percentage: USER -> {round((user_win_count/count)*100)} %   COMPUTER -> {round((computer_win_count/count)*100)} %   DRAW -> {round((draw_count/count)*100)}")



main=Main()
main.game()    