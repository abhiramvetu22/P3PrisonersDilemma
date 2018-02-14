team_name = 'Phang'
strategy_name = 'Copy'
strategy_description = 'Collude first round. Take their play from last round and use that move'
    
def move(my_history, their_history, my_score, their_score):
    from random import randint
    rollOne = randint(1,100)
    rollTwo = randint(1,100)
    if rollTwo == rollOne:
        rollTwo = randint(1,100)
    if len(my_history)==0: # It's the first round; collude.
        return 'c'
    elif their_history[-1]=='b' and my_history.len() == rollOne or my_history.len() == rollTwo:
        return 'b' #A random betrayal regardless of their last move @ two random rounds
    elif their_history[-1]=='b':
        return 'b'
    elif their_history[-1]=='c':
        return 'c' #If their last move was collude, then collude
    else:
        return 'b' # otherwise betray.