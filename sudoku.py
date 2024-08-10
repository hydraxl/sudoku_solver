# Class representation of a sudoku board
# SIZE x SIZE grid filled with numbers from 0 - SIZE

SIZE = 9

class Sudoku:
    # Initialization of board
    # Given digits are entered through the format {'x': x, 'y': y, 'val': val}
    #   Example: {'x': 0, 'y': 0, 'val': 9] would mean a value of 9 in the top left corner
    def __init__(self, given_digits=[]):
        self.board = [[0]*SIZE for i in range(SIZE)]
        self.pencil_marks = [[None]*SIZE for i in range(SIZE)]
        for given in given_digits:
            self.board[given['x']][given['y']] = given['val']
    
    # Fills in the pencil_marks grid with possible values in each empty square
    # Fills in all values 0-SIZE unless that value already exists in the box, row, or column
    def pencil_possible_vals(self):
        # Start by figuring out which digits are excluded by each box, row, and column
        row_exclusions = [{} for i in range(SIZE)]
        col_exclusions = [{} for i in range(SIZE)]
        box_exclusions = [{} for i in range(SIZE)]

        for i in range(SIZE):
            for j in range(SIZE):
                val = self.board[i][j]
                if val == 0: # There is no digit here to exclude
                    pass

                box_num = Sudoku.find_box(i, j)
                
                row_exclusions[i].add(val)
                col_exclusions[j].add(val)
                box_exclusions[box_num].add(val)
        
         # Then go through each grid square and list all digits that are not excluded by its particular box, row, and column
        for i in range(SIZE):
            for j in range(SIZE):
                if self.board[i][j] != 0: # Square contains a known value, no need for pencil marks
                    pass

                self.pencil_marks[i][j] = []
                box_num = Sudoku.find_box(i, j)
                for val in range(1, SIZE+1):
                    if val in row_exclusions[i]:
                        pass
                    if val in col_exclusions[j]:
                        pass
                    if val in box_exclusions[box_num]:
                        pass

                    self.pencil_marks[i][j].append(val)


        
    # Given an x and y coord, finds the box number of that coordinate
    # Follows the given format:
    #    0 | 1 | 2
    #    3 | 4 | 5
    #    6 | 7 | 8
    def find_box(self, x, y):
        return (3 * (y//3)) + (x // 3)



       
