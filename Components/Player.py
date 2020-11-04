import random
import math
from functools import reduce


def sigmoid(num):
    return 1 / (1 + math.e ** (-num))


class Player:
    def __init__(self, index):
        self.action_table = {}
        self.index = index
        self.name = None
        self.update_flag = (index > 0)

    def set_name(self, string):
        self.name = string

    def get_id(self):
        return self.index

    def add_action_function(self, info_set):
        choice_num = info_set.get_choice_count()
        self.action_table[info_set] = [5, [1/choice_num] * choice_num, -1]

    def change_action_function(self, info_set, new_dict):
        self.action_table[info_set][1] = new_dict

    def choose_action(self, info_set):
        print("Choosing action: Player", self.index, "at node", info_set.index)
        action_dict = self.action_table[info_set][1]
        rand = random.random()
        ans = 0
        for action in action_dict:
            if rand <= action:
                self.action_table[info_set][2] = ans
                return ans
            ans += 1
            rand -= action

    def update_prior(self, payoff):
        if not self.update_flag:
            return
        print("Updating: Player", self.index, "updating")
        delta = []
        for key, value in self.action_table.items():
            if not value[2] == -1:
                print(key.index, ": ", value, " ")
                num = self.action_table[key][0]
                weight = [num * i for i in value[1]]
                weight[value[2]] += sigmoid(payoff) * 3
                total = sum(weight)
                new_prob = [i / total for i in weight]
                self.action_table[key][0] = num + 1
                delta += [(self.action_table[key][1][i] - new_prob[i]) * num / 2 for i in range(len(new_prob))]
                self.action_table[key][1] = new_prob
                self.action_table[key][2] = -1
        if delta:
            return reduce(lambda a, b: math.sqrt(a ** 2 + b ** 2), delta)
        else:
            return 1.0

    def __str__(self):
        string = "'"
        for key, value in self.action_table.items():
            string += str(key.index) + ": "
            string += str(value) + " "
        return string

    def __eq__(self, other):
        return self.index == other.get_id()
