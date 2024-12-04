class Solution {
    public static int rotate(int x1, int y1, int x2, int y2, int[][] matrix) {
        int first = matrix[x1][y1]; // 테두리의 첫 번째 값
        int minValue = first;      // 최소값 초기화

        // 왼쪽 세로줄
        for (int k = x1; k < x2; k++) {
            matrix[k][y1] = matrix[k + 1][y1];
            minValue = Math.min(minValue, matrix[k + 1][y1]);
        }

        // 아래쪽 가로줄
        for (int k = y1; k < y2; k++) {
            matrix[x2][k] = matrix[x2][k + 1];
            minValue = Math.min(minValue, matrix[x2][k + 1]);
        }

        // 오른쪽 세로줄
        for (int k = x2; k > x1; k--) {
            matrix[k][y2] = matrix[k - 1][y2];
            minValue = Math.min(minValue, matrix[k - 1][y2]);
        }

        // 위쪽 가로줄
        for (int k = y2; k > y1; k--) {
            matrix[x1][k] = matrix[x1][k - 1];
            minValue = Math.min(minValue, matrix[x1][k - 1]);
        }

        // 저장해둔 첫 번째 값 삽입
        matrix[x1][y1 + 1] = first;

        return minValue;
    }


    public int[] solution(int rows, int columns, int[][] queries) {
        int[][] matrix = new int[rows][columns];
        int[] answer = new int[queries.length];
        int index = 0;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                matrix[i][j] = i * columns + (j + 1);
            }
        }

        for (int[] query : queries) {
            int x1 = query[0] - 1;
            int y1 = query[1] - 1;
            int x2 = query[2] - 1;
            int y2 = query[3] - 1;

            answer[index++] = rotate(x1, y1, x2, y2, matrix);
        }

        return answer;
    }
}