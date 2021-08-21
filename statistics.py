class Statistics:

    algorithm_name = ""
    max_iterations = 0
    max_space = 0

    def reset_statistics(self):
        self.max_iterations = 0
        self.max_space = 0

    def print_statistics(self):
        print("algorithm:\t" + self.algorithm_name)
        print("max iterations:\t" + str(self.max_iterations))
        print("max space:\t" + str(self.max_space))