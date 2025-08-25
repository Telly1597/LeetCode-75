class Solution:
    def tribonacci(self, n: int) -> int: 
        if n == 0:
            return 0
        elif n <= 2:
            return 1

        value = 0
        last_val, second_to_last, third_to_last = 0, 1, 1
        for i in range(3, n + 1):
            last_val, second_to_last, third_to_last = second_to_last, third_to_last, last_val +  second_to_last +  third_to_last


        return third_to_last