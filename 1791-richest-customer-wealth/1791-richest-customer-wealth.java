class Solution {
    public int maximumWealth(int[][] accounts) {
        int ans=Integer.MIN_VALUE;
                for (int[] account : accounts) {
                            int sum = 0;
                                        for (int i : account) {
                                                        sum += i;
                                                                    }
                                                                                if (ans < sum) {
                                                                                                ans = sum;
                                                                                                            }
                                                                                                                    }
                                                                                                                            return ans;
    }
}