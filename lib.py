# read an input file and return a list of tuples
# where each tuple is an (x, y) pair


def read_inputs(filename):
    with open(filename) as f:
        contents = f.read()
    contents_list = contents.strip().splitlines()
    points_list = list()
    for pair in contents_list:
        coords = tuple(int(coord) for coord in pair.split(' '))
        points_list.append(coords)
    return points_list

# input is the filename, the distance as a float
# and a list of tuples of tuples,
# where each tuple of tuples is a pair of (x, y) points like ((1, 0), (0, 1))


def write_outputs(filename, distance, points):
    with open(filename, "w") as f:
        f.write(f'{distance}\n')
        for pair_points in points:
            f.write(f'{pair_points[0][0]} {pair_points[0][1]} {pair_points[1][0]} {pair_points[1][1]}\n')
