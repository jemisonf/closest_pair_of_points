from lib import read_inputs, write_outputs
import os


def test_read_inputs():
    with open("testinput", "w+") as f:
        f.write("1 0\n0 1\n2 3\n3 4\n5 6\n9 1\n8 2\n")

    inputs = read_inputs("testinput")

    os.remove("testinput")

    assert(len(inputs) == 7)
    assert(inputs[0][0] == 1 and inputs[0][1] == 0)
    assert(inputs[1][0] == 0 and inputs[1][1] == 1)
    assert(inputs[6][0] == 8 and inputs[6][1] == 2)


def test_write_outputs():
    distance = 1.0
    points = list([
                [[1, 0], [1, 1]],
                [[2, 0], [2, 1]],
                [[4, 1], [5, 1]]
            ])
    write_outputs("testoutput", distance, points)
    with open("testoutput") as f:
        contents = f.read()
    assert(contents == "1.0\n1 0 1 1\n2 0 2 1\n4 1 5 1\n")

    os.remove("testoutput")
test_read_inputs()
test_write_outputs()
