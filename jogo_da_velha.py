def marker_selection(counter):
    if counter % 2 == 0:
        marker = "O"
    else:
        marker = "X"
    return marker


def player_input(marker):
    valid_inputs = ("a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3")

    while True:
        new_input = input(
            f"Jogador '{marker}', digite uma posição válida para marcar: "
        ).lower()
        if new_input in valid_inputs:
            return new_input
        elif (new_input[1] + new_input[0]) in valid_inputs:
            return new_input[1] + new_input[0]


def player_move(position_dict, new_input, marker):
    position_dict[new_input[0]][new_input[1]] = marker
    return position_dict


def update_view(position_dict):
    game_view = print(
        f"""
    1     2     3
A:  {position_dict['a']['1']}  |  {position_dict['a']['2']}  |  {position_dict['a']['3']}
  _____|_____|_____
B:  {position_dict['b']['1']}  |  {position_dict['b']['2']}  |  {position_dict['b']['3']}
  _____|_____|_____
C:  {position_dict['c']['1']}  |  {position_dict['c']['2']}  |  {position_dict['c']['3']}
       |     |
"""
    )

    return game_view


def win_check(position_dict, marked_positions):
    if len(marked_positions) == 9:
        print("Fim de Jogo!")
        return False
    for i in ("a", "b", "c"):
        if (
            position_dict[i]["1"]
            == position_dict[i]["2"]
            == position_dict[i]["3"]
            != " "
        ):
            print("Fim de Jogo!")
            return False
    for j in ("1", "2", "3"):
        if (
            position_dict["a"][j]
            == position_dict["b"][j]
            == position_dict["c"][j]
            != " "
        ):
            print("Fim de Jogo!")
            return False
    if (
        position_dict["a"]["1"]
        == position_dict["b"]["2"]
        == position_dict["c"]["3"]
        != " "
    ):
        print("Fim de Jogo!")
        return False
    elif (
        position_dict["c"]["1"]
        == position_dict["b"]["2"]
        == position_dict["a"]["3"]
        != " "
    ):
        print("Fim de Jogo!")
        return False
    else:
        return True


print("Welcome to Gramma's Game!")
counter = 1
position_dict = {
    "a": {"1": " ", "2": " ", "3": " "},
    "b": {"1": " ", "2": " ", "3": " "},
    "c": {"1": " ", "2": " ", "3": ""},
}
continue_game = True
update_view(position_dict)
marked_positions = []

while continue_game:
    marker = marker_selection(counter)
    new_input = player_input(marker)
    if new_input in marked_positions:
        continue
    else:
        marked_positions.append(new_input)
    position_dict = player_move(position_dict, new_input, marker)
    update_view(position_dict)
    continue_game = win_check(position_dict, marked_positions)
    counter = counter + 1
