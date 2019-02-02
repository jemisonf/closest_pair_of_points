from math import pow, sqrt
from statistics import median
from typing import List, Tuple

import lib


test_data = [(1, 2), (5, 2), (8, 9), (10, 20), (11, 21), (9, 5), (19, 21)]
test_data_2 = [(1, 2), (3, 4)]
test_data_3 = [(1, 2), (3, 4), (5, 6)]


def closest_pair(points: List[Tuple]) -> List[Tuple[Tuple]]:
    if len(points) == 2:
        result = list()
        result.append(tuple(points))
        print(f"returning {result}")
        return result
    if len(points) == 3:
        distances = {
            (points[0], points[1]): compute_distance(points[0], points[1]),
            (points[1], points[2]): compute_distance(points[1], points[2]),
            (points[0], points[2]): compute_distance(points[0], points[2])
        }
        print(f"min distance: {min(distances.values())}")
        result = list(filter(
            lambda it: distances[it] == min(distances.values()),
            distances.keys()
        ))
        print(f"returning {result}")
        return result

    median_x = median(map(lambda it: it[0], points))
    print(f"computed median_x: {median_x}")
    left_half = list(filter(lambda it: it[0] <= median_x, points))
    right_half = list(filter(lambda it: it[0] > median_x, points))
    print(f"left_half: {left_half}")
    print(f"right_half: {right_half}")
    closest_left = closest_pair(left_half)
    closest_right = closest_pair(right_half)
    delta = min([
        compute_distance(closest_left[0][0], closest_left[0][1]),
        compute_distance(closest_right[0][0], closest_right[0][1])
    ])
    print(f"computed delta: {delta}")
    middle_band = list(filter(
        lambda it: median_x - delta <= it[0] <= median_x + delta,
        points
    ))
    print(f"middle_band: {middle_band}")
    # Sort by y coord
    # Call closest cross pair


def closest_cross_pair(
    points: List[Tuple], delta: float
) -> List[Tuple[Tuple]]:
    dm = delta
    for i in range(len(points) - 1):
        j = i + 1
        while(points[j][1] - points[i][1] <= delta and j <= len(points)):
            d = compute_distance(points[0], points[1])
            dm = min(d, dm)
            j = j + 1
    print(f"min distance in cross pairs: {dm}")
    #TODO return closest pairs without increasing runtime


def compute_distance(point_a, point_b):
    return sqrt(
        pow(point_b[0] - point_a[0], 2) + pow(point_b[1] - point_a[1], 2)
    )


if __name__ == "__main__":
    inputs = test_data
    print(f"inputs: {inputs}")
    print(f"closest pair: {closest_pair(inputs)}")
