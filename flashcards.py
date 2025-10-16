from typing import List,Tuple
import os
import json
import random
import time
from icecream import ic

from rich.console import Console
from rich.panel import Panel
from rich.table import Table


def is_all_done(flashcards_data):
    #empty dict evauluate to false
    not_done = flashcards_data['not_done']
    
    not_done_has_items = bool(not_done)

    if not_done_has_items:
        return False
    else:
        return True


def is_flashcardsdata_valid(flashcards_data):

    #3 keys
    #
    #settings 3 keys

    
    
    #does not follow condition of corect data
    #if key in both  
    #if 
    #if 
    pass

def get_all_desc(flashcards_data):

    done_words = list(flashcards_data['done'].keys())
    not_done_words = list(flashcards_data['not_done'].keys())

    all_desc = []

    for word in done_words:
        lis_desc = flashcards_data['done'][word]['descriptions']
        for desc in lis_desc:
            all_desc.append(desc)

    for word in not_done_words:
        lis_desc = flashcards_data['not_done'][word]['descriptions']
        for desc in lis_desc:
            all_desc.append(desc)


    #flashcards_data['done']
    #for lis_desc in word_data
    #
    #
    #lis_done_descriptions:List[List[str]] = [done_words[word]['description'] for word in done_words]
    #lis_not_done_desc:List[List[str]] = [not_done_words[word]['description'] for word in not_done_words]
    #
    #
    #
    #
    #
    #
    #for desc in lis_not_done_desc.extend(lis_done_descriptions):
    #    all_desc.append(desc)
    #
    ##later maybe all must be unique

    return all_desc

def save_data(flashcards_data,full_json_path):

    with open(full_json_path,'w') as f:
        json.dump(flashcards_data,f)

def is_inp_valid():
    #does it follow conditions of correct inp

    pass

def display_options(cur_word:str,
                    enu_options:List[Tuple[int, str]],
                    max_correct_user_choices:int,
                    options_indent:int,
                    console
                    )->None:
    
    print('\n\n\n\n\n\n')
    print(f"There are (1 to {max_correct_user_choices}) correct descriptions")
    

    table = Table(style="black bold")

    table.add_column(cur_word,style="yellow2")

    for i,option in enu_options:
        if i%2==0:
            table.add_row(f"{str(i).ljust(3)}: {option}")
        else:
            table.add_row(f"{str(i).ljust(3)}: {option}")

    console.print(table)


def is_inp_correct(valid_inp:List[int],
                   enu_options:List[Tuple[int, str]],
                   lis_correct_desc:List[str]
                    )->bool:
    
    choices_numbers = valid_inp 

    lis_choice_desc:List[str]= []

    for choice_number in choices_numbers:

        choosen_option:List[str] = [option for i,option in enu_options
                        if choice_number==i]  
         
        if len(choosen_option)!=1:
            ic(choosen_option) 
            raise ValueError
        if not(isinstance(choosen_option[0],str)): 
            ic(choosen_option)
            ic(not(isinstance(choosen_option[0],str)))
            raise ValueError

        choosen_option_str:str = choosen_option[0]
        lis_choice_desc.append(choosen_option_str)

    if set(lis_choice_desc)==set(lis_correct_desc):
        return True
    else:
        return False


def handle_json_not_exist(full_json_path):
        


    with open(full_json_path,'w') as f:

        print('you have forgotten to write the falshcards or written them in wrong file')


        json_data_when_no_file = {
            'settings':{ 
                'n_user_options':10,
                'max_correct_user_choices':3,
                'options_indent':3
            },
            'not_done':{
                "keyword/name of thing": 
                    {
                    'descriptions':["description of thing"," other description of the thing","other description of th thing","this list must have items such that n==1 or n>1"],
                    'counter':"this should be 0 when the card is done and this should be an integer",
                    'group':"this we have now as A for all cards"
                    },
                "first example cat":
                    {
                    'descriptions':["it is an animal","it has 4 legs","it likes meat","it is an pet"],
                    'counter':3,
                    'group':"A"
                    }
            },
            'done':{
                "keyword/name of thing": 
                    {
                    'descriptions':["description of thing"," other description of the thing","other description of th thing","this list must have items such that n==1 or n>1"],
                    'counter':"this should be 0 when the card is done and this should be an integer",
                    'group':"this we have now as A for all cards"
                    },
                "first example cat":
                    {
                    'descriptions':["it is an animal","it has 4 legs","it likes meat","it is an pet"],
                    'counter':0,
                    'group':"A"
                    }
            }
        }

        json.dump(json_data_when_no_file,f)

    raise FileNotFoundError("go and edit the json that was created")

