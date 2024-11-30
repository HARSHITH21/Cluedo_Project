# test_solution_selector.py

from solution_selector import select_solution, display_solution

if __name__ == "__main__":
    # Generate a random solution
    solution = select_solution()

    # Display the solution (for testing only)
    display_solution(solution)
