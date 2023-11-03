class Solution {
public:
    int numberOfSteps(int num) {
        int steps = 0;
        
        while (num)
        {
            if (num % 2 == 0)
                num /= 2;
            else
                num--;
            steps++;
        }
        return steps;
    }
};