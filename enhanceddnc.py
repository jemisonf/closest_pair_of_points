from math import pow, sqrt
from statistics import median
from sys import argv

from lib import read_inputs, write_outputs


# Computes the closest pairs and the distance between these two points
# Returns a tuple of a float and a list of tuples of tuples representing pairs
# of points
def closest_pair(points):
    if len(points) == 2:
        result = list()
        result.append(tuple(points))
        final_result = (compute_distance(points[0], points[1]), result)
        return final_result
    if len(points) == 3:
        distances = {
            (points[0], points[1]): compute_distance(points[0], points[1]),
            (points[1], points[2]): compute_distance(points[1], points[2]),
            (points[0], points[2]): compute_distance(points[0], points[2])
        }
        min_distance = min(distances.values())
        result = list(filter(
            lambda it: distances[it] == min_distance,
            distances.keys()
        ))
        final_result = (min_distance, result)
        return final_result

    median_x = median(map(lambda it: it[0], points))
    left_half = list(filter(lambda it: it[0] <= median_x, points))
    right_half = list(filter(lambda it: it[0] > median_x, points))
    closest_left = closest_pair(left_half)
    closest_right = closest_pair(right_half)
    delta = min([closest_left[0], closest_right[0]])
    middle_band = list(filter(
        lambda it: median_x - delta <= it[0] <= median_x + delta,
        points
    ))
    # Sort by y coord
    middle_band.sort(key=lambda it: it[1])
    # Call closest cross pair
    closest_cross = closest_cross_pair(middle_band, delta)
    new_min = min(delta, closest_cross[0])
    result = (new_min, [])
    for section in [closest_left, closest_right, closest_cross]:
        if section[0] == new_min:
            for pair in section[1]:
                if not any(x in result[1] for x in [pair, (pair[1], pair[0])]):
                    result[1].append(pair)
    return result


# Compute the closest cross-pair
# points should be sorted by y-coordinate in ascending order
# Returns a tuple with first item being the shortest distance and the second
# item being the list of tuples with distance equal to the shortest distance
def closest_cross_pair(points, delta):
    dm = delta
    for i in range(len(points) - 1):
        j = i + 1
        while(j < len(points) and points[j][1] - points[i][1] <= delta):
            d = compute_distance(points[0], points[1])
            dm = min(d, dm)
            j = j + 1
    possible_pairs = list((x, y) for x in points for y in points)
    closest_pairs = list(filter(
        lambda it: compute_distance(it[0], it[1]) <= dm and it[0] != it[1],
        possible_pairs
    ))
    final_result = (dm, closest_pairs)
    return final_result


# Compute the distance between two points
def compute_distance(point_a, point_b):
    return sqrt(
        pow(point_b[0] - point_a[0], 2) + pow(point_b[1] - point_a[1], 2)
    )


if __name__ == "__main__":
    try:
        inputs = read_inputs(argv[1])
    except IndexError:
        exit("No input file was provided")
    result = closest_pair(inputs)
    write_outputs('enhanceddnc-output.txt', result[0], result[1])
