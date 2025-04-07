from sudoku_puzzle import SudokuPuzzle
from sudoku_visualizer import SudokuVisualizer
import copy

class SudokuSolver:
    def __init__(self, log_gui_display=True, verbose_flag=False, hide_possible_values_flag=False):
        self.log_gui_display = log_gui_display
        self.hide_possible_values_flag = hide_possible_values_flag
        self.verbose_flag = verbose_flag
        self.steps = []
        if log_gui_display:
            self.visualizer = SudokuVisualizer(hide_possible_values_flag=hide_possible_values_flag)

    def load_puzzle(self, file_name):
        ###Loads a puzzle.###
        #Load isn't using set_square because it's only for the initial puzzle state.
        file = open(file_name, "r")
        puzzle = SudokuPuzzle()

        for x in range(9):
            line = file.readline()
            if line[0] == "-":
                line = file.readline()
            line = line.replace("|", "")

            for y in range(9):
                puzzle.squares[x][y]['value'] = line[y]
                if line[y] == ' ':
                    puzzle.squares[x][y]['initial_value'] = False
                else:
                    puzzle.squares[x][y]['initial_value'] = True
        
        return puzzle

    def display_puzzle_to_console(self, puzzle):
        for x in range(9):
            if x == 3 or x == 6:
                print("--------- --------- ---------")
            for y in range(9):
                if y == 3 or y == 6:
                    print("|", end="")
                print(f" {puzzle.squares[x][y]['value']} ", end="")

            print("")
        print("")

    def start_solving(self, puzzle):
        #record the fist step and then solve
        self.record_step(puzzle)
        puzzle = self.solve_puzzle(puzzle)
        return puzzle
    
    def record_step(self, puzzle):
        self.populate_possible_values(puzzle)
        
        # For unit testing, you can turn off the GUI generator, which add run time, and is a dependency not needed
        if self.log_gui_display == True:
            self.steps.append(self.visualizer.generate_sudoku_render(puzzle))
        else:
            #Just sticking something on the stack so I can still track how many steps are being used here.
            self.steps.append("X")

    def solve_puzzle(self, puzzle):
        ###Solves a Sudoku puzzle.###
        self.populate_possible_values(puzzle)
        
        changesd_squares = 0
        continue_to_loop = True
        while continue_to_loop == True:
            continue_to_loop = False
            # If this puzzle is not solveable any more, return
            if puzzle.is_solvable() == False:
                return puzzle
            
            changesd_squares = 0
            changesd_squares = self.naked_single(puzzle)
            
            # Since changes squreas does promitions until he realizes the puzzle might not be solveable, check here again
            if puzzle.is_solvable() == False:
                return puzzle
            
            if changesd_squares == 0:
                changesd_squares = self.hidden_single(puzzle)
                if puzzle.is_solvable() == False:
                    return puzzle
            
            # Do more complex elimination if the easy options have been removed.
            if changesd_squares == 0:
                changesd_squares = self.locked_candidates(puzzle)
                if puzzle.is_solvable() == False:
                    return puzzle

            if changesd_squares > 0 and puzzle.is_solvable():
                continue_to_loop = True
            if changesd_squares == 0:
                hidden_pairs_elimination = self.hidden_pairs(puzzle)
                
                if hidden_pairs_elimination and puzzle.is_solvable():
                    continue_to_loop = True

        if not puzzle.is_solved():
            puzzle = self.guess_a_value(puzzle)
        
        return puzzle

    def populate_possible_values(self, puzzle):
        ###Populates the possible value array.###
        for x in range(9):
            for y in range(9):
                if puzzle.squares[x][y]['value'] == " ":
                    possible_values = list(range(1, 10))

                    for xaxis in range(9):
                        if (puzzle.squares[xaxis][y]['value'] != " "):
                            if int(puzzle.squares[xaxis][y]['value']) in possible_values:
                                possible_values.remove(int(puzzle.squares[xaxis][y]['value']))

                    for yaxis in range(9):
                        if (puzzle.squares[x][yaxis]['value'] != " "):
                            if int(puzzle.squares[x][yaxis]['value']) in possible_values:
                                possible_values.remove(int(puzzle.squares[x][yaxis]['value']))

                    #Check the box
                    if 0 <= x <= 2:
                        xrange = [0, 1, 2]
                    elif 3 <= x <= 5:
                        xrange = [3, 4, 5]
                    else:
                        xrange = [6, 7, 8]

                    if 0 <= y <= 2:
                        yrange = [0, 1, 2]
                    elif 3 <= y <= 5:
                        yrange = [3, 4, 5]
                    else:
                        yrange = [6, 7, 8]

                    for xaxis in xrange:
                        for yaxis in yrange:
                            if not (xaxis == x and yaxis == y):
                                if (puzzle.squares[xaxis][yaxis]['value'] != " "):
                                    if int(puzzle.squares[xaxis][yaxis]['value']) in possible_values:
                                        possible_values.remove(int(puzzle.squares[xaxis][yaxis]['value']))

                    if puzzle.squares[x][y]['possible_values'] == []:
                        puzzle.squares[x][y]['possible_values'] = possible_values
                    else:
                        # Since hidden pairs can trim possible values, find the intersection of the current list and the new list
                        current_possible_values = puzzle.squares[x][y]['possible_values'] 
                        intersection_list = list(set(possible_values) & set(current_possible_values))
                        puzzle.squares[x][y]['possible_values'] = intersection_list
                else:
                    puzzle.squares[x][y]['possible_values'] = []

    def hidden_single(self, puzzle):
        ###Checks for values that only occur once in a line or in a 3 x 3 box,###
        for x in range(9):
            for y in range(9):
                found_axis_requirement = False
                found_box_requirement = False
                if puzzle.squares[x][y]['value'] == " ":
                    for possible_value in puzzle.squares[x][y]['possible_values']:
                        if not found_axis_requirement and not found_box_requirement:
                            only_x_axis_appearance = True
                            only_y_axis_appearance = True

                            for xaxis in range(9):
                                if possible_value in puzzle.squares[xaxis][y]['possible_values']:
                                    only_x_axis_appearance = False

                            for yaxis in range(9):
                                if possible_value in puzzle.squares[x][yaxis]['possible_values']:
                                    only_y_axis_appearance = False

                            if only_x_axis_appearance or only_y_axis_appearance:
                                found_axis_requirement = True
                                puzzle.set_square(x, y, possible_value)
                                self.record_step(puzzle)
                                return 1
                            else:
                                only_box_appearance = True
                                #Check the box
                                if 0 <= x <= 2:
                                    xrange = [0, 1, 2]
                                elif 3 <= x <= 5:
                                    xrange = [3, 4, 5]
                                else:
                                    xrange = [6, 7, 8]

                                if 0 <= y <= 2:
                                    yrange = [0, 1, 2]
                                elif 3 <= y <= 5:
                                    yrange = [3, 4, 5]
                                else:
                                    yrange = [6, 7, 8]

                                for xaxis in xrange:
                                    for yaxis in yrange:
                                        if not (xaxis == x and yaxis == y):
                                            if possible_value in puzzle.squares[xaxis][yaxis]['possible_values']:
                                                only_box_appearance = False

                                if only_box_appearance:
                                    found_box_requirement = True
                                    puzzle.set_square(x, y, possible_value)
                                    self.record_step(puzzle)
                                    return 1
        
        return 0

    # TODO Describe this mess
    # Locked out possibilities is a techhique I've used that merges a few different sudoku tricks to find a value.
    # For each square not solved, check each possible value and see if the other possibl3e values in that square must appear in a 
    # different row or column out of line with this square due to limitations due to their home 3 x 3 box.
    # If we can determine that the other possibilities 
    def locked_candidates(self, puzzle):
        for number_of_options in range(2, 9):
            for x in range(9):
                for y in range(9):
                    if puzzle.squares[x][y]['value'] == " " and len(puzzle.squares[x][y]['possible_values']) == number_of_options:
                        change_made = self.locked_candidates_analysis(puzzle, x, y)
                        if (change_made):
                            return 1

        return 0

    def locked_candidates_analysis(self, puzzle, x, y):
        # There is another case I can check here for solving the puzzle.
        # I need to check if values for a cell must appear in other cells aligned with the cell on the x asxis and the yaxis. If so, I can prune the list of possibilities
        # Specifically, the use case of two values must appear in two specific cells on any axis.
        # I could also look at this for three cells in a box one the axises.
        for possible_value in puzzle.squares[x][y]['possible_values']:
            other_possible_values = copy.deepcopy(puzzle.squares[x][y]['possible_values'])
            other_possible_values.remove(possible_value)
            
            # Let's get some ranges for a vertical slice
            if 0 <= x <= 2:
                xaxis_of_boxes = [0, 1, 2]
            elif 3 <= x <= 5:
                xaxis_of_boxes = [3, 4, 5]
            else:
                xaxis_of_boxes = [6, 7, 8]
            
            if 0 <= y <= 2:
                yaxis_of_box_1 = [3, 4, 5]
                yaxis_of_box_2 = [6, 7, 8]
            elif 3 <= y <= 5:
                yaxis_of_box_1 = [0, 1, 2]
                yaxis_of_box_2 = [6, 7, 8]
            else:
                yaxis_of_box_1 = [0, 1, 2]
                yaxis_of_box_2 = [3, 4, 5]
            
            # Vertical Box 1
            found_possible_value_not_in_line = False
            for xaxis1 in xaxis_of_boxes:
                for yaxis1 in yaxis_of_box_1:
                    for value in other_possible_values: 
                        if yaxis1 != y:
                            if value in puzzle.squares[xaxis1][yaxis1]['possible_values']:
                                found_possible_value_not_in_line = True

            if not found_possible_value_not_in_line:
                for yaxis2 in yaxis_of_box_1:
                    check_tracker = {}
                    for value2 in other_possible_values:
                        check_tracker[value2] = False
                    
                    for value in other_possible_values: 
                        if value in puzzle.squares[x][yaxis2]['possible_values']:
                            check_tracker[value] = True
                
                everything_in_list = True
                for value2 in check_tracker:
                    if check_tracker[value2] == False:
                        everything_in_list = False
                
                if everything_in_list:
                    self.locked_candidates_set_value(puzzle, x, y, possible_value)
                    return True
                
            # Vertiocal Box 2
            found_possible_value_not_in_line = False
            for xaxis1 in xaxis_of_boxes:
                for yaxis1 in yaxis_of_box_2:
                    for value in other_possible_values: 
                        if yaxis1 != y:
                            if value in puzzle.squares[xaxis1][yaxis1]['possible_values']:
                                found_possible_value_not_in_line = True
            
            if not found_possible_value_not_in_line:
                for yaxis2 in yaxis_of_box_2:
                    check_tracker = {}
                    for value2 in other_possible_values:
                        check_tracker[value2] = False
                    
                    for value in other_possible_values: 
                        if value in puzzle.squares[x][yaxis2]['possible_values']:
                            check_tracker[value] = True
                
                everything_in_list = True
                for value2 in check_tracker:
                    if check_tracker[value2] == False:
                        everything_in_list = False
                
                if everything_in_list:
                    self.locked_candidates_set_value(puzzle, x, y, possible_value)
                    return True
            
            # Let's get some ranges for a horizontial slice
            if 0 <= x <= 2:
                xaxis_of_box_1 = [3, 4, 5]
                xaxis_of_box_2 = [6, 7, 8]
            elif 3 <= x <= 5:
                xaxis_of_box_1 = [0, 1, 2]
                xaxis_of_box_2 = [6, 7, 8]
            else:
                xaxis_of_box_1 = [0, 1, 2]
                xaxis_of_box_2 = [3, 4, 5]
            
            if 0 <= y <= 2:
                yaxis_of_boxes = [0, 1, 2]
            elif 3 <= y <= 5:
                yaxis_of_boxes = [3, 4, 5]
            else:
                yaxis_of_boxes = [6, 7, 8]
            
            # Horizontal Box 1
            found_possible_value_not_in_line = False
            for xaxis1 in xaxis_of_box_1:
                for yaxis1 in yaxis_of_boxes:
                    for value in other_possible_values: 
                        if yaxis1 != y:
                            if value in puzzle.squares[xaxis1][yaxis1]['possible_values']:
                                found_possible_value_not_in_line = True

            if not found_possible_value_not_in_line:
                for xaxis2 in xaxis_of_box_1:
                    check_tracker = {}
                    for value2 in other_possible_values:
                        check_tracker[value2] = False
                    
                    for value in other_possible_values: 
                        if value in puzzle.squares[xaxis2][y]['possible_values']:
                            check_tracker[value] = True
                
                everything_in_list = True
                for value2 in check_tracker:
                    if check_tracker[value2] == False:
                        everything_in_list = False
                
                if everything_in_list:
                    self.locked_candidates_set_value(puzzle, x, y, possible_value)
                    return True

            # Horizontal Box 2
            found_possible_value_not_in_line = False
            for xaxis1 in xaxis_of_box_2:
                for yaxis1 in yaxis_of_boxes:
                    for value in other_possible_values: 
                        if yaxis1 != y:
                            if value in puzzle.squares[xaxis1][yaxis1]['possible_values']:
                                found_possible_value_not_in_line = True
            
            if not found_possible_value_not_in_line:
                for xaxis2 in xaxis_of_box_2:
                    check_tracker = {}
                    for value2 in other_possible_values:
                        check_tracker[value2] = False
                    
                    for value in other_possible_values: 
                        if value in puzzle.squares[xaxis2][y]['possible_values']:
                            check_tracker[value] = True
                
                everything_in_list = True
                for value2 in check_tracker:
                    if check_tracker[value2] == False:
                        everything_in_list = False
                
                if everything_in_list:
                    self.locked_candidates_set_value(puzzle, x, y, possible_value)
                    return True
        
        return False
    
    def hidden_pairs(self, puzzle):
        ###Removes possibilities with hidden pairs###
        change_made = False
        for x in range(9):
            for y in range(9):
                if puzzle.squares[x][y]['value'] == " " and len(puzzle.squares[x][y]['possible_values']) >= 2:
                    for pair_of_possibilities in self.get_possible_pairs(puzzle.squares[x][y]['possible_values']):
                    
                        change_made = self.hidden_pairs_check(puzzle, x, y, pair_of_possibilities)
                        # if (change_made):
                        #     print("Hidden pairs man!!!!")
                        #     return True

        if (change_made):
            return True
        else:
            return False
    
    def hidden_pairs_check(self, puzzle, x1, y1, pair_of_possibilities):
        ###Does a possible pairs check###
        pair_value1 = pair_of_possibilities[0]
        pair_value2 = pair_of_possibilities[1]
        
        matrix_changed = False
        #First, see if this pair occurs in another square in line or in our cube.

        # Vertical check
        for xaxis in range(9):
            if xaxis != x1:
                if puzzle.squares[xaxis][y1]['value'] == ' ':
                    possible_values_in_square = puzzle.squares[xaxis][y1]['possible_values']
                    if pair_of_possibilities[0] in possible_values_in_square and pair_of_possibilities[1] in possible_values_in_square:
                        collision_found = False
                        for xaxis2 in range(9):
                            if xaxis2 != x1 and xaxis2 != xaxis and collision_found == False:
                                possible_values_in_square_in_other_square = puzzle.squares[xaxis2][y1]['possible_values']
                                if pair_value1 in possible_values_in_square_in_other_square or pair_value2 in possible_values_in_square_in_other_square:
                                    collision_found = True
                        
                        if (puzzle.squares[x1][y1]['possible_values'] != pair_of_possibilities or puzzle.squares[xaxis][y1]['possible_values'] != pair_of_possibilities) and not collision_found:
                            self.mark_hidden_pairs(puzzle, x1, y1, xaxis, y1, pair_of_possibilities)
                            return True

        # Horizontal check
        for yaxis in range(9):
            if yaxis != y1:
                if puzzle.squares[x1][yaxis]['value'] == ' ':
                    possible_values_in_square = puzzle.squares[x1][yaxis]['possible_values']
                    if pair_of_possibilities[0] in possible_values_in_square and pair_of_possibilities[1] in possible_values_in_square:
                        collision_found = False
                        for yaxis2 in range(9):
                            if yaxis2 != y1 and yaxis2 != yaxis and collision_found == False:
                                possible_values_in_square_in_other_square = puzzle.squares[x1][yaxis2]['possible_values']
                                if pair_value1 in possible_values_in_square_in_other_square or pair_value2 in possible_values_in_square_in_other_square:
                                    collision_found = True
                                    
                        if (puzzle.squares[x1][y1]['possible_values'] != pair_of_possibilities or puzzle.squares[x1][yaxis]['possible_values'] != pair_of_possibilities) and not collision_found:
                            self.mark_hidden_pairs(puzzle, x1, y1, x1, yaxis, pair_of_possibilities)
                            return True
        
        # Box check
        if 0 <= x1 <= 2:
            xaxis_of_box = [0, 1, 2]
        elif 3 <= x1 <= 5:
            xaxis_of_box = [3, 4, 5]
        else:
            xaxis_of_box = [6, 7, 8]
        
        if 0 <= y1 <= 2:
            yaxis_of_box = [0, 1, 2]
        elif 3 <= y1 <= 5:
            yaxis_of_box = [3, 4, 5]
        else:
            yaxis_of_box = [6, 7, 8]
            
        for xaxis in xaxis_of_box:
            for yaxis in yaxis_of_box:
                if xaxis != x1 and yaxis != x1:
                    if puzzle.squares[xaxis][yaxis]['value'] == ' ':
                        possible_values_in_square = puzzle.squares[xaxis][yaxis]['possible_values']
                        box_1 = str(x1) + str(y1)
                        box_2 = str(xaxis) + str(yaxis)
                        if pair_of_possibilities[0] in possible_values_in_square and pair_of_possibilities[1] in possible_values_in_square:
                            collision_found = False
                            for xaxis2 in xaxis_of_box:
                                for yaxis2 in yaxis_of_box:
                                    box_checking = str(xaxis2) + str(yaxis2)
                                    if box_1 != box_checking and box_2 != box_checking and collision_found == False:
                                        possible_values_in_square_in_other_square = puzzle.squares[xaxis2][yaxis2]['possible_values']
                                        if pair_value1 in possible_values_in_square_in_other_square or pair_value2 in possible_values_in_square_in_other_square:
                                            collision_found = True
                                            
                            if (puzzle.squares[x1][y1]['possible_values'] != pair_of_possibilities or puzzle.squares[xaxis][yaxis]['possible_values'] != pair_of_possibilities) and not collision_found:
                                self.mark_hidden_pairs(puzzle, x1, y1, xaxis, yaxis, pair_of_possibilities)
                                return True
        
        return False
    
    def mark_hidden_pairs(self, puzzle, x1, y1, x2, y2, pair):
        ###Set hidden pairs values.###
        if __debug__ and self.verbose_flag:
            print(f"Hidden pairs set the possibilities as {pair[0]}, {pair[1]} on the squares [{x1}, {y1}] and [{x2}, {y2}]")
            print()
            self.display_puzzle_to_console(puzzle)
        
        puzzle.squares[x1][y1]['possible_values'] = pair
        puzzle.squares[x2][y2]['possible_values'] = pair
    
    def get_possible_pairs(self, possible_values):
        ###Gets the possible pairs out of the list of possible values.###
        sets = []
        
        if len(possible_values) >= 2:
            for value in possible_values:
                for other_value in possible_values:
                    if other_value > value:
                        sets.append([value, other_value])
                        
        return sets

    def locked_candidates_set_value(self, puzzle, x, y, value_to_set):
        if __debug__ and self.verbose_flag:
            print(f"Analysis calculated the value at [{x}, {y}] to be {value_to_set}")
            print()
            self.display_puzzle_to_console(puzzle)
        
        puzzle.set_square(x, y, value_to_set)
        self.record_step(puzzle)
        
        puzzle.locked_candidates_helped = True

    def guess_a_value(self, puzzle):
        puzzle.guessing_used = True
        unmodified_puzzle = copy.deepcopy(puzzle)

        x, y = self.pick_a_square_to_guess(unmodified_puzzle)

        for possible_value in unmodified_puzzle.squares[x][y]['possible_values']:
            if __debug__ and self.verbose_flag:
                print(f"Guessing a value at [{x}, {y}] with the value {possible_value}")
                print()
                self.display_puzzle_to_console(unmodified_puzzle)
                
            puzzle2 = copy.deepcopy(unmodified_puzzle)

            puzzle2.set_square(x, y, possible_value)
            puzzle2.squares[x][y]['is_guess'] = True
            self.record_step(puzzle2)
            
            skip_guess = False
            if puzzle2.is_solvable() == False:
                skip_guess == True

            if skip_guess != True:
                puzzle2 = self.solve_puzzle(puzzle2)
                if puzzle2.is_solved():
                    puzzle = copy.deepcopy(puzzle2)
                    return puzzle
      
        return unmodified_puzzle

    def pick_a_square_to_guess(self, puzzle):
        #If there is a square with only one option, this method should not be called, but we're returning it incase it is.
        for option_count in range(2, 10):
            for x in range(9):
                for y in range(9):
                    if puzzle.squares[x][y]['value'] == " " and len(puzzle.squares[x][y]['possible_values']) > 0 and len(puzzle.squares[x][y]['possible_values']) <= option_count:
                        return x, y
        
        #This is an error state
        return -1, -1

    def naked_single(self, puzzle):
        ###Promotes solved squares.###
        promotions = 0

        for x in range(9):
            for y in range(9):
                if len(puzzle.squares[x][y]['possible_values']) == 1:
                    puzzle.set_square(x, y, puzzle.squares[x][y]['possible_values'][0])
                    self.record_step(puzzle)
                    promotions += 1
                    
                    if puzzle.is_solvable == False:
                        return promotions

        return promotions