class Solution {
public:
    int countOdds(int low, int high) {
        int odds_low = (low + 1) / 2;
        int odds_high = (high + 1) / 2;
        
        int ans = odds_high - odds_low;
        ans += low % 2 != 0 ? 1 : 0;
        return ans;
    }
};