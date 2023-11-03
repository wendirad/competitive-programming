class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int ran_len = ransomNote.length(), mag_len = magazine.length();
        unordered_map <char, int> m;
        for (char i: magazine) m[i]++;
        for (char j: ransomNote)
            if (--m[j] < 0)
                return false;
        return true;
        
    }
};