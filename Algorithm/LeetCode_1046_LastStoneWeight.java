package Greedy;

import java.util.Arrays;

public class LeetCode_1046_LastStoneWeight {

    public static int lastStoneWeight(int[] stones) {

        if (stones.length == 1)
            return stones[0];

        int lastWeight = 0;
        int len = stones.length;
        boolean foundRes = true;

        while (foundRes) {
            Arrays.sort(stones);

            if (stones[len - 2] == 0) {
                return stones[len - 1];
            } else {
                stones[len - 1] = stones[len - 1] - stones[len - 2];
                stones[len - 2] = 0;
            }
        }

        return lastWeight;
    }

    public static void main(String[] args) {
        int[] array = {1,1,2,4,7,8};
        System.out.println(lastStoneWeight(array));
    }

}
