class Solution:
    def rotatedDigits(self, n: int) -> int:
        dp = {'0': '0', '1': '1', '8': '8', '2': '5', '5': '2', '6': '9', '9': '6'}
        count = 0

        for i in range(1, n + 1):
            num_str = str(i)
            valid = False

            if num_str in dp:
                valid = True
                temp = dp[num_str]
            else:
                temp = ''
                for ch in num_str:
                    if ch in dp:
                        temp += dp[ch]
                    else:
                        valid = False
                        break
                    valid = True

            if valid and temp != num_str:
                dp[num_str] = temp
                dp[temp] = num_str
                count += 1


        return count