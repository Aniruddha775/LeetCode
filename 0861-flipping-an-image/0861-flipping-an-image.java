class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        for (int[] row : image) {
            //reverse the array
            for (int i = 0; i < (image[0].length + 1) / 2; i++) {
                //swap
                int temp = row[i] ^ 1;
                row[i] = row[image[0].length - i - 1] ^ 1; // as xor any number with 1 gives the invert of that number
                row[image[0].length - i - 1] = temp;
            }

        }
        return image;
    }
}
