def solution(source, destination):

    chessboard = [[], [], [], [], [], [], [], []]

    identifier_counter = 0

    for i in range(8):
        for j in range(8):
            chessboard[i].append([identifier_counter, (j, i)])
            identifier_counter += 1

    source_x = 0
    source_y = 0

    destination_x = 0
    destination_y = 0

    for array in chessboard:

        for element in array:

            if element[0] == source:

                source_x = element[1][0]
                source_y = element[1][1]

            elif element[0] == destination:

                destination_x = element[1][0]
                destination_y = element[1][1]

    difference_x = abs(destination_x - source_x)
    difference_y = abs(destination_y - source_y)

    if difference_x >= difference_y:
        primary = difference_x
        secondary = difference_y
    else:
        primary = difference_y
        secondary = difference_x

    primary -= 1

    moves_array = [[3, 2], [2, 1, 4], [3, 2, 3, 2], [2, 3, 2, 3, 4], [3, 4, 3, 4, 3, 4], [4, 3, 4, 3, 4, 5, 4],
                   [5, 4, 5, 4, 5, 4, 5, 6]]

    needed_subset = moves_array[primary]

    if source == destination:
        return 0
    else:
        shortest_moves = needed_subset[secondary]

    return shortest_moves

print(solution(0,0))