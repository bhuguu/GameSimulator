class InfoSetTable:
    def __init__(self):
        self.info_set_num = 0
        self.info_set_inverse_table = {}

    def register_new_info_set(self, info_set):
        self.info_set_inverse_table[self.info_set_num] = info_set
        self.info_set_num += 1
        return self.info_set_num - 1

    def get_info_sets(self):
        return self.info_set_inverse_table.values()

    def remove_info_set(self, info_set_id):
        del self.info_set_inverse_table[info_set_id]
