from nicegui import app, ui
from SudokuPuzzle import SudokuPuzzle
import copy
import time

#This might get removed, but for now it's here.
STYLE = """
<style>
.possibleValuesCell {
    width: 33.33%;
    height: 33.33%;
    text-align: center;
    color: gray;
}

.puzzleCell {
    border: 2px solid black;
    padding: 0px;
    width: 80px;
    height: 80px;
}

.possibleValues {
    width: 100%;
    height: 100%;
}

.valueCellContainer {
    width: 100%;
    height: 100%;
}

.valueCell {
    text-align: center;
    font-size: 50px;
    width: 100%;
    height: 100%;
}

.initialValueCell {
    background-color: gainsboro;
}

.cell-00, .cell-10, .cell-20, .cell-30, .cell-40, .cell-50, .cell-60, .cell-70, .cell-80, 
.cell-03, .cell-13, .cell-23, .cell-33, .cell-43, .cell-53, .cell-63, .cell-73, .cell-83,
.cell-06, .cell-16, .cell-26, .cell-36, .cell-46, .cell-56, .cell-66, .cell-76, .cell-86 {
    border-left: 5px solid black;
}

.cell-08, .cell-18, .cell-28, .cell-38, .cell-48, .cell-58, .cell-68, .cell-78, .cell-88 {
    border-right: 5px solid black;
}

.cell-00, .cell-01, .cell-02, .cell-03, .cell-04, .cell-05, .cell-06, .cell-07, .cell-08,
.cell-30, .cell-31, .cell-32, .cell-33, .cell-34, .cell-35, .cell-36, .cell-37, .cell-38,
.cell-60, .cell-61, .cell-62, .cell-63, .cell-64, .cell-65, .cell-66, .cell-67, .cell-68
{
    border-top: 5px solid black;
}

.cell-80, .cell-81, .cell-82, .cell-83, .cell-84, .cell-85, .cell-86, .cell-87, .cell-88
{
    border-bottom: 5px solid black;
}
</style>
"""

FOUND_CELL = """
<div class="valueCellContainer">
    <div class="valueCell">xyz</div>
</div>
"""

POSSIBLE_VALUES = """
<table class="possibleValues">
<tr>
    <td class="possibleValuesCell">x1</td>
    <td class="possibleValuesCell">x2</td>
    <td class="possibleValuesCell">x3</td>
</tr>
<tr>
    <td class="possibleValuesCell">x4</td>
    <td class="possibleValuesCell">x5</td>
    <td class="possibleValuesCell">x6</td>
</tr>
<tr>
    <td class="possibleValuesCell">x7</td>
    <td class="possibleValuesCell">x8</td>
    <td class="possibleValuesCell">x9</td>
</tr>
</table>
"""

