import random
import sys

MAX_SIZE = sys.maxsize
MIN_SIZE = 0

# Call program as python3 create_test_inputs.py $NUM_PAIRS


def get_random_pair(min_size, max_size):
    x = random.randint(min_size, max_size)
    y = random.randint(min_size, max_size)
    return (x, y)


def write_pairs(pairs):
    with open(f'testinput-{len(pairs)}', "w") as f:
        for pair in pairs:
            f.write(f'{pair[0]} {pair[1]}\n')


def generate_random_pairs(num_pairs):
    pairs = list()
    for _ in range(num_pairs):
        pairs.append(get_random_pair(MIN_SIZE, MAX_SIZE))
    write_pairs(pairs)

random.seed()
num_pairs = int(sys.argv[1])
generate_random_pairs(num_pairs)
