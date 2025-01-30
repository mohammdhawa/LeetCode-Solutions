class Bank:

    def __init__(self, balance):
        self.accounts = {idx+1: val for idx, val in enumerate(balance)}

    def _validate_account(self, account):
        return self.accounts.get(account) is not None

    def _validate_balance(self, account, balance):
        return self._validate_account(account) and self.accounts[account] >= balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self._validate_balance(account1, money) and self._validate_account(account2):
            if account1 == account2:
                return True
            self.accounts[account2] += money
            self.accounts[account1] -= money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if not self._validate_account(account):
            return False
        self.accounts[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._validate_balance(account, money):
            return False
        self.accounts[account] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)