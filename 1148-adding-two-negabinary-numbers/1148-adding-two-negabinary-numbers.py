class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n, m = len(arr1), len(arr2)
        answer = []

        carry = 0
        i = n - 1
        j = m - 1

        while i >= 0 or j >= 0 or carry:
            a_bit = arr1[i] if i >= 0 else 0
            b_bit = arr2[j] if j >= 0 else 0
            res = a_bit + b_bit + carry
            
            if res == 0:
                digit, carry = 0, 0
            elif res == 1:
                digit, carry = 1, 0
            elif res == 2:
                digit, carry = 0, -1
            elif res == 3:
                digit, carry = 1, -1
            elif res == -1:
                digit, carry = 1, 1
            else:
                digit, carry = 0, 0

            answer.append(digit)
            i -= 1
            j -= 1
        
        # Remove leading zerso from the most significant side
        while len(answer) > 1 and answer[-1] == 0:
            answer.pop()
        
        return answer[::-1]