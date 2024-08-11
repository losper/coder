#include <stdio.h>

void matrix_multiply(int a[2][2], int b[2][2], int c[2][2])
{
    c[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0];
    c[0][1] = a[0][0] * b[0][1] + a[0][1] * b[1][1];
    c[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0];
    c[1][1] = a[1][0] * b[0][1] + a[1][1] * b[1][1];
}

void matrix_power(int matrix[2][2], int n)
{
    int result[2][2] = {{1, 0}, {0, 1}};
    while (n > 0)
    {
        if (n & 1)
        {
            matrix_multiply(result, matrix, result);
        }
        matrix_multiply(matrix, matrix, matrix);
        n >>= 1;
    }
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            matrix[i][j] = result[i][j];
        }
    }
}

int fibonacci_matrix(int n)
{
    if (n <= 1)
    {
        return n;
    }
    int matrix[2][2] = {{1, 1}, {1, 0}};
    matrix_power(matrix, n - 1);
    return matrix[0][0];
}