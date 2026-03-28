class Solution {
    public void gameOfLife(int[][] board) {
        int m = board.length;
        int n = board[0].length;

        int[][] dirs = {
            {-1,-1}, {-1,0}, {-1,1},
            {0,-1},         {0,1},
            {1,-1}, {1,0}, {1,1}
        };

        // Step 1: Apply rules using encoded states
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                int liveNeighbors = 0;

                for (int[] d : dirs) {
                    int ni = i + d[0];
                    int nj = j + d[1];

                    if (ni >= 0 && ni < m && nj >= 0 && nj < n 
                        && Math.abs(board[ni][nj]) == 1) {
                        liveNeighbors++;
                    }
                }

                // Apply rules
                if (board[i][j] == 1) {
                    if (liveNeighbors < 2 || liveNeighbors > 3) {
                        board[i][j] = -1; // live → dead
                    }
                } else {
                    if (liveNeighbors == 3) {
                        board[i][j] = 2; // dead → live
                    }
                }
            }
        }

        // Step 2: Finalize states
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] > 0) board[i][j] = 1;
                else board[i][j] = 0;
            }
        }
    }
}