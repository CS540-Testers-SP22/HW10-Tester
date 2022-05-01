import gym
import pickle
import random
import numpy as np
import time



def default_Q_value():
    return 0


def evaluate_frozen_lake(Q_table, EPSILON, visualize=False):
    total_reward = 0
    random.seed(1)
    np.random.seed(1)
    env = gym.envs.make("FrozenLake-v1")
    env.reset(seed=1)
    env.action_space.np_random.seed(1)
    
    for i in range(100):
        obs = env.reset()
        done = False
        while done == False:
            if random.uniform(0,1) < EPSILON:
                action = env.action_space.sample()
            else:
                prediction = np.array([Q_table[(obs,i)] for i in range(env.action_space.n)])
                action =  np.argmax(prediction)
            obs,reward,done,info = env.step(action)
            total_reward += reward
            if visualize:
                env.render()
                time.sleep(.01)
    score = total_reward/100
    return score


def test_Q_learning(visualize = False):
    print("Test 1 out of 4. Visualization is "+ str(visualize))
    loaded_data = pickle.load(open('Q_TABLE.pkl', 'rb'))
    Q_table = loaded_data[0]
    EPSILON = loaded_data[1]
    score = evaluate_frozen_lake(Q_table,EPSILON, visualize = False)
    points = 0
    true_iterations = 0
    iterations = 0
    
    EPISODES =  20000
    EPSILON_DECAY = .999
    
    while(EPSILON <= 1):
        true_iterations += 1
        EPSILON = EPSILON / EPSILON_DECAY
        
    EPSILON = loaded_data[1]
    while(iterations != EPISODES):
        iterations += 1
        EPSILON = EPSILON / EPSILON_DECAY
    
    if(iterations == EPISODES and round(EPSILON,12) == 1):
        points += 15
    else:
        print("Returned " + str(iterations) + " iterations, instead of " + str(true_iterations))
        print("EPSILON == " + str(EPSILON) + " instead of 1")
        print("")
        return points
        
    if score >= 0.6:
        points += 30
    elif score >= 0.4:
        points += 15 
        
    print("Q Learning on FrozenLake-v1:")
    print("Average episode-reward over 100 episodes is " + str(score))
    print(str(points)  +" out of 45 points received.")
    print("")
    return points


def test_Q_learning2(visualize = False):
    print("Test 2 out of 4. Visualization is "+ str(visualize))
    loaded_data = pickle.load(open('Q_TABLE.pkl', 'rb'))
    Q_table = loaded_data[0]
    EPSILON = loaded_data[1]
    score = evaluate_frozen_lake(Q_table,EPSILON,visualize = False)
    points = 0
    true_iterations = 0
    iterations = 0
    
    EPISODES =  10000
    EPSILON_DECAY = .999
    
    while(EPSILON <= 1):
        true_iterations += 1
        EPSILON = EPSILON / EPSILON_DECAY
        
    EPSILON = loaded_data[1]
    while(iterations != EPISODES):
        iterations += 1
        EPSILON = EPSILON / EPSILON_DECAY
    
    if(iterations == EPISODES and round(EPSILON,12) == 1):
        points += 15
    else:
        print("Returned " + str(iterations) + " iterations, instead of " + str(true_iterations))
        print("EPSILON == " + str(EPSILON) + " instead of 1")
        print("")
        return points
        
    if score >= 0.6:
        points += 30
    elif score >= 0.4:
        points += 15 
        
    print("Q Learning2 on FrozenLake-v1:")
    print("Average episode-reward over 100 episodes is " + str(score))
    print(str(points)  +" out of 45 points received.")
    print("")
    return points

def test_Q_learning3(visualize = False):
    print("Test 3 out of 4. Visualization is "+ str(visualize))
    loaded_data = pickle.load(open('Q_TABLE.pkl', 'rb'))
    Q_table = loaded_data[0]
    EPSILON = loaded_data[1]
    score = evaluate_frozen_lake(Q_table,EPSILON,visualize = False)
    points = 0
    true_iterations = 0
    iterations = 0
    
    EPISODES =  5000
    EPSILON_DECAY = .999
    
    while(EPSILON <= 1):
        true_iterations += 1
        EPSILON = EPSILON / EPSILON_DECAY

    EPSILON = loaded_data[1]
    while(iterations != EPISODES):
        iterations += 1
        EPSILON = EPSILON / EPSILON_DECAY
    
    if(iterations == EPISODES and round(EPSILON,12) == 1):
        points += 15
    else:
        print("Returned " + str(iterations) + " iterations, instead of " + str(true_iterations))
        print("EPSILON == " + str(EPSILON) + " instead of 1")
        print("")
        return points
        
    if score >= 0.6:
        points += 30
    elif score >= 0.4:
        points += 15 
        
    print("Q Learning3 on FrozenLake-v1:")
    print("Average episode-reward over 100 episodes is " + str(score))
    print(str(points)  +" out of 45 points received.")
    print("")
    return points

def test_Q_learning4(visualize = False):
    print("Test 4 out of 4. Visualization is "+ str(visualize))
    loaded_data = pickle.load(open('Q_TABLE.pkl', 'rb'))
    Q_table = loaded_data[0]
    EPSILON = loaded_data[1]
    score = evaluate_frozen_lake(Q_table,EPSILON,visualize = False)
    points = 0
    true_iterations = 0
    iterations = 0
    
    EPISODES =  50000
    EPSILON_DECAY = .999
    
    while(EPSILON <= 1):
        true_iterations += 1
        EPSILON = EPSILON / EPSILON_DECAY
        
    EPSILON = loaded_data[1]
    while(iterations != EPISODES):
        iterations += 1
        EPSILON = EPSILON / EPSILON_DECAY
    
    if(iterations == EPISODES and round(EPSILON,12) == 1):
        points += 15
    else:
        print("Returned " + str(iterations) + " iterations, instead of " + str(true_iterations))
        print("EPSILON == " + str(EPSILON) + " instead of 1")
        print("")
        return points
        
    if score >= 0.6:
        points += 30
    elif score >= 0.4:
        points += 15 
        
    print("Q Learning4 on FrozenLake-v1:")
    print("Average episode-reward over 100 episodes is " + str(score))
    print(str(points)  +" out of 45 points received.")
    print("")
    return points



if __name__ == "__main__":
    total_points = 0
    total_extra_credit_points = 0
    print('-' * 40)
    try:
        # Testing 20,000 episodes
        total_points += test_Q_learning()
        
        # Testing 10,000 episodes
        total_points += test_Q_learning2()
        
        # Testing 5,000 episodes
        total_points += test_Q_learning3()
        
        #Testing 50,000 episodes
        total_points += test_Q_learning4()
    except Exception as e:
        print(e)
