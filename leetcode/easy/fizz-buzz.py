class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz_buzz = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                fizz_buzz.append("FizzBuzz")
            elif i % 3 == 0:
                fizz_buzz.append("Fizz")
            elif i % 5 == 0:
                fizz_buzz.append("Buzz")
            else:
                fizz_buzz.append("%d" % i)
        return fizz_buzz
