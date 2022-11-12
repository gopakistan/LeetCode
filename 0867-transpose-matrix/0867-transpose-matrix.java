class Solution {
    public int[][] transpose(int[][] matrix) {
        int[][] matrix2 = new int[matrix[0].length][matrix.length];
        //System.out.println(matrix.length + " " + matrix[0].length);
        
        for (int i = 0; i < matrix.length; i++){
            for (int j = 0; j < matrix[0].length; j++){
                //System.out.println(matrix[j][i]);
                matrix2[j][i] = matrix[i][j];
            }
        }
        return matrix2;
    }
}