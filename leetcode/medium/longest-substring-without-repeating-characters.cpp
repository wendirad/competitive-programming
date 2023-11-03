class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start = 0, max_len = 0, n = s.length(), i= 1, current;
        if (n < 2) return n;
        map<char, int> umap;
        umap[s[0]] = 0;
        for (;i < n; i++)
        {
            if (umap.find(s[i]) != umap.end() && umap[s[i]] >= start)
            {   
                current = i - start;
                max_len = max(max_len, current);                
                start = umap[s[i]] + 1;
            }
            umap[s[i]] = i;
            
        }
        current = i - start;
        max_len = max(max_len, current);
        return max_len;
    }
};