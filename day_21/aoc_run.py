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
    # Yikes! No simulation this time
    # Need to use math instead


    return 0
