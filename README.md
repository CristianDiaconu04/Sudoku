<h1>Sudoku</h1> 
<a href="https://skillicons.dev"> <img src="https://skillicons.dev/icons?i=python"/> </a>
<p> This game is build using Python's Pygame library. Users can play this game by either solving the default game puzzle or a custom-generated one. If stuck, a user can click the "Solve it" button to make the program display the solution.</p>

<h2>Custom Sudoku Puzzle Generation</h2>
<p> To generate a unique sudoku puzzle, a 9x9 grid is first created and filled with 0's representing empty cells. Then, the fillGrid method uses a backtracking algorithm to fill the grid with numbers. Then, some numbers are removed in order to create the final puzzle. </p>

<h2>Sudoku Solver Algorithm</h2>
<p> To solve any sudoku puzzle, I implemented a recursive backtracking algorithm. First, the algorithm iterates through each cell in the grid. For each empty cell, it attempts to place each number from 1-9 in the cell while checking to see if the placement is valid. When a valid number is found, the algorithm proceeds to the next cell recursively. If it successfully places numbers in all of the cells, the puzzle is solved. </p>
