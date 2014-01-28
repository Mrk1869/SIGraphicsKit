# coding:utf-8

import matrix
import numpy as np

if __name__ == "__main__":
    classes = ["ostrich", "swallow", "cuckoo", "chicken", "quail"]
    data = np.array([
        [50, 0, 0, 0, 0],
        [2, 40, 4, 4, 0],
        [2, 8, 34, 4, 2],
        [0, 2, 8, 38, 2],
        [2, 0, 2, 2, 44],
        ])
    confusion_matrix = matrix.Matrix(classes, data)
    confusion_matrix.draw()
