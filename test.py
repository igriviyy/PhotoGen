# figuring out how stdout, stderr works with DeepFace function
import os
import sys
from deepface import DeepFace
from operator import add
import warnings
from functools import reduce


def test_function():
    result_dict = DeepFace.analyze('em1.jpg', actions=['gender', 'age'])
    return result_dict


old_stdout = sys.stdout
file = open('output.txt', 'r+')
# sys.stdout = file
# sys.stderr = file
# print(test_function())
# sys.stdout = old_stdout
print(*map(lambda *args: sum(args), [1, 2, 3, 10], [5, 6, 7, 8], [1, 2, 3, 4]))
file.close()



