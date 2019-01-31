from math import pow, sqrt
from statistics import median

import lib


test_data = [(1, 2), (5, 2), (8, 9), (10, 20)]
test_data_2 = [(1, 2), (3, 4)]
test_data_3 = [(1, 2), (3, 4), (5, 6)]


def closest_pair(points):
    if len(points) == 2:
        return points
    if len(points) == 3:
        distances = {
            (points[0], points[1]): compute_distance(points[0], points[1]),
            (points[1], points[2]): compute_distance(points[1], points[2]),
            (points[0], points[2]): compute_distance(points[0], points[2])
        }
        print(f"min distance: {min(distances.values())}")
        return list(filter(
            lambda it: distances[it] == min(distances.values()),
            distances.keys()
        ))

    median_x = median(map(lambda it: it[0], inputs))
    print(f"computed median_x: {median_x}")
    # TODO: Implement


def compute_distance(point_a, point_b):
    return sqrt(
        pow(point_b[0] - point_a[0], 2) + pow(point_b[1] - point_a[1], 2)
    )


if __name__ == "__main__":
    inputs = test_data
    print(f"inputs: {inputs}")
    print(f"closest pair: {closest_pair(inputs)}")