def get_correct_json_path():
    #get the path of this code
    cur_full_path:str = os.path.abspath(__file__)

    # manipulate the path to the correct file name for the _data.json file
    not_ready_json_path = cur_full_path
    print(cur_full_path)

    while not_ready_json_path[-1]!=".":
        not_ready_json_path= not_ready_json_path[:-1]
    not_ready_json_path= not_ready_json_path[:-1]    # we do it one more time to remove "."

    #now we have an correct file name
    full_json_path = not_ready_json_path + "_data.json"
    return full_json_path

def get_valid_input(cur_word,
                    enu_options,
                    max_correct_user_choices,
                    options_indent,
                    console       
                    ) -> str | List[int]:
    
    def is_every_char_a_number(user_inp_lis:List[str]) -> bool:
        
        if ("".join(user_inp_lis)).isnumeric()==True:
            return True #every char is a number
        else:
            return False #there is digits that are not numbers


        

    while True:
        display_options(cur_word,
                        enu_options,
                        max_correct_user_choices,
                        options_indent,
                        console)
        
        user_inp:str = input("write your choice: ") #" EXIT 22 2 2 2 " 
        user_inp = user_inp.lower()            #-> " exit 22 2 2 2 " 
        user_inp = user_inp.strip()           #-> "exit 22 2 2 2"
        user_inp_lis:List[str] = user_inp.split()   #-> ["exit","22","2","2","2"]

        if is_every_char_a_number(user_inp_lis): 

            user_inp_lis:List[str] #every char is an number
            #We process user input (string->list(strings))
            user_inp_lis_int:List[int] = [int(user_choice) for user_choice in user_inp_lis]
            
            #here we have an list of strings
            if len(user_inp_lis_int)>max_correct_user_choices or len(user_inp_lis_int)==0:
                print(f'you choose:{len(user_inp_lis_int)} number of options. Highest number of choices is {max_correct_user_choices}, lowest number of choices are 1')
                print('')
                input("press enter to try again")

            else:
                ############ check if all choices are valid choices 
                # there should not be one choice that is not on the screen
                all_choices_are_valid = True
                #we try to falsify
                lis_options:List[int] = [option[0] for option in enu_options]
                for user_choice in user_inp_lis_int:
                    if user_choice not in lis_options:
                        all_choices_are_valid=False

                if all_choices_are_valid:
                    return user_inp_lis_int
                else:
                    print("you picked an option that is not on the screen")
                    input("press enter to try again")
                    #goto start of loop
                ######################################

        elif not(is_every_char_a_number(user_inp_lis)):
            #here sting has letters in it
            user_inp_lis:List[str]
            user_inp_exit:str = ""

            for user_choice in user_inp_lis:
                if user_choice=='exit':
                    user_inp_exit = 'exit'

            if user_inp_exit == 'exit':
                return user_inp_exit
            else:
                print("you only can have letters if these letters are exit")
                print("try again but use numbers or exit if you wnat to exit")
                input("press enter to try again")
                #goto start of loop

        else: raise ValueError("just in case somthing went wrong here")

