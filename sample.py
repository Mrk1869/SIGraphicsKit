# coding:utf-8

import matrix
import numpy as np

if __name__ == "__main__":
    classes = ["ostrich", "swallow", "cuckoo", "chicken", "quail"]
    data = np.array([
        [18, 0, 1, 2, 9],
        [2, 24, 0, 1, 3],
        [0, 0, 21, 8, 1],
        [0, 1, 10, 19, 0],
        [4, 0, 0, 0, 26],
        ])
    mx = matrix.Matrix(classes, data)
    mx.draw()
