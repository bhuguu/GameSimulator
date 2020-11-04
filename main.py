from Components import *


player_list = PlayerList()
info_set_table = InfoSetTable()
result_table = ResultTable()
player_list.register_new_player(1)
player_list.set_players_name(0, "god")

# init map
player_list.register_new_player(2)
god = player_list.get_player_by_index(0)
player_list.set_players_name(1, "alice")
player_list.set_players_name(2, "bob")
alice = player_list.get_player_by_index(1)
bob = player_list.get_player_by_index(2)
node0 = Node(info_set_table, god)
node1 = Node(info_set_table, alice)
node2 = Node(info_set_table, alice)
node3 = Node(info_set_table, god)
node4 = Node(info_set_table, god)
node5 = Node(info_set_table, bob)
node6 = Node(info_set_table, bob)
node7 = Node(info_set_table, god)
node8 = Node(info_set_table, god)
node9 = Node(info_set_table, alice)
node10 = Node(info_set_table, alice)
node11 = Node(info_set_table, god)
node12 = Node(info_set_table, god)
node13 = Node(info_set_table, god)
node14 = Node(info_set_table, god)
node0.connect(node1)
node0.connect(node2)
node1.connect(node3)
node2.connect(node4)
node1.connect(node5)
node2.connect(node6)
node5.connect(node7)
node6.connect(node8)
node5.connect(node9)
node6.connect(node10)
node9.connect(node11)
node10.connect(node12)
node9.connect(node13)
node10.connect(node14)
node5.merge(node6)
node3.set_as_terminal([4, 4], result_table)
node4.set_as_terminal([-1, 4], result_table)
node7.set_as_terminal([5, 2], result_table)
node8.set_as_terminal([0, 2], result_table)
node11.set_as_terminal([3, 3], result_table)
node12.set_as_terminal([-1, 3], result_table)
node13.set_as_terminal([1, -5], result_table)
node14.set_as_terminal([0, -5], result_table)


# Do not change
# init information sets
for info_set in info_set_table.get_info_sets():
    if not result_table.check_if_terminal(info_set):
        info_set.count()
        info_set.create_action_list()

# edit nature
god.change_action_function(node0.get_info_set(), [0.9, 0.1])

# Do not change
# run the game
while True:
    current_node = node0
    while not result_table.check_if_terminal(current_node.get_info_set()):
        current_node = current_node.move()
    payoff = result_table.get_payoff(current_node.get_info_set())
    delta = 0
    for j in range(2):
        delta += player_list.get_player_by_index(j + 1).update_prior(payoff[j])
    if delta < 0.001:
        break

for i in range(5):
    current_node = node0
    while not result_table.check_if_terminal(current_node.get_info_set()):
        print("Player: " + str(current_node.info_set.player.index) + " Node: " + str(current_node.info_set.index))
        current_node = current_node.move()
    print("Player: " + str(current_node.info_set.player.index) + " Node: " + str(current_node.info_set.index))
    payoff = result_table.get_payoff(current_node.get_info_set())
    for j in range(2):
        player_list.get_player_by_index(j + 1).update_prior(payoff[j])

# show result
for j in range(2):
    print(player_list.get_player_by_index(j + 1))
