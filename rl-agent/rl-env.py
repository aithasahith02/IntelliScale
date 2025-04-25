class DummyEnv:
    """
    A dummy reinforcement learning environment.
    """
    def decide_action(self, state):
        cpu, memory, request_rate = state
        
        if cpu > 0.75 or memory > 0.8:
            return "scale_up"
        elif cpu < 0.2 and memory < 0.3:
            return "scale_down"
        else:
            return "no_action"

