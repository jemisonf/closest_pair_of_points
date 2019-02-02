import math

from brute_force import find_closest_pairs


def check_output_equality(real, desired):
    for idx, pair in enumerate(real):
        assert(pair[0] == desired[idx][0])
        assert(pair[1] == desired[idx][1])


def main():
    testin_0 = list([[1, 0], [0, 1]])
    testdist_0 = math.sqrt(2)
    testout_0 = list([
                        [[1, 0], [0, 1]],
                    ])

    testin_1 = list([[1, 0],
                     [1, 1],
                     [3, 0],
                     [3, 1],
                     [5, 1],
                     [6, 1],
                     ])
    testdist_1 = 1
    testout_1 = list([
            [[1, 0], [1, 1]],
            [[3, 0], [3, 1]],
            [[5, 1], [6, 1]],
            ])

    testin_2 = list([[1, 1], [2, 2], [3, 3], [5, 5]])
    testdist_2 = math.sqrt(2)
    testout_2 = list([
            [[1, 1], [2, 2]],
            [[2, 2], [3, 3]]])

    print("Checking for base test")
    dist, closest_pairs = find_closest_pairs(testin_0)
    check_output_equality(closest_pairs, testout_0)
    assert(dist == testdist_0)
    print("... Passed")

    print("Checking for 1st test")
    dist, closest_pairs = find_closest_pairs(testin_1)
    check_output_equality(closest_pairs, testout_1)
    assert(dist == testdist_1)
    print("... Passed")

    print("Checking for 2nd test")
    dist, closest_pairs = find_closest_pairs(testin_2)
    check_output_equality(closest_pairs, testout_2)
    assert(dist == testdist_2)
    print("... Passed")
if (__name__ == "__main__"):
    main()
