# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================





##include <iostream>
#include <iomanip>
using namespace std;

// Function to display a matrix
void displayMatrix(int matrix[10][10], int rows, int cols)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            cout << setw(5) << matrix[i][j];
        }
        cout << endl;
    }
}

// Function to transpose a matrix
void transposeMatrix(int matrix[10][10], int transpose[10][10], int rows, int cols)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            transpose[j][i] = matrix[i][j];
        }
    }
}

// Function to add two matrices
void addMatrices(int A[10][10], int B[10][10], int sum[10][10], int rows, int cols)
{
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < cols; j++)
        {
            sum[i][j] = A[i][j] + B[i][j];
        }
    }
}

// Function to multiply two matrices
void multiplyMatrices(int A[10][10], int B[10][10], int product[10][10], int rowsA, int colsA, int colsB)
{
    for (int i = 0; i < rowsA; i++)
    {
        for (int j = 0; j < colsB; j++)
        {
            product[i][j] = 0;

            for (int k = 0; k < colsA; k++)
            {
                product[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main()
{
    int choice;

    cout << "========== Matrix Operations ==========" << endl;
    cout << "1. Transpose Matrix" << endl;
    cout << "2. Add Two Matrices" << endl;
    cout << "3. Multiply Two Matrices" << endl;
    cout << "Enter your choice: ";
    cin >> choice;

    if (choice == 1)
    {
        int matrix[10][10], transpose[10][10];
        int rows, cols;

        cout << "Enter number of rows: ";
        cin >> rows;

        cout << "Enter number of columns: ";
        cin >> cols;

        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                cout << "Enter element [" << i << "][" << j << "]: ";
                cin >> matrix[i][j];
            }
        }

        transposeMatrix(matrix, transpose, rows, cols);

        cout << "\nOriginal Matrix:\n";
        displayMatrix(matrix, rows, cols);

        cout << "\nTransposed Matrix:\n";
        displayMatrix(transpose, cols, rows);
    }
    else if (choice == 2)
    {
        int A[10][10], B[10][10], sum[10][10];
        int rows, cols;

        cout << "Enter number of rows: ";
        cin >> rows;

        cout << "Enter number of columns: ";
        cin >> cols;

        cout << "\nEnter elements of Matrix A:\n";
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                cout << "Enter element [" << i << "][" << j << "]: ";
                cin >> A[i][j];
            }
        }

        cout << "\nEnter elements of Matrix B:\n";
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                cout << "Enter element [" << i << "][" << j << "]: ";
                cin >> B[i][j];
            }
        }

        addMatrices(A, B, sum, rows, cols);

        cout << "\nMatrix A:\n";
        displayMatrix(A, rows, cols);

        cout << "\nMatrix B:\n";
        displayMatrix(B, rows, cols);

        cout << "\nSum Matrix:\n";
        displayMatrix(sum, rows, cols);
    }
    else if (choice == 3)
    {
        int A[10][10], B[10][10], product[10][10];
        int rowsA, colsA, rowsB, colsB;

        cout << "Enter rows of Matrix A: ";
        cin >> rowsA;

        cout << "Enter columns of Matrix A: ";
        cin >> colsA;

        cout << "\nEnter elements of Matrix A:\n";
        for (int i = 0; i < rowsA; i++)
        {
            for (int j = 0; j < colsA; j++)
            {
                cout << "Enter element [" << i << "][" << j << "]: ";
                cin >> A[i][j];
            }
        }

        cout << "\nEnter rows of Matrix B: ";
        cin >> rowsB;

        cout << "Enter columns of Matrix B: ";
        cin >> colsB;

        if (colsA != rowsB)
        {
            cout << "\nMatrix multiplication is not possible." << endl;
            return 0;
        }

        cout << "\nEnter elements of Matrix B:\n";
        for (int i = 0; i < rowsB; i++)
        {
            for (int j = 0; j < colsB; j++)
            {
                cout << "Enter element [" << i << "][" << j << "]: ";
                cin >> B[i][j];
            }
        }

        multiplyMatrices(A, B, product, rowsA, colsA, colsB);

        cout << "\nMatrix A:\n";
        displayMatrix(A, rowsA, colsA);

        cout << "\nMatrix B:\n";
        displayMatrix(B, rowsB, colsB);

        cout << "\nProduct Matrix:\n";
        displayMatrix(product, rowsA, colsB);
    }
    else
    {
        cout << "Invalid choice!" << endl;
    }

    return 0;
}