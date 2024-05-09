# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
# Initialize the Q-table with zeros
Q = {
    ('R', 'R'): 0, ('R', 'P'): 0, ('R', 'S'): 0,
    ('P', 'R'): 0, ('P', 'P'): 0, ('P', 'S'): 0,
    ('S', 'R'): 0, ('S', 'P'): 0, ('S', 'S'): 0
}

# Define the available actions (Rock, Paper, Scissors)
actions = ['R', 'P', 'S']

# Define the learning rate
alpha = 0.1

# Define the discount factor
gamma = 0.9

# Define the exploration rate
epsilon = 0.1


# Function to select an action based on epsilon-greedy policy
def choose_action(state):
    if random.random() < epsilon:
        return random.choice(actions)
    else:
        return max(actions, key=lambda a: Q[state, a])

# Function to update the Q-values based on the reward received
def update_Q(state, action, reward, next_state):
    best_next_action = max(actions, key=lambda a: Q[next_state, a])
    Q[state, action] += alpha * (reward + gamma * Q[next_state, best_next_action] - Q[state, action])

def player(prev_play, opponent_history=[]):
    if prev_play == '':
        guess = random.choice(actions)
    else:
        guess = choose_action(prev_play)
    next_state = guess, random.choice(actions)
    if guess == next_state[1]:
            reward = 0  # Tie
    elif (guess == 'R' and next_state[1] == 'S') or (guess == 'P' and next_state[1] == 'R') or (guess == 'S' and next_state[1] == 'P'):
            reward = 1  # Win
    else:
            reward = -1  # Lose

    if prev_play!='':
        update_Q(prev_play, guess, reward, next_state[1])

    return guess
