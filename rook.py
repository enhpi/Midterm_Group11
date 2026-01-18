def safeRooks(n, rooks):
    # Track occupied rows and columns
    occupied_rows = set()
    occupied_cols = set()
    for r, c in rooks:
        occupied_rows.add(r)
        occupied_cols.add(c)

    # Calculation of safe squares
    emptyRows = n - len(occupied_rows)
    emptyCols = n - len(occupied_cols)
    safe_count = emptyRows * emptyCols

    # Print the matrix
    for i in range(n):
        row_str = ""
        for j in range(n):
            if i in occupied_rows or j in occupied_cols:
                cell_value = 1
            else:
                cell_value = 0
            row_str += f"{cell_value}\t"
        print(row_str)

    return safe_count
 
try:
    n = int(input("Enter board size (n): "))
    while n <= 0:
        print("Board size must be a positive integer.")
        n = int(input("Enter board size (n): "))

    numRooks = int(input("Enter number of rooks to place: "))
    while numRooks < 0 or numRooks > n * n:
        print(f"Invalid number of rooks! Must be between 0 and {n * n}.")
        numRooks = int(input("Enter number of rooks to place: "))

    rooksList = []
    for i in range(numRooks):
        print(f"\nEntering coordinates for Rook {i + 1}:")
        r = int(input(f"  Row (0 to {n - 1}): "))
        c = int(input(f"  Col (0 to {n - 1}): "))

        # Coordinate validation
        if 0 <= r < n and 0 <= c < n:
            rooksList.append((r, c))
        else:
            print(f"  Invalid position! Must be between 0 and {n - 1}. Skipping this rook.")

    result = safeRooks(n, rooksList)
    print(f"\nTotal safe squares: {result}")

except ValueError:
    print("Please enter valid integers only.")