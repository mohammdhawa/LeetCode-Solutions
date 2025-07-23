class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        result = 0
        while mainTank >= 0:
            temp = mainTank - 5
            if temp >= 0:
                result += 50
                if additionalTank > 0:
                    mainTank = temp + 1
                    additionalTank -= 1
                else:
                    mainTank = temp
            else:
                result += mainTank * 10
                mainTank = temp
        return result