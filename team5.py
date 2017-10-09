
team_name = 'The name the team gives to itself' # Only 10 chars displayed.
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    if len(their_history)== 1:
        return 'b'
    if 'b' in their_history[-1]:
        return 'c'
    else:
        return 'b'
    if 'c' in their_history[-1]:
        return 'b'
    else:
        return 'b'
    