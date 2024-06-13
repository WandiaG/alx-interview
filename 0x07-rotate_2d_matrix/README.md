module contains algorithm that rotates a 2d array 90 degrees
    clockwise
    APPROACH:
        -> normalize the 2d array to a 1d array by abstracting each
           row_index - column-index pair into a single index; from
           this single index row_index and col_index can be computed
           easily since the matrix width == height
            -> actual row_index = floor(normalized_index / width)
               eg: if n_i = 20 and width = 5 actual row n_i element
               belong to = 4 (ie 5th row 0 indexed)
            -> actual col_index = normalized_index % width
               eg: if n_i = 20 and width = 5 actual column n_i element
               belong to = 0 (ie 1st column 0 indexed)
        -> get all possible indeces == width * height of matrix
        -> build a map of all normalized indeces to:
            -> its next position
            -> its value
        -> loop over map and place each value in its new position
    FUNCTIONS:
    rotate_2d_matrix -> main function; gathers every function together
    build_map -> builds a map of all normalized indeces to:
        -> its next position
        -> its value
        map_structure = {
            index: {
                'new_index': computed_new_index,
                'value': value at current index
            }
        }
    get_new_index -> computes the new index of an index after rotation
        parameters:
        index -> index to compute new index for
        width -> width of the matrix
        LOGIC:
            -> get its current col_index
            -> get its current row_index
            -> next_col_index = width - 1 - current_row_index
               e.g:
               4 starts at col_index 0, row_index 1
               and its new col_index is 1
               which is == 3(width) - 1(constant) - 1(row_index)
                start [                 end [
                        [1, 2, 3],              [7, 4, 1],
                        [4, 5, 6],              [8, 5, 2],
                        [7, 8, 9]               [9, 6, 3],
                ]                       ]
            -> next_row_index = current_col_index
               e.g:
               6 starts at row_index 1, col_index 2
               and its new row_index is 2
               which is == next_row_index = current_col_index
                start [                 end [
                        [1, 2, 3],              [7, 4, 1],
                        [4, 5, 6],              [8, 5, 2],
                        [7, 8, 9]               [9, 6, 3],
                ]                       ]
            -> compute normalized new index and return it
    get_value -> denormalize normalized index and return the
                 value retrived from the actual matrix
    compute_row_and_index -> returns actual row and index from a
                             normalized index