SUDOKU_CONTAINER = """
<table class="puzzle">
<tr class="puzzleRow">
    <td class="puzzleCell cell-00">z00</td>
    <td class="puzzleCell cell-01">z01</td>
    <td class="puzzleCell cell-02">z02</td>
    <td class="puzzleCell cell-03">z03</td>
    <td class="puzzleCell cell-04">z04</td>
    <td class="puzzleCell cell-05">z05</td>
    <td class="puzzleCell cell-06">z06</td>
    <td class="puzzleCell cell-07">z07</td>
    <td class="puzzleCell cell-08">z08</td>
</tr>
<tr class="puzzleRow">
    <td class="puzzleCell cell-10">z10</td>
    <td class="puzzleCell cell-11">z11</td>
    <td class="puzzleCell cell-12">z12</td>
    <td class="puzzleCell cell-13">z13</td>
    <td class="puzzleCell cell-14">z14</td>
    <td class="puzzleCell cell-15">z15</td>
    <td class="puzzleCell cell-16">z16</td>
    <td class="puzzleCell cell-17">z17</td>
    <td class="puzzleCell cell-18">z18</td>
</tr>
<tr class="puzzleRow">
    <td class="puzzleCell cell-20">z20</td>
    <td class="puzzleCell cell-21">z21</td>
    <td class="puzzleCell cell-22">z22</td>
    <td class="puzzleCell cell-23">z23</td>
    <td class="puzzleCell cell-24">z24</td>
    <td class="puzzleCell cell-25">z25</td>
    <td class="puzzleCell cell-26">z26</td>
    <td class="puzzleCell cell-27">z27</td>
    <td class="puzzleCell cell-28">z28</td>
</tr>
<tr class="puzzleRow">
    <td class="puzzleCell cell-30">z30</td>
    <td class="puzzleCell cell-31">z31</td>
    <td class="puzzleCell cell-32">z32</td>
    <td class="puzzleCell cell-33">z33</td>
    <td class="puzzleCell cell-34">z34</td>
    <td class="puzzleCell cell-35">z35</td>
    <td class="puzzleCell cell-36">z36</td>
    <td class="puzzleCell cell-37">z37</td>
    <td class="puzzleCell cell-38">z38</td>
</tr>
<tr class="puzzleRow">
    <td class="puzzleCell cell-40">z40</td>
    <td class="puzzleCell cell-41">z41</td>
    <td class="puzzleCell cell-42">z42</td>
    <td class="puzzleCell cell-43">z43</td>
    <td class="puzzleCell cell-44">z44</td>
    <td class="puzzleCell cell-45">z45</td>
    <td class="puzzleCell cell-46">z46</td>
    <td class="puzzleCell cell-47">z47</td>
    <td class="puzzleCell cell-48">z48</td>
</tr>
<tr class="puzzleRow">
    <td class="puzzleCell cell-50">z50</td>
    <td class="puzzleCell cell-51">z51</td>
    <td class="puzzleCell cell-52">z52</td>
    <td class="puzzleCell cell-53">z53</td>
    <td class="puzzleCell cell-54">z54</td>
    <td class="puzzleCell cell-55">z55</td>
    <td class="puzzleCell cell-56">z56</td>
    <td class="puzzleCell cell-57">z57</td>
    <td class="puzzleCell cell-58">z58</td>
</tr>
<tr class="puzzleRow">
    <td class="puzzleCell cell-60">z60</td>
    <td class="puzzleCell cell-61">z61</td>
    <td class="puzzleCell cell-62">z62</td>
    <td class="puzzleCell cell-63">z63</td>
    <td class="puzzleCell cell-64">z64</td>
    <td class="puzzleCell cell-65">z65</td>
    <td class="puzzleCell cell-66">z66</td>
    <td class="puzzleCell cell-67">z67</td>
    <td class="puzzleCell cell-68">z68</td>
</tr>
<tr class="puzzleRow">
    <td class="puzzleCell cell-70">z70</td>
    <td class="puzzleCell cell-71">z71</td>
    <td class="puzzleCell cell-72">z72</td>
    <td class="puzzleCell cell-73">z73</td>
    <td class="puzzleCell cell-74">z74</td>
    <td class="puzzleCell cell-75">z75</td>
    <td class="puzzleCell cell-76">z76</td>
    <td class="puzzleCell cell-77">z77</td>
    <td class="puzzleCell cell-78">z78</td>
</tr>
<tr class="puzzleRow">
    <td class="puzzleCell cell-80">z80</td>
    <td class="puzzleCell cell-81">z81</td>
    <td class="puzzleCell cell-82">z82</td>
    <td class="puzzleCell cell-83">z83</td>
    <td class="puzzleCell cell-84">z84</td>
    <td class="puzzleCell cell-85">z85</td>
    <td class="puzzleCell cell-86">z86</td>
    <td class="puzzleCell cell-87">z87</td>
    <td class="puzzleCell cell-88">z88</td>
</tr>
</table>
"""

