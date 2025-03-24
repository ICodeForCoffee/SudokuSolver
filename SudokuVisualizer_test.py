from SudokuSolver import SudokuSolver
from SudokuPuzzle import SudokuPuzzle
from SudokuVisualizer import SudokuVisualizer
import pytest

def test_generate_possible_values_html():
    visualizer = SudokuVisualizer()
    
    possible_values = [1, 5, 8]
    result = visualizer.generate_possible_values_html(possible_values)
    
    expected_result = """
        <table class="possibleValues">
            <tr>
                <td class="possibleValuesCell">1</td>
                <td class="possibleValuesCell">&nbsp;</td>
                <td class="possibleValuesCell">&nbsp;</td>
            </tr>
            <tr>
                <td class="possibleValuesCell">&nbsp;</td>
                <td class="possibleValuesCell">5</td>
                <td class="possibleValuesCell">&nbsp;</td>
            </tr>
            <tr>
                <td class="possibleValuesCell">&nbsp;</td>
                <td class="possibleValuesCell">8</td>
                <td class="possibleValuesCell">&nbsp;</td>
            </tr>
        </table>
    """
    
    #I had issues with the number of spaces coming in.
    #Solution: Remove all spaces and then restore them when needed to retain valid html.
    result = result.replace(" ", "").replace("tableclass", "table class").replace("tdclass", "td class")
    expected_result = expected_result.replace(" ", "").replace("tableclass", "table class").replace("tdclass", "td class")
    
    assert result == expected_result
    
    #check a different matrix.
    possible_values = [4]
    result = visualizer.generate_possible_values_html(possible_values)
    
    expected_result = """
        <table class="possibleValues">
            <tr>
                <td class="possibleValuesCell">&nbsp;</td>
                <td class="possibleValuesCell">&nbsp;</td>
                <td class="possibleValuesCell">&nbsp;</td>
            </tr>
            <tr>
                <td class="possibleValuesCell">4</td>
                <td class="possibleValuesCell">&nbsp;</td>
                <td class="possibleValuesCell">&nbsp;</td>
            </tr>
            <tr>
                <td class="possibleValuesCell">&nbsp;</td>
                <td class="possibleValuesCell">&nbsp;</td>
                <td class="possibleValuesCell">&nbsp;</td>
            </tr>
        </table>
    """
    
    #Same as above
    result = result.replace(" ", "").replace("tableclass", "table class").replace("tdclass", "td class")
    expected_result = expected_result.replace(" ", "").replace("tableclass", "table class").replace("tdclass", "td class")
    
    assert result == expected_result