class ResultTable:
    def __init__(self):
        self.result_table = {}

    def register_info_set_as_terminal(self, info_set, payoff_list):
        self.result_table[info_set] = payoff_list

    def check_if_terminal(self, info_set):
        return self.result_table.__contains__(info_set)

    def get_payoff(self, info_set):
        return self.result_table[info_set]
