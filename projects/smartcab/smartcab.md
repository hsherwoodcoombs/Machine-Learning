# Project Report

## Introduction
The smartcab problem poses a goal for which the agent should learn an optimal policy in navigating the road grid while obeying traffic rules, avoiding accidents, and reaching a passengers destination in the allotted time. The implementation of the policy will be based on the rewards and penalties the agent receives from the actions it takes. 

### Markov Decision Processes (MDPs)

The MDP can be treated as a 5-tuple, where:
- S is the set of states
- A is the set of actions
- P returns the state of transition probabilities

The state space of the search problem is defined the agents environment and the agents own parameter locations. The upper bound on the state space for the original 6x8 grid can be represented by 

We can treat the the smartcab environment as **stochastic** or **deterministic** because the environment does posses some inherent randomness and actions do not always produce the same result. For these reasons, I believe the environment is more stochastic than deterministic. That parameter values that are *not* predictable are traffic lights and traffic (locations of other agents). This *stochastic* environment is more complex and requires more learning. With many states and a stochastic environment, a good model can be difficult to produce without training a the learner itself. That is, to return non-deterministic transition probabilities, state-action pairs must be learned.


The environment can also be described as **partially observable**, as opposed to fully observable. The cab needs to apply the unpredictable nature of what it encounters (storing it to memory) to make good optimal decisions in addition to what it senses; the optimal decision can benefit by information it acquired from the past. An example could be the case of a collision. If a cab observed long lights on a certain road. Knowing this could be applied to make the best decision. (This could be somewhat preconcerted in the smartcab model but would apply to a more realistic one.)

We can also describe the environment as **benign**. In the model there are is no ulterior motive (like in the prisoners dilemma) or even with real cab drivers who fight for passengers. 


The state space of our model **discrete** when a deadline is enforced. Because the smartcab is limited to a finite number of actions it can take before a trial is aborted it acts in a discrete environment. It can be noted that in a more realistic model, the state space would more likely be **continuous**.


We can therefor sum up the smartcab model with the attributes:
**Partially observable, stochastic, discrete, multi agent, benign **

A continuous state space iUsing reinforcement learning and  implementing a Markov decision process, an optimal reward function can be maximized through iteration. 

The MDP for the smartcab is s

The smartcab receives a  positive reward 
• For each successfully completed trip  

• A smaller reward for each action it executes successfully that obeys traffic rules  

The smartcab recieves a negative reward
• For any incorrect action  

• A larger penalty for any action that violates traffic rules or causes an accident with another vehicle


## Observe what you see with the agent's behavior as it takes random actions. Does the smartcab eventually make it to the destination? Are there any other interesting observations to note?

- Yes, the smartcab eventually does make it to the destination, however it is not optimum but rather completely random.
- By changing `enforce_deadline` to False the smartcab actually makes it to the destination every trial. The caveat is that when it exceeds the allotted time, the deadline begins counting backwards. 

For example in first trial, my smartcab did not reach its destination within the deadline of 20 moves. When it exceeded its 20th move, the deadline accumulated onto the negative parameter. So when, the smartcab did reach the destination it made it in -17. That would be 17 most **past** what it is allowed.

## What states have you identified that are appropriate for modeling the smartcab and environment? Why do you believe each of these states to be appropriate for this problem?

- States that are appropriate to model the smartcab include `oncoming`, `left`, `right` and `light`
	- `Oncoming` describes traffic conditions. Valid elements within `oncoming` are left, right, and forward
- States within output are not relevant to the prediction process.

### How many states in total exist for the smartcab in this environment? Does this number seem reasonable given that the goal of Q-Learning is to learn and make informed decisions about each state? Why or why not?

## QUESTION: What changes do you notice in the agent's behavior when compared to the basic driving agent when random actions were always taken? Why is this behavior occurring?


## Report the different values for the parameters tuned in your basic implementation of Q-Learning. For which set of parameters does the agent perform best? How well does the final driving agent perform?


## Does your agent get close to finding an optimal policy, i.e. reach the destination in the minimum possible time, and not incur any penalties? How would you describe an optimal policy for this problem?