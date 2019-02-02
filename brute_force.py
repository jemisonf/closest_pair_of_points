from lib import read_inputs, write_outputs
import math
import sys


def calculate_distance(first_point, second_point):
    distance = math.sqrt(math.fabs(
                                  (first_point[1] - second_point[1])**2 +
                                  (first_point[0] - second_point[0])**2))
    return distance


def find_closest_pairs(pairs):
    closest_distance = sys.maxsize
    closest_pairs = list()
    for idx1, pair1 in enumerate(pairs):
        if (idx1 < len(pairs)):
            for idx2, pair2 in enumerate(pairs[idx1 + 1:]):
                cur_distance = calculate_distance(pair1, pair2)
                if (cur_distance < closest_distance):
                    closest_pairs = list([tuple([pair1, pair2])])
                    closest_distance = cur_distance
                elif (cur_distance == closest_distance):
                    closest_pairs.append([pair1, pair2])
    return (closest_distance, closest_pairs)


def main():
    try:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
    except:
        print("Error parsing arguments--need to call with \
              'python3 ./brute_force.py $INPUT_FILE $OUTPUT_FILE'")
        exit()

    pairs = read_inputs(input_file)
    closest_distance, closest_pairs = find_closest_pairs(pairs)
    write_outputs(output_file, closest_distance, closest_pairs)


if (__name__ == "__main__"):
    main()
