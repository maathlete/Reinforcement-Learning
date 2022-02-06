# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 15:55:43 2022

@author: aaaro
"""

import os

from generalized_transportation_mdp import TransportationMDP

def valueIteration(mdp):
    
    # initialize
    
    V = {} # sate -> Vopt(state)
    
    for state in mdp.states():
        
        V[state] = 0
        
    def Q(state, action):
        
        return(sum(prob*(reward + mdp.discount()*V[newState]) \
                   for newState, prob, reward in mdp.succProbReward(state, action)))
               
    while True:
        
        # compute the new values (newV) given the old values (V)
        
        new_V = {}
        
        for state in mdp.states():
            
            if mdp.isEnd(state):
                
                new_V[state] = 0
                
            else:
                
                new_V[state] = max(Q(state, action) for action in mdp.actions(state)) 
                
            
        # check for convergence
        
        if max(abs(V[state] - new_V[state]) for state in mdp.states()) < 1e-10:
            
            break
        
        V = new_V
        
        # read out policy
        
        pi = {}
        
        for state in mdp.states():
            
            if mdp.isEnd(state):
                
                pi[state] = 'none'
                
            else:
                pi[state] = max((Q(state, action), action) for action in mdp.actions(state))[1]
        
        
        os.system('clear')
        
        print('{:15} {:15} {:15}'.format('s', 'V(s)', 'pi(s)'))
        
        for state in mdp.states():
            
            print('{:15} {:15} {:15}'.format(state, V[state], pi[state]))
            
        input()
        

mdp = TransportationMDP(N = 10)

valueIteration(mdp)
