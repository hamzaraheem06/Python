
def get_transpose(matrix: list):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = []

    for i in range(0, rows):
        for j in range(0, cols):
            transpose[j][i] = matrix[i][j]
        
    return transpose

def main():
    matrix = [[2, 4], [23, 12]]
    rows = len(matrix)
    cols = len(matrix[0])

    result = get_transpose(matrix)

    for i in range(0, cols):
        for j in range(0, rows):
            print(matrix[i][j], end="  ")
        
        print()

main()


