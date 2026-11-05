public class Main {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3},
            {4, 0, 6},
            {7, 8, 9}
        };
        int foundRow = -1;
        int foundCol = -1;
        
        outer:
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                if (matrix[i][j] == 0) {
                    foundRow = i;
                    foundCol = j;
                    break outer;
                }
            }
        }
        
        System.out.println("Zero found at row " + foundRow + ", col " + foundCol);
    }
}