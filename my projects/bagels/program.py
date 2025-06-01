import random
class bagels:
    def __init__(self,number_max_size=3,maximum_chances=10):
        self.number_max_size=number_max_size
        self.maximum_chances=maximum_chances
        self.random_number=self.get_random_number()

    def get_random_number(self):
        lst=[i for i in range(10)]
        random.shuffle(lst)

        random_number=''
        for i in range(self.number_max_size):
            random_number+=str(lst[i])

        return random_number

    def main_function(self):

        print("""DISCLAIMER:  In Bagels, a deductive logic game, you 
                must guess a secret three-digit number 
                based on clues. The game offers one of 
                the following hints in response to your guess: 
                “Pico” when your guess has a correct digit in the 
                wrong place, “Fermi” when your guess has a correct 
                digit in the correct place, and “Bagels” if your guess 
                has no correct digits. You have 10 tries to guess the 
                secret number \n\n\n\n""")

        x=0
        while(x<=self.maximum_chances):
            x+=1
            print(f"\nremaining chances --> {self.maximum_chances-x+1}")
            user_input=input(f"enter only {self.number_max_size} digits: ")

            if(len(user_input)!=self.number_max_size):
                print("WRONG INPUT")
                return
            
            hints=self.getHints2(user_input,str(self.random_number))
            if hints==1:
                print("RIGHT ANSWER, BRAIN TRAINER!")
                return
            else:
                print(hints)
            
        print("BETTER LUCK NEXT TIME\nBEFORE TRYING NEXT, FIRST TRAIN YOUR BRAIN")
        print(f"the actual answer is {self.random_number}")


    def getHints(self,user_input,random_number):

        if(user_input==random_number):
            return 1

        hints=[]

        for i in range(len(user_input)):
            if user_input[i]==random_number[i]:
                hints.append("fermi")
                break
        
        for i in user_input:
            if i in random_number:
                hints.append("pico")
                break
        
        if len(hints)==0:
            hints.append("bagels")

        return " ".join(hints)
    

    def getHints2(self,user_input,random_number):

        if(user_input==random_number):
            return 1

        hints=[]

        for i in range(len(user_input)):
            if user_input[i]==random_number[i]:
                hints.append(f"{user_input[i]} in the correct position")
            elif user_input[i] in random_number:
                hints.append(f"{user_input[i]} in the wrong position")

        if len(hints)==0:
            hints.append("none of the numbers are correct")

        return " ".join(hints)
            
Bagels=bagels(3)
Bagels.main_function()
