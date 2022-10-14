#include<bits/stdc++.h>
using namespace std;

#define N 5


bool isSafe_to_place(int board[N][N], int row, int col) {
    int i, j;

    for (i = 0; i < col; i++) {
        if(board[row][i]) {
            return false;
        }
    }

    for(i = row, j = col; i >= 0 and j>= 0; i--, j--) {
        if(board[i][j]) {
            return false;
        }
    }

    for(i = row, j = col; j >= 0 and i< N; i++, j--) {
        if(board[i][j]) {
            return false;
        }
    }

    return true;
}

bool solveNQueen(int board[N][N], int col) {
    if(col >= N) {
        return true;
    }

    for (int i = 0; i < N; i++) {
        if(isSafe_to_place(board, i, col)) {
            board[i][col] = 1;

            if(solveNQueen(board, col+1)) {
                return true;
            }

            board[i][col] = 0;
        }
    }

    return false;
}

void printOutput(int board[N][N]) {
    for (int i = 0; i<N; i++) {
        for(int j = 0; j < N; j++) {
            cout << board[i][j];
        }
        cout << endl;
    }
}

bool solveNQ(){
    int board[N][N] = { { 0, 0, 0, 0, 0},
                        { 0, 0, 0, 0, 0},
                        { 0, 0, 0, 0, 0},
                        { 0, 0, 0, 0, 0} };

    if(solveNQueen(board, 0) == false) {
        cout<< "Solution does not exist" << endl;
        return false;
    } 

    printOutput(board);
    return true;
}

int main(){
    solveNQ();
    return 0;
}
