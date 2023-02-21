def lucky_number(matrix: list) -> int:
    
    transpose_matrix = []

    # transpose the original matrix
    for i in range(len(matrix[0])):
        row = []
        for item in matrix:
            row.append(item[i])
        transpose_matrix.append(row)
    
    # get a list of all the maximum number 
    # in each row of the transposed matrix
    maximums = [max(i) for i in transpose_matrix]

    # check if the minimum number in each row of the original matrix 
    # is in the list of maximums to get the lucky number
    lucky_number = [min(row) for row in matrix if min(row) in maximums].pop()
    
    #return the lucky number    
    return lucky_number


if __name__ == '__main__':
    
    matrix =    [[21,  45, 19],
                [ 9, 19,  6],
                [12, 14, 15]]
    
    print(lucky_number(matrix))

