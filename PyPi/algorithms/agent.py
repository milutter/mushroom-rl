import logging


class Agent(object):
    """
    This class implements the functions to evaluate the Q-function
    of the agent and drawing actions.
    """
    def __init__(self, approximator, policy, **params):
        """
        Constructor.

        # Arguments
            approximator (object): the approximator of the Q function;
            policy (object): the policy to use.
        """
        self.approximator = approximator
        self.policy = policy
        self.mdp_info = dict()
        self.logger = logging.getLogger('logger')
        self.params = params

        self._next_action = None

    def initialize(self, mdp_info):
        for k, v in mdp_info.iteritems():
            self.mdp_info[k] = v

    def draw_action(self, state):
        """
        Returns the action to execute. It is the action returned by the policy
        or the pre-set action.

        # Arguments
            state (np.array): the state where the agent is.

        # Returns
            the action to be executed.
        """
        if self._next_action is None:
            return self.policy(state, self.approximator)
        else:
            action = self._next_action
            self._next_action = None
            return action