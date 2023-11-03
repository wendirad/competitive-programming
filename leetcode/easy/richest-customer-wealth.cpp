class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int MAX = 0, total;
        for (vector<int>v: accounts)
        {
            total = accumulate(v.begin(), v.end(), 0);
            MAX = max(total, MAX);
        }
        return MAX;
    }
};