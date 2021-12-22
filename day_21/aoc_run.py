class Game:
    outcome_rates = {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1
    }

    def __init__(self, player_1_score, player_1_index, player_2_score, player_2_index, instances, player_1_turn, depth):
        self.player_1_score = player_1_score
        self.player_1_index = player_1_index
        self.player_2_score = player_2_score
        self.player_2_index = player_2_index
        self.instances = instances
        self.player_1_turn = player_1_turn
        self.children = []
        self.winners = 0

        self.depth = depth + 1
        self.play_round()

    def play_round(self):
        if self.depth > 50:
            print(self.player_1_score)
            print(self.player_2_score)
            print(self.instances)
        if self.player_1_turn:
            for outcome in self.outcome_rates.keys():
                player_1_new_index = ((self.player_1_index + outcome - 1) % 10) + 1
                player_1_new_score = self.player_1_score + player_1_new_index
                if player_1_new_score < 21:
                    self.children.append(Game(player_1_new_score,
                                              player_1_new_index,
                                              self.player_2_score,
                                              self.player_2_index,
                                              self.instances * self.outcome_rates[outcome],
                                              not self.player_1_turn,
                                              self.depth
                                              ))
                else:
                    self.winners += self.instances * self.outcome_rates[outcome]
        else:
            for outcome in self.outcome_rates.keys():
                player_2_new_index = ((self.player_2_index + outcome - 1) % 10) + 1
                player_2_new_score = self.player_2_score + player_2_new_index
                if player_2_new_score < 21:
                    self.children.append(Game(player_2_new_score,
                                              player_2_new_index,
                                              self.player_2_score,
                                              self.player_2_index,
                                              self.instances * self.outcome_rates[outcome],
                                              not self.player_1_turn,
                                              self.depth
                                              ))
                else:
                    self.winners += self.instances * self.outcome_rates[outcome]


def part_1(raw_input):
    # Simply simulate the game
    player_1_position = int(raw_input[0][-1])
    player_1_score = 0

    player_2_position = int(raw_input[1][-1])
    player_2_score = 0

    dice = 0
    dice_rolls = 0
    player_1_turn = True
    while True:
        roll = 0
        for i in range(3):
            roll += dice + 1
            dice += 1
            dice = dice % 100
            dice_rolls += 1
        if player_1_turn:
            player_1_position += roll
            player_1_position = ((player_1_position - 1) % 10) + 1
            player_1_score += player_1_position
        else:
            player_2_position += roll
            player_2_position = ((player_2_position - 1) % 10) + 1
            player_2_score += player_2_position

        if player_1_score >= 1000:
            return player_2_score * dice_rolls
        elif player_2_score >= 1000:
            return player_1_score * dice_rolls

        player_1_turn = not player_1_turn


def part_2(raw_input):
    player_1_position = int(raw_input[0][-1])
    player_2_position = int(raw_input[1][-1])

    print('This could take a minute or two...')

    outcome_rates = {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1
    }

    player_wins = {1: 0, 2: 0}

    def recurse(player_1_score: int, player_1_index: int, player_2_score: int, player_2_index: int, player_1_turn: bool, instances: int):
        if player_1_turn:
            for outcome in outcome_rates.keys():
                new_index = ((player_1_index + outcome - 1) % 10) + 1
                new_score = player_1_score + new_index
                if new_score > 20:
                    player_wins[1] += instances * outcome_rates[outcome]
                else:
                    recurse(new_score, new_index, player_2_score, player_2_index, False, instances * outcome_rates[outcome])
        else:
            for outcome in outcome_rates.keys():
                new_index = ((player_2_index + outcome - 1) % 10) + 1
                new_score = player_2_score + new_index
                if new_score > 20:
                    player_wins[2] += instances * outcome_rates[outcome]
                else:
                    recurse(player_1_score, player_1_index, new_score, new_index, True, instances * outcome_rates[outcome])

    recurse(0, player_1_position, 0, player_2_position, True, 1)

    if player_wins[1] > player_wins[2]:
        return player_wins[1]
    else:
        return player_wins[2]


