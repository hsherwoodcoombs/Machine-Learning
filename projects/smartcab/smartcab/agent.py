import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator

class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""

    def __init__(self, env):
        # sets self.env = env, state = None, next_waypoint = None, and a default color
        super(LearningAgent, self).__init__(env)
        self.color = 'red'  # override color
        # simple route planner to get next_waypoint
        self.planner = RoutePlanner(self.env, self)
        # TODO: Initialize any additional variables here

    def reset(self, destination=None):
        self.planner.route_to(destination)
        # TODO: Prepare for a new trip; reset any variables here, if required

    def update(self, t):
        # Gather inputs
        # # from route planner, also displayed by simulator
        self.next_waypoint = self.planner.next_waypoint()
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)

        # TODO: Update state
        self.state = self.next_waypoint, inputs['light']
        # self.state = self.next_waypoint, (inputs['oncoming'] == None or inputs['light'] == 'green')

        # TODO: Select action according to your policy
        # Define actions
        actions = [None, 'forward', 'left', 'right']

        # QUESTION 1- select random action
        action = random.choice(actions)

        # Execute action and get reward
        reward = self.env.act(self, action)

        # TODO: Learn policy based on state, action, reward


        # Formatting ----- My own formatting style --------
        # Reformated updates in environment.act
        # print "LearningAgent.update():\n\tdeadline = {}\n\tinputs = {}\n\taction = {}\n\treward = {}\n".format(deadline, inputs, action, reward)  # [debug]
        # print "Deadline:\t\t{}".format(deadline)

def run():
    """Run the agent for a finite number of trials."""

    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent)  # create agent

    # QUESTION 1- sets `enforce_deadline` to `False`
    e.set_primary_agent(a, enforce_deadline=True)  # specify agent to track
    # NOTE: You can set enforce_deadline=False
    # while debugging to allow longer trials

    # Now simulate it
    # # create simulator (uses pygame when display=True, if available)
    sim = Simulator(e, update_delay=0.01, display=False)
    # NOTE: To speed up simulation,
    # reduce update_delay and/or set display=False

    # run for a specified number of trials
    sim.run(n_trials=100)

    print "Finished!"
    # NOTE: To quit midway, press Esc or close pygame window,
    # or hit Ctrl+C on the command-line


if __name__ == '__main__':
    run()