def CLI_flashcards():

    console = Console()

    full_json_path = get_correct_json_path()
    
    if os.path.exists(full_json_path)==False:
        handle_json_not_exist(full_json_path)

    #now we have card data

    with open(full_json_path,'r') as f:
        flashcards_data = json.load(f)

    is_flashcardsdata_valid(flashcards_data)

    #get all the descriptions
    all_desc = get_all_desc(flashcards_data)


    #get settings parameters
    n_user_options = flashcards_data['settings']['n_user_options']
    max_correct_user_choices = flashcards_data['settings']['max_correct_user_choices']
    options_indent = flashcards_data['settings']['options_indent']
    

    #later maybe in loop generate new cards and delete cards in CLI

    while True:

        #### we get options,correct  
        #here we get the cards that should be displayed
        cur_word = random.choice(list(flashcards_data['not_done'].keys()))#we chose one correct word out of the not done cards
        
        #we get the correct descriptions that should be included in options
        all_correct_desc = flashcards_data['not_done'][cur_word]['descriptions']    #we take the correct description for this card
        n_correct_desc = random.randint( 1, min(len(all_correct_desc),max_correct_user_choices) ) #  here we can not have more correcct description then amount of descriptions AND no more then the max that is specified by the user
        lis_correct_desc:List[str] = random.sample(list(all_correct_desc),n_correct_desc)                  #here we have an list of all descriptions/choices that are correct

        n_false_desc = n_user_options-n_correct_desc
        if n_false_desc+n_correct_desc!=n_user_options:raise valueError()
        
        for choice in range(1000):
            lis_false_desc:List[str] = random.sample(all_desc, n_false_desc)
            options:List[str] = lis_false_desc + lis_correct_desc
            
            #This to make sure we have an valid set of options
            if len(set(options))==len(options):
                break
            if choice>900:
                raise ValueError('somthing wrong here')

        enu_options:List[Tuple[int, str]] 
        enu_options = list(enumerate(options, start=1))


        #get valid input from the user
        valid_inp: List[int] | str 
        valid_inp = get_valid_input(cur_word,enu_options,max_correct_user_choices,options_indent,console)
        
        


        ###################### do things based on user input
        if valid_inp=='exit':
            # -----------------------------------------------------
            save_data(flashcards_data,full_json_path)
            break 
            # -----------------------------------------------------

        elif is_inp_correct(valid_inp,enu_options,lis_correct_desc):
            # -----------------------------------------------------
            print('\n\n\n')
            table = Table()
            table.add_column("correct",style="yellow2")
            table.add_row(f"word: {cur_word}\n")
            table.add_row("These are the options you choose:")
            table.add_row('---')
            for correct_desc in lis_correct_desc:
                table.add_row(correct_desc)
            table.add_row('---\n')
            table.add_row(f'These are all the correct descriptions for {cur_word}')
            table.add_row('---')
            for desc in flashcards_data['not_done'][cur_word]['descriptions']:
                table.add_row(desc)
            table.add_row('---')
            console.print(table)
            input("press enter to continue")

            #decrement the counter because user guessed right
            flashcards_data['not_done'][cur_word]['counter'] -= 1
            if flashcards_data['not_done'][cur_word]['counter']==0:
                flashcards_data['done'][cur_word] = flashcards_data['not_done'].pop(cur_word)

            # -----------------------------------------------------

        else:
            # -----------------------------------------------------
            
            #get choosen options
            lis_choosen_options = []
            for choice_number in valid_inp:
                for number,option in enu_options:
                    if choice_number==number:
                        lis_choosen_options.append(option)

            print('\n\n\n')
            table = Table()
            table.add_column("not correct",style="yellow2")
            table.add_row(f"word: {cur_word}\n")
            table.add_row("These are the options you choose:")
            table.add_row('---')
            for choice in lis_choosen_options:
                table.add_row(choice)
            table.add_row('---\n')

            table.add_row(f'These are the correct options for {cur_word}:')
            table.add_row('---')
            for correct_desc in lis_correct_desc:
                table.add_row(correct_desc)
            table.add_row('---\n')

            table.add_row(f'These are all the correct descriptions for {cur_word}')
            table.add_row('---')
            for desc in flashcards_data['not_done'][cur_word]['descriptions']:
                table.add_row(desc)
            table.add_row('---\n')
            console.print(table)

            input("press enter to continue")

            #edit in data
            if flashcards_data['not_done'][cur_word]['counter']<5:
                flashcards_data['not_done'][cur_word]['counter'] += 1
            # -----------------------------------------------------
            
        if is_all_done(flashcards_data):
                print("we done now")
                save_data(flashcards_data,full_json_path)
                break





def main():

    CLI_flashcards()


if __name__=='__main__':
    main()