#!/usr/bin/python3

matrix_mul = __import__('100-matrix_mul').matrix_mul



print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))

print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))



guillaume@ubuntu:~/0x07$ ./100-main.py 

[[7, 10], [15, 22]]

[[13, 16]]

guillaume@ubuntu:~/0x07$ python3 -m doctest -v ./tests/100-matrix_mul.txt | tail -2

6 passed and 0 failed.

Test passed.
