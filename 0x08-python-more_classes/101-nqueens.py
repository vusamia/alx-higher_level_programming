#!/usr/bin/python3
"""
nqueens backtracking program to print the coordinates of n queens
on an nxn grid such that they are all in non-attacking positions
"""
from sys import argv
if __name__ == "__main__":
    ab = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    m = int(argv[1])
    if m < 4:
        print("N must be at least 4")
        exit(1)
    # initialize the answer list
    for z in range(m):
        ab.append([z, None])

    def already_exists(q):
        """check that a queen does not already exist in that y value"""
        for f in range(m):
            if q == ab[f][1]:
                return True
        return False

    def reject(f, q):
        """determines whether or not to reject the solution"""
        if (already_exists(q)):
            return False
        z = 0
        while(z < f):
            if abs(ab[z][1] - q) == abs(z - f):
                return False
            z += 1
        return True

    def clear_a(f):
        """clears the answers from the point of failure on"""
        for z in range(f, m):
            ab[z][1] = None

    def nqueens(f):
        """recursive backtracking function to find the solution"""
        for q in range(m):
            clear_a(f)
            if reject(f, q):
                ab[f][1] = q
                if (f == m - 1):  # accepts the solution
                    print(ab)
                else:
                    nqueens(f + 1)  # moves on to next x value to continue
    # start the recursive process at x = 0
    nqueens(0)
