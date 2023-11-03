class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int unique = nums[0], n = nums.size();
        for(int i = 1; i < n; i++)
            unique ^= nums[i];
        return unique;
    }
};