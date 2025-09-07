import sys

def search_matrix(matrix, m, n, s):
    for row in range(m):
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == s:
                # Move left to find the first occurrence in this row
                while mid > 0 and matrix[row][mid - 1] == s:
                    mid -= 1
                return f"{row} {mid}"
            elif matrix[row][mid] < s:
                left = mid + 1
            else:
                right = mid - 1
    return "None"

def main():
    input_data = sys.stdin.read().strip().splitlines()
    idx = 0

    while idx < len(input_data):
        m, n, k = map(int, input_data[idx].split())
        idx += 1
        if m == 0 and n == 0 and k == 0:
            break

        # Read the matrix
        matrix = []
        for _ in range(m):
            row = list(map(int, input_data[idx].split()))
            idx += 1
            matrix.append(row)

        # Process each query
        for _ in range(k):
            s = int(input_data[idx])
            idx += 1
            print(search_matrix(matrix, m, n, s))

if __name__ == "__main__":
    main()
