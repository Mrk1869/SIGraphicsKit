# coding:utf-8

import matrix
import numpy as np

if __name__ == "__main__":
    classes = ["ostrich", "swallow", "cuckoo", "chicken", "quail"]
    data = np.array([
        [50, 0, 0, 0, 0],
        [1, 41, 5, 3, 0],
        [2, 9, 34, 4, 1],
        [1, 1, 8, 38, 2],
        [1, 0, 2, 3, 44],
        ])
    confusion_matrix = matrix.Matrix(classes, data)
    confusion_matrix.draw()
