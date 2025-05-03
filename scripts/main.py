""" Module to count islands from a file """
import sys
from typing import List

class IslandCounter:
    """
    Class to count the number of islands in a matrix read from a file.
    Each island is defined as a group of connected '1's surrounded by '0's.
    """

    def __init__(self, matrix: List[List[str]]) -> None:
        """
        Initializes the matrix and visited matrix for counting islands.
        
        Args:
            matrix (List[List[str]]): 2D grid with '1' for land and '0' for water.
        """
        self.matrix: List[List[str]] = matrix
        self.rows: int = len(matrix)
        self.cols: int = len(matrix[0]) if matrix else 0
        self.visited: List[List[bool]] = [[False] * self.cols for _ in range(self.rows)]

    def count_islands(self) -> int:
        """Counts and returns the number of islands in the matrix."""
        island_count: int = 0

        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] not in ['1', '0']:
                    raise ValueError("Error: Input array has invalid characters.")

                if self.matrix[i][j] == '1' and not self.visited[i][j]:
                    # New island found, trigger DFS
                    self._dfs(i, j)
                    island_count += 1

        return island_count

    def _dfs(self, r: int, c: int) -> None:
        """
        Depth-First Search to mark all connected land cells as visited.
        
        Args:
            r (int): Row index of the cell.
            c (int): Column index of the cell.
        """
        # Boundary and visit checks
        if (r < 0 or r >= self.rows or c < 0 or c >= self.cols or
                self.visited[r][c] or self.matrix[r][c] == '0'):
            return

        self.visited[r][c] = True

        # Visit all 8 neighbors
        self._dfs(r - 1, c)  # Up
        self._dfs(r + 1, c)  # Down
        self._dfs(r, c - 1)  # Left
        self._dfs(r, c + 1)  # Right
        self._dfs(r + 1, c + 1)  # Down-right
        self._dfs(r - 1, c - 1)  # Up-left
        self._dfs(r + 1, c - 1)  # Down-left
        self._dfs(r - 1, c + 1)  # Up-right

    @classmethod
    def from_file(cls, filepath: str) -> 'IslandCounter':
        """
        Reads a matrix from a file and returns an IslandCounter instance.
        
        Args:
            filepath (str): Path to the input file.
            
        Returns:
            IslandCounter: Instance of IslandCounter initialized with the matrix.
        """
        if not filepath.endswith(".txt"):
            raise FileNotFoundError("Error: Invalid file path.")
        matrix: List[List[str]] = []
        try:
            with open(filepath, 'r') as file:
                for line in file:
                    row = line.strip().split()  # Split by spaces
                    matrix.append(row)
        except Exception as e:
            print(f"Error reading file: {e}", file=sys.stderr)
            sys.exit(1)

        return cls(matrix)

def main(filepath: str) -> None:
    """Main function to initialize the IslandCounter and print the island count."""
    counter = IslandCounter.from_file(filepath)
    num_islands = counter.count_islands()
    print(str(num_islands))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_input_file>", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1])
