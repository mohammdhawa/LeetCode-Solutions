class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        d = {'lower': False, 'upper': False, 'digit': False, 'special': False}

        for idx in range(len(password)):
            char = password[idx]
            if idx > 0 and password[idx - 1] == char:
                return False
            if char.isdigit():
                d['digit'] = True
            if char.isupper():
                d['upper'] = True
            if char.islower():
                d['lower'] = True
            if char in '!@#$%^&*()-+':
                d['special'] = True

        return all(d.values())