def part_2_surplus(raw_input):

    # Yikes! No simulation this time
    # Need to use math instead
    # Rolling 3d3 gives these outcome rates
    outcome_rates = {
        3: 1,
        4: 3,
        5: 6,
        6: 7,
        7: 6,
        8: 3,
        9: 1
    }

    # Running one dictionary per player of indexes on the game board
    # Each entry has another dictionary with score values as keys, and number of players as values

    player_1 = {}
    player_1_updates = {}
    player_2 = {}
    player_2_updates = {}

    rounds = 0
    rounds_winner = {}

    # Generate indexes

    for i in range(1, 11):
        player_1[i] = {}
        player_1_updates[i] = {}
        player_2[i] = {}
        player_2_updates[i] = {}
        for j in range(21):
            player_1[i][j] = 0
            player_1_updates[i][j] = 0
            player_2[i][j] = 0
            player_2_updates[i][j] = 0

    # Add starting positions

    player_1_position = int(raw_input[0][-1])
    player_1[player_1_position][0] += 1
    player_2_position = int(raw_input[1][-1])
    player_2[player_2_position][0] += 1

    def roll_for_player(player, to_update):
        winners = 0
        # Reset update dictionary
        for index in to_update.keys():
            for score in to_update[i].keys():
                to_update[index][score] = player[index][score]

        for index in player.keys():
            for score in player[index].keys():
                if player[index][score] > 0:
                    # If there are players at an index, use outcome rates to see where their spawn will end up
                    players = player[index][score]
                    for outcome in outcome_rates.keys():
                        new_index = ((index + outcome - 1) % 10) + 1
                        # Place the new players at their appropriate score
                        new_score = score + new_index
                        if new_score > 20:
                            winners += outcome_rates[outcome] * players
                        else:
                            to_update[new_index][new_score] = player[new_index][new_score] + (outcome_rates[outcome] * players)
                    # New universes are created so destroy the current one
                    to_update[index][score] = 0

        # Update main dictionary
        for index in to_update.keys():
            for score in to_update[index].keys():
                player[index][score] = to_update[index][score]

        # Update winners
        rounds_winner[rounds] = winners
        if rounds > 1:
            rounds_winner[rounds] -= rounds_winner[rounds - 1]

    def other_player_rolls(player):
        for index in player.keys():
            for score in player[index].keys():
                player[index][score] *= 27

    def has_players(player):
        for index in player.keys():
            for score in player[index].keys():
                if player[index][score] > 0:
                    return True
        return False

    player_1_turn = True
    count = 0
    player_1_has_players = True
    player_2_has_players = True
    while True:
        if count > 21:
            break
        if not player_1_has_players and not player_2_has_players:
            break
        rounds += 1
        if player_1_turn and player_1_has_players:
            roll_for_player(player_1, player_1_updates)
            player_1_has_players = has_players(player_1)
            other_player_rolls(player_2)
        elif not player_1_turn and player_2_has_players:
            roll_for_player(player_2, player_2_updates)
            player_2_has_players = has_players(player_2)
            other_player_rolls(player_1)

        player_1_turn = not player_1_turn
        count += 1

    # for key in player_1.keys():
    #     for k in player_1[key].keys():
    #         if player_1[key][k] > 0:
    #             print(key)
    #             print('\t' + str(k) + ': ' + str(player_1[key][k]))

    print('Winners:')
    winners_total_1 = 0
    winners_total_2 = 0

    for key in rounds_winner.keys():
        # print(str(key) + ': ' + str(rounds_winner[key]))
        if key > 1:
            if key & 2 == 0:
                winners_total_2 += rounds_winner[key]
            else:
                winners_total_1 += rounds_winner[key]

    print(winners_total_1)
    print(winners_total_2)
    # player 1 score
    # 23146309267265110365
    # 444356092776315
    # player 2 score
    # 334873133751086061921
    # 341960390180808
