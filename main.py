# this function get our first map from our file
def get_first_map():
    """
    no argument
    get first map in t=0 from file with name "map.init" and return the map
    """

    map_file = open("map.init")
    global first_map
    first_map = map_file.read()
    first_map = first_map.replace("â–‘", "░")
    first_map = first_map.replace("â–ˆ", "█")

    return first_map


# this function calculate length and width of our map
# this func need global var "first_map" so we should run "get_first_map" first
def calculate_edges_of_map(map_world):
    """
       get the map calculate the edges in variables "length" & "width" return this two in a list
       so index[0]= length & index[1]= width
    """

    map_world = first_map

    counter_rows = 0
    for i in range(len(map_world)):
        if map_world[i] != "░" and map_world[i] != "█":
            counter_rows += 1

    #   last line does not have "space or new line" so width+1
    global rows
    rows = counter_rows + 1
    global columns
    columns = len(map_world) // rows

    return [rows, columns]


# make a matrix from any cells in map
# this func need global var "width" so we should run "calculate_edges_of_map" first
def matrix_of_map(map_world):
    """
    :param map_world
    :return: matrix of map
    """
    map_world = str(map_world)
    map_list = map_world.split()

    matrix_of_map = []
    for i in range(rows):
        matrix_of_map.append(list(map_list[i]))

    return matrix_of_map


# make list from 8 neighbors of one cell in map
def neighbors_cell(row, column, matrix_map):
    """
    :param matrix_map: map of world
    :param row: row of cell in matrix_map
    :param column: column of cel in matrix_map
    :return: a list contain neighbors of a cell with special index them
    """

    neighbors_list = []

    if row == 0 and column == 0:
        # * 0
        # 1 2

        # 0
        neighbors_list.append(matrix_map[row][column + 1])
        # 1
        neighbors_list.append(matrix_map[row + 1][column])
        # 2
        neighbors_list.append(matrix_map[row + 1][column + 1])

    elif row == rows - 1 and column == 0:
        # 0 2
        # * 1

        # 0
        neighbors_list.append(matrix_map[row - 1][column])
        # 1
        neighbors_list.append(matrix_map[row][column + 1])
        # 2
        neighbors_list.append(matrix_map[row - 1][column + 1])

    elif row == 0 and column == columns - 1:
        # 0 *
        # 2 1

        # 0
        neighbors_list.append(matrix_map[row][column - 1])
        # 1
        neighbors_list.append(matrix_map[row + 1][column])
        # 2
        neighbors_list.append(matrix_map[row + 1][column - 1])

    elif row == rows - 1 and column == columns - 1:
        # 2 0
        # 1 *

        # 0
        neighbors_list.append(matrix_map[row - 1][column])
        # 1
        neighbors_list.append(matrix_map[row][column - 1])
        # 2
        neighbors_list.append(matrix_map[row - 1][column - 1])

    elif row == 0 and 0 < column < columns - 1:
        # 0 * 1
        # 2 3 4

        # 0
        neighbors_list.append(matrix_map[row][column - 1])
        # 1
        neighbors_list.append(matrix_map[row][column + 1])
        # 2
        neighbors_list.append(matrix_map[row + 1][column - 1])
        # 3
        neighbors_list.append(matrix_map[row + 1][column])
        # 4
        neighbors_list.append(matrix_map[row + 1][column + 1])

    elif row == rows - 1 and 0 < column < columns - 1:
        # 0 1 2
        # 3 * 4

        # 0
        neighbors_list.append(matrix_map[row - 1][column - 1])
        # 1
        neighbors_list.append(matrix_map[row - 1][column])
        # 2
        neighbors_list.append(matrix_map[row - 1][column + 1])
        # 3
        neighbors_list.append(matrix_map[row][column - 1])
        # 4
        neighbors_list.append(matrix_map[row][column + 1])

    elif 0 < row < rows - 1 and column == columns - 1:
        # 0 1
        # 2 *
        # 3 4

        # 0
        neighbors_list.append(matrix_map[row - 1][column - 1])
        # 1
        neighbors_list.append(matrix_map[row - 1][column])
        # 2
        neighbors_list.append(matrix_map[row][column - 1])
        # 3
        neighbors_list.append(matrix_map[row + 1][column - 1])
        # 4
        neighbors_list.append(matrix_map[row + 1][column])

    elif 0 < row < rows - 1 and column == 0:
        # 0 1
        # * 2
        # 3 4

        # 0
        neighbors_list.append(matrix_map[row - 1][column])
        # 1
        neighbors_list.append(matrix_map[row - 1][column + 1])
        # 2
        neighbors_list.append(matrix_map[row][column + 1])
        # 3
        neighbors_list.append(matrix_map[row + 1][column])
        # 4
        neighbors_list.append(matrix_map[row + 1][column + 1])
    else:
        # 0 1 2
        # 3 * 4
        # 5 6 7

        # 0
        neighbors_list.append(matrix_map[row - 1][column - 1])
        # 1
        neighbors_list.append(matrix_map[row - 1][column])
        # 2
        neighbors_list.append(matrix_map[row - 1][column + 1])
        # 3
        neighbors_list.append(matrix_map[row][column - 1])
        # 4
        neighbors_list.append(matrix_map[row][column + 1])
        # 5
        neighbors_list.append(matrix_map[row + 1][column - 1])
        # 6
        neighbors_list.append(matrix_map[row + 1][column])
        # 7
        neighbors_list.append(matrix_map[row + 1][column + 1])

    return neighbors_list


# count number of live neighbors
def live_neighbors(list_of_neighbors):
    """
    :param list_of_neighbors: a list from neighbors of a cell
    :return: number of live neighbors
    """
    list_of_neighbors = list(list_of_neighbors)
    return list_of_neighbors.count("█")


#  define that a cell should die or live and if cell need change
def to_be_or_not_to_be(map_matrix, map_str=get_first_map()):
    """

    :param map_matrix:
    :param map_str:
    :return:
    """
    new_map_matrix = map_matrix.copy()
    for row in range(rows):
        for column in range(columns):

            if map_matrix[row][column] == "█":
                if live_neighbors(neighbors_cell(row, column, matrix_of_map(map_str))) < 2 or live_neighbors(
                        neighbors_cell(row, column, matrix_of_map(map_str))) > 3:
                    new_map_matrix[row][column] = "░"

            if map_matrix[row][column] == "░":
                if live_neighbors(neighbors_cell(row, column, matrix_of_map(map_str))) == 3:
                    new_map_matrix[row][column] = "█"

    return new_map_matrix


# change matrix of map to a regular(str) map
def matrix_to_string(matrix):
    """

    :param matrix:
    :return:
    """
    strr = ""
    for row in range(rows):
        for column in range(columns):
            strr += matrix[row][column]
        strr += "\n"
    return strr


import os


# clear the screen
def clear():
    os.system('cls')if os.name == "nt" else os.system('clear')


# start our world!!!!
def hello_world():
    map_world = get_first_map()
    calculate_edges_of_map(get_first_map())

    while True:
        map_world = matrix_to_string(to_be_or_not_to_be(matrix_of_map(map_world), map_world))
        clear()
        print(map_world)


hello_world()
