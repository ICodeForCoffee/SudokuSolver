from nicegui import app, ui
from SudokuPuzzle import SudokuPuzzle
import copy

#This might get removed, but for now it's here.
STYLE = """
<style>
.possibleValuesCell {
    outline: 1px dotted gray;
    width: 33.33%;
    height: 33.33%;
    text-align: center;
}

.puzzleCell {
    border: 1px solid black;
    padding: 0x;
}

.puzzleCell {
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
    background-color: gray;
}

.cell-00, .cell-10, .cell-20, .cell-30, .cell-40, .cell-50, .cell-60, .cell-70, .cell-80, 
.cell-03, .cell-13, .cell-23, .cell-33, .cell-43, .cell-53, .cell-63, .cell-73, .cell-83,
.cell-06, .cell-16, .cell-26, .cell-36, .cell-46, .cell-56, .cell-66, .cell-76, .cell-86 {
    border-left: 3px solid black;
}

.cell-08, .cell-18, .cell-28, .cell-38, .cell-48, .cell-58, .cell-68, .cell-78, .cell-88 {
    border-right: 3px solid black;
}

.cell-00, .cell-01, .cell-02, .cell-03, .cell-04, .cell-05, .cell-06, .cell-07, .cell-08,
.cell-30, .cell-31, .cell-32, .cell-33, .cell-34, .cell-35, .cell-36, .cell-37, .cell-38,
.cell-60, .cell-61, .cell-62, .cell-63, .cell-64, .cell-65, .cell-66, .cell-67, .cell-68
{
    border-top: 3px solid black;
}

.cell-80, .cell-81, .cell-82, .cell-83, .cell-84, .cell-85, .cell-86, .cell-87, .cell-88
{
    border-bottom: 3px solid black;
}
</style>
"""

FOUND_CELL = """
<table class="valueCellContainer">
    <tr>
        <td class="valueCell">xyz</td>
    </tr>
</table>
"""

POSSIBLE_VALUES = """
<table class="possibleValues">
<tr>
    <td class="possibleValuesCell" data-fakeId="y1">x1</td>
    <td class="possibleValuesCell" data-fakeId="y2">x2</td>
    <td class="possibleValuesCell" data-fakeId="y3">x3</td>
</tr>
<tr>
    <td class="possibleValuesCell" data-fakeId="y4">x4</td>
    <td class="possibleValuesCell" data-fakeId="y5">x5</td>
    <td class="possibleValuesCell" data-fakeId="y6">x6</td>
</tr>
<tr>
    <td class="possibleValuesCell" data-fakeId="y7">x7</td>
    <td class="possibleValuesCell" data-fakeId="y8">x8</td>
    <td class="possibleValuesCell" data-fakeId="y9">x9</td>
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
                    found_cell = copy.deepcopy(FOUND_CELL)
                    html_fragment = found_cell.replace("xyz", str(found_value))
                    
                    
                sudoku_rendering = sudoku_rendering.replace(cell, html_fragment)
        
        #not sure yet if this method will render or just generate the code
        ui.html(sudoku_rendering)

    #this method will have to go at some point if this is to be unit tested.
    def display_puzzle_to_website(self, puzzle):
        app.native.window_args['resizable'] = False
        app.native.start_args['debug'] = True
        app.native.settings['ALLOW_DOWNLOADS'] = True
        
        ui.html(STYLE)
        ui.label('Hello NiceGUI!')
        
        self.generate_sudoku_render(puzzle)
        
        ui.button('Solve Puzzle', on_click=lambda: ui.notify('button was pressed'))
        #ui.table()
        
        #ui.run(native=True, window_size=(400, 300), fullscreen=False)
        ui.run()
