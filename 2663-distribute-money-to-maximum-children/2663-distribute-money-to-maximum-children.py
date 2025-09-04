class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1

        money -= children

        max_eight = money // 7

        if max_eight == children and money % 7 == 0:
            return max_eight

        if max_eight >= children:
            return children - 1

        remaining_money = money - (max_eight * 7)

        if children - max_eight  == 1:
            if remaining_money == 3:
                return max_eight - 1
            return max_eight

        if remaining_money > 0:
            return max_eight
        return max_eight