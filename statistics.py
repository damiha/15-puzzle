class Statistics:

    def __init__(self, algorithm_name):
        self.algorithm_name = algorithm_name
        self.max_iterations = 0
        self.max_space = 0

    def reset_statistics(self):
        self.max_iterations = 0
        self.max_space = 0

    def print(self):
        print("algorithm:\t" + self.algorithm_name)
        print("max iterations:\t" + str(self.max_iterations))
        print("max space:\t" + str(self.max_space) + " bytes")
