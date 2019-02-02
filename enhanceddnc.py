from math import pow, sqrt
from statistics import median
from sys import argv
from typing import List, Tuple

from lib import read_inputs


def closest_pair(points: List[Tuple]) -> Tuple[float, List[Tuple[Tuple]]]:
    if len(points) == 2:
        result = list()
        result.append(tuple(points))
        final_result = (compute_distance(points[0], points[1]), result)
        print(f"returning {final_result}")
        return final_result
    if len(points) == 3:
        distances = {
            (points[0], points[1]): compute_distance(points[0], points[1]),
            (points[1], points[2]): compute_distance(points[1], points[2]),
            (points[0], points[2]): compute_distance(points[0], points[2])
        }
        min_distance = min(distances.values())
        print(f"min distance: {min_distance}")
        result = list(filter(
            lambda it: distances[it] == min_distance,
            distances.keys()
        ))
        final_result = (min_distance, result)
        print(f"returning {final_result}")
        return final_result

    median_x = median(map(lambda it: it[0], points))
    print(f"computed median_x: {median_x}")
    left_half = list(filter(lambda it: it[0] <= median_x, points))
    right_half = list(filter(lambda it: it[0] > median_x, points))
    print(f"left_half: {left_half}")
    print(f"right_half: {right_half}")
    print("\nrecursive call on left")
    closest_left = closest_pair(left_half)
    print("\nrecursive call on right")
    closest_right = closest_pair(right_half)
    print()
    delta = min([closest_left[0], closest_right[0]])
    print(f"computed delta: {delta}")
    middle_band = list(filter(
        lambda it: median_x - delta <= it[0] <= median_x + delta,
        points
    ))
    print(f"middle_band: {middle_band}")
    # Sort by y coord
    middle_band.sort(key=lambda it: it[1])
    # Call closest cross pair
    closest_cross = closest_cross_pair(middle_band, delta)
    print(f"closest_cross: {closest_cross}")
    new_min = min(delta, closest_cross[0])
    print(f"new_min: {new_min}")
    result = (new_min, [])
    for section in [closest_left, closest_right, closest_cross]:
        if section[0] == new_min:
            for pair in section[1]:
                if not any(x in result[1] for x in [pair, (pair[1], pair[0])]):
                    result[1].append(pair)
    print(f"result: {result}")
    return result


def closest_cross_pair(
    points: List[Tuple], delta: float
) -> Tuple[float, List[Tuple[Tuple]]]:
    dm = delta
    for i in range(len(points) - 1):
        j = i + 1
        while(j < len(points) and points[j][1] - points[i][1] <= delta):
            d = compute_distance(points[0], points[1])
            dm = min(d, dm)
            j = j + 1
    print(f"min distance in cross pairs: {dm}")
    pairs = list((x, y) for x in points for y in points)
    print(f"pairs: {pairs}")
    result = list(filter(
        lambda it: compute_distance(it[0], it[1]) <= dm and it[0] != it[1],
        pairs
    ))
    final_result = (dm, result)
    return final_result


def compute_distance(point_a, point_b):
    return sqrt(
        pow(point_b[0] - point_a[0], 2) + pow(point_b[1] - point_a[1], 2)
    )


if __name__ == "__main__":
    try:
        inputs = read_inputs(argv[1])
    except IndexError:
        exit("No input file was provided")
    print(f"inputs: {inputs}")
    print(f"closest pair: {closest_pair(inputs)}")
