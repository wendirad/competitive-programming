class Solution {
public:
    bool isValid(string s) {
        stack<char> pars;
        char t;
        if (s.length() < 2) return false;
        for (char c: s)
        {
            if (isOpening(c))
            {
                pars.push(c);
            } else {
                if (pars.empty())
                    return false;
                t = pars.top();
                pars.pop();
                if (!isMatch(t, c)) {
                    return false;
                }
            }
        }
        if (pars.empty())
            return true;
        return false;
    }
    bool isOpening(char c)
    {
        return c == '(' or c == '[' or c == '{';
    }
    bool isMatch(char t, char c)
    {
        return ((t == '(' && c == ')') or (t == '[' && c == ']') or (t == '{' && c == '}'));
    }
};