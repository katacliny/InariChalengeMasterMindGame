from colorama import Fore, init


def title():
    
    title = Fore.WHITE + """ 
 ██     ██ ███████ ██       ██████  ██████  ███    ███ ███████     ████████  ██████      ███    ███  █████  ███████ ████████ ███████ ██████  ███    ███ ██ ███    ██ ██████  """ + Fore.RED + """    ▒███████▒ ▒█████   ███▄ ▄███▓ ▄▄▄▄    ██▓  
""" + Fore.WHITE + """ ██     ██ ██      ██      ██      ██    ██ ████  ████ ██             ██    ██    ██     ████  ████ ██   ██ ██         ██    ██      ██   ██ ████  ████ ██ ████   ██ ██   ██ """ + Fore.RED + """    ▒ ▒ ▒ ▄▀░▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ ▓██▒
""" + Fore.WHITE + """ ██  █  ██ █████   ██      ██      ██    ██ ██ ████ ██ █████          ██    ██    ██     ██ ████ ██ ███████ ███████    ██    █████   ██████  ██ ████ ██ ██ ██ ██  ██ ██   ██ """ + Fore.RED + """    ░ ▒ ▄▀▒░ ▒██░  ██▒▓██    ▓██░▒██▒ ▄██▒██▒
""" + Fore.WHITE + """ ██ ███ ██ ██      ██      ██      ██    ██ ██  ██  ██ ██             ██    ██    ██     ██  ██  ██ ██   ██      ██    ██    ██      ██   ██ ██  ██  ██ ██ ██  ██ ██ ██   ██ """ + Fore.RED + """      ▄▀▒   ░▒██   ██░▒██    ▒██ ▒██░█▀  ░██░
""" + Fore.WHITE + """  ███ ███  ███████ ███████  ██████  ██████  ██      ██ ███████        ██     ██████      ██      ██ ██   ██ ███████    ██    ███████ ██   ██ ██      ██ ██ ██   ████ ██████  """ + Fore.RED + """    ▒███████▒░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓░██░
                                                                                                                                                                            """ + Fore.RED + """    ░▒▒ ▓░▒░▒░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒░▓  
                                                                                                                                                                            """ + Fore.RED + """    ░░▒ ▒ ░ ▒  ░ ▒ ▒░ ░  ░      ░▒░▒   ░  ▒ ░
                                                                                                                                                                            """ + Fore.RED + """    ░ ░ ░ ░ ░░ ░ ░ ▒  ░      ░    ░    ░  ▒ ░
                                                                                                                                                                            """ + Fore.RED + """        ░ ░        ░ ░         ░    ░       ░  
                                                                                                                                                                            """ + Fore.RED + """         ░                                  ░     
   
    """
    
    print(title)


def intro():
    text = """
        The year 2150 passes and a terrible epidemic strikes humanity, 
        a Chinese laboratory has spread the strain of a deadly virus which 
        turns its host into a creature without intelligence that only thinks
        about eating ... eating human brains. After more than 3 years of 
        investigation the police have managed to reach the laboratory where 
        they hide the antidote, the last barrier is to decipher the entry key, 
        you have to win a game of master mind but be careful, the attempts are 
        limited, an error could free hundreds ZOMBIES and destroy the last hope 
        of humanity.
    """

    print(Fore.YELLOW + text)

    global show_intro
    show_intro = False


def help_log():
    help: str = f"""
    
        MasterMind is a logic board game from the 70’s in which you have to co-
        rrectly guess a random secret code in a determined number of guesses.

        This game can be played by two players, the code-maker and the co-
        de-breaker.

        • The code-maker creates the secret combination, composed by a se-
        quence of 4 colored pegs

        • The code-breaker makes a series of guesses, each guess composed in
        the same way by 4 colores pegs. After each guess, the code-maker gives

        feedback to the code-breaker to see how close you got to the real se-
        cret code.

        Each feedback is composed of two numbers, represented by white pegs

        and black pegs, and they tell you how your guess and the secret combina-
        tion compare. Black pegs tell you how many pegs of your guess you have

        correct in color and position, and white pegs tell you how many pegs of
        your guess you have correct in color but not in the proper position.
        
        The list of possible colors is {str(list(Colors.__members__.keys()))} you only can use a 4 colors combination.
        
        The possible commands are:

            --exit This comand will exist the program.
    
    """

    print(help)
    input("Press any key to continue.")