class SudokuVisualizer:
    def __init__(self):
        #ToDo Should all the HTML and styling be declared in init?
        pass

    def generate_possible_values_html(self, possible_values):
        body_new = copy.deepcopy(POSSIBLE_VALUES)
        
        for x in range(1,10):
            cell = "x" + str(x)
            if x in possible_values:
                body_new = body_new.replace(cell, str(x))
            else:
                body_new = body_new.replace(cell, "&nbsp;")
        
        return body_new

    def generate_sudoku_render(self, puzzle):
        sudoku_rendering = copy.deepcopy(SUDOKU_CONTAINER)
        
        for x in range(9):
            for y in range(9):
                cell = "z" + str(x) + str(y)
                
                html_fragment = ""
                if puzzle.squares[x][y]['value'] == " ":
                    possible_values = puzzle.squares[x][y]['possible_values']
        
                    html_fragment = self.generate_possible_values_html(possible_values)
                else:
                    found_value = puzzle.squares[x][y]['value']
                    html_fragment = copy.deepcopy(FOUND_CELL)
                    
                    if puzzle.squares[x][y]['initial_value'] == True:
                        html_fragment = html_fragment.replace('"valueCell"', '"valueCell initialValueCell"')
                        pass
                    
                    html_fragment = html_fragment.replace("xyz", str(found_value))
                    
                sudoku_rendering = sudoku_rendering.replace(cell, html_fragment)
        
        
        return sudoku_rendering

    #this method will have to go at some point if this is to be unit tested.
    def display_puzzle_to_website(self, puzzle):
        app.native.window_args['resizable'] = False
        app.native.start_args['debug'] = True
        app.native.settings['ALLOW_DOWNLOADS'] = True
        
        ui.html(STYLE)
        ui.label('Hello NiceGUI!')
        
        sudoku_rendering = self.generate_sudoku_render(puzzle)
        ui.html(sudoku_rendering)
        
        ui.button('Solve Puzzle', on_click=lambda: ui.notify('button was pressed'))
        #ui.table()
        
        #ui.run(native=True, window_size=(400, 300), fullscreen=False)
        ui.run()
        
    @ui.refreshable
    def render_gui(self, steps):
        ui.html(STYLE)
        ui.label('Hello NiceGUI!')
        
        container = ui.html()
        #timer = ui.timer(1.0, lambda: container.set_content(steps[3]))
        #timer.active = False
        
        container.set_content(steps[0])
        
        global total_steps
        total_steps = len(steps) -1
        
        with ui.grid(columns=5):
            ui.button('<', on_click=lambda: container.set_content(get_previous_step(steps))), 
            ui.button('Autosolve Puzzle', on_click=lambda: container.set_content(get_next_step(steps)))
            ui.button('>', on_click=lambda: container.set_content(get_next_step(steps)))
            ui.button('Show Solution', on_click=lambda: container.set_content(get_last_step(steps)))
            ui.button('Reset', on_click=lambda: container.set_content(reset_puzzle(steps)))
        
        ui.run()
        
        #ui.html(steps[0])

        
        #ui.table()
        
        #ui.run(native=True, window_size=(400, 300), fullscreen=False)
        # def handle_click(steps):
        #     for state in steps:
        #         container.set_content(state)
                
        #         time.sleep(1)
        
        # so here's a thought, what if I put the curent_step and how many steps there are as hidden properties, can this method then read them?
        
        
        
        def get_next_step(steps):
            global current_step
            global total_steps
            if current_step <= total_steps:
                current_step += 1
            contentToReturn = steps[current_step]
            return contentToReturn
        
        def get_previous_step(steps):
            global current_step
            if current_step > 0:
                current_step -= 1
            contentToReturn = steps[current_step]
            return contentToReturn
        
        def get_last_step(steps):
            global current_step
            global total_steps
            current_step = total_steps
            contentToReturn = steps[total_steps]
            return contentToReturn
        
        def reset_puzzle(steps):
            global current_step
            current_step = 0
            contentToReturn = steps[current_step]
            return contentToReturn
        
current_step = 0
total_steps = 0