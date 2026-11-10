"""
Predefined Sample Python Programs for Complex Code Testing Dashboard
"""

SAMPLE_PROGRAMS = {
    "calculator": {
        "title": "1. Scientific Calculator (Clean & Modular)",
        "description": "Standard mathematical utility with robust error handling and defensive checks.",
        "code": '''import math

class Calculator:
    """A robust scientific calculator supporting arithmetic and geometric functions."""

    def __init__(self, precision: int = 4):
        self.precision = precision
        self.history = []

    def add(self, a: float, b: float) -> float:
        """Adds two real numbers."""
        result = round(a + b, self.precision)
        self.history.append(('add', a, b, result))
        return result

    def subtract(self, a: float, b: float) -> float:
        """Subtracts b from a."""
        result = round(a - b, self.precision)
        self.history.append(('subtract', a, b, result))
        return result

    def multiply(self, a: float, b: float) -> float:
        """Multiplies two numbers."""
        result = round(a * b, self.precision)
        self.history.append(('multiply', a, b, result))
        return result

    def divide(self, a: float, b: float) -> float:
        """Divides a by b with defensive zero division safeguard."""
        if b == 0:
            raise ValueError("ZeroDivisionError: Denominator cannot be zero.")
        result = round(a / b, self.precision)
        self.history.append(('divide', a, b, result))
        return result

    def power(self, base: float, exponent: float) -> float:
        """Computes power with edge case validation."""
        if base < 0 and not exponent.is_integer():
            raise ValueError("Negative base cannot have fractional exponent.")
        return round(math.pow(base, exponent), self.precision)

    def square_root(self, val: float) -> float:
        """Computes square root of non-negative real value."""
        if val < 0:
            raise ValueError("Cannot calculate square root of negative number.")
        return round(math.sqrt(val), self.precision)

    def clear_history(self) -> None:
        """Clears calculation ledger."""
        self.history.clear()


if __name__ == '__main__':
    calc = Calculator()
    print("Add:", calc.add(15.5, 4.5))
    print("Divide:", calc.divide(100, 4))
    print("Sqrt:", calc.square_root(144))
'''
    },
    "bank_account": {
        "title": "2. Banking & Ledger System (Stateful & Defensive)",
        "description": "Demonstrates multi-branch banking business logic, transaction limits, and status states.",
        "code": '''import datetime

class BankAccount:
    """Manages transactional lifecycle, deposits, withdrawals, and balance verification."""

    def __init__(self, account_number: str, holder_name: str, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = float(initial_balance)
        self.is_active = True
        self.transactions = []

    def deposit(self, amount: float) -> float:
        if not self.is_active:
            raise RuntimeError("Account is suspended or closed.")
        if amount <= 0:
            raise ValueError("Deposit amount must be strictly positive.")
        
        self.balance += amount
        self.transactions.append({
            'type': 'DEPOSIT',
            'amount': amount,
            'timestamp': datetime.datetime.now().isoformat(),
            'balance_after': self.balance
        })
        return self.balance

    def withdraw(self, amount: float) -> float:
        if not self.is_active:
            raise RuntimeError("Account is frozen.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance in account.")
        
        self.balance -= amount
        self.transactions.append({
            'type': 'WITHDRAWAL',
            'amount': amount,
            'timestamp': datetime.datetime.now().isoformat(),
            'balance_after': self.balance
        })
        return self.balance

    def close_account(self) -> float:
        if self.balance > 0:
            payout = self.balance
            self.balance = 0.0
            self.is_active = False
            return payout
        self.is_active = False
        return 0.0


if __name__ == '__main__':
    acct = BankAccount("ACC-9021", "Amogh Patil", 5000.0)
    acct.deposit(1200.0)
    acct.withdraw(800.0)
    print(f"Final Balance: ${acct.balance}")
'''
    },
    "ecommerce_cart": {
        "title": "3. E-Commerce Cart & Discount Matrix (High Branching)",
        "description": "Simulates pricing tier evaluation, discount matrices, taxation, and coupons.",
        "code": '''class CartItem:
    def __init__(self, item_id: str, name: str, price: float, quantity: int = 1):
        if price < 0 or quantity <= 0:
            raise ValueError("Invalid item pricing or quantity parameters.")
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self) -> float:
        return self.price * self.quantity


class ShoppingCart:
    """Complex business rules for discounts, promotional coupons, and GST taxes."""

    TAX_RATE = 0.18

    def __init__(self):
        self.items = {}
        self.applied_coupon = None

    def add_item(self, item: CartItem):
        if item.item_id in self.items:
            self.items[item.item_id].quantity += item.quantity
        else:
            self.items[item.item_id] = item

    def apply_coupon(self, code: str) -> bool:
        valid_coupons = {'SAVE10': 0.10, 'FESTIVE20': 0.20, 'SDM50': 0.50}
        clean_code = code.strip().upper()
        if clean_code in valid_coupons:
            self.applied_coupon = (clean_code, valid_coupons[clean_code])
            return True
        return False

    def calculate_subtotal(self) -> float:
        return sum(item.total() for item in self.items.values())

    def calculate_discount(self) -> float:
        subtotal = self.calculate_subtotal()
        if not self.applied_coupon:
            return 0.0
        _, rate = self.applied_coupon
        return subtotal * rate

    def calculate_final_total(self) -> float:
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        discounted = max(0.0, subtotal - discount)
        tax = discounted * self.TAX_RATE
        return round(discounted + tax, 2)


if __name__ == '__main__':
    cart = ShoppingCart()
    cart.add_item(CartItem("ITM01", "Software Testing Textbook", 850.0, 1))
    cart.add_item(CartItem("ITM02", "Notebook", 60.0, 3))
    cart.apply_coupon("FESTIVE20")
    print("Final Payable with Tax:", cart.calculate_final_total())
'''
    },
    "vulnerable_code": {
        "title": "4. Defect & Vulnerability Probe (Triggers Linter & Security Warnings)",
        "description": "Intentionally contains dangerous patterns (eval, hardcoded token, long line, unused var) to demonstrate tool failure detection.",
        "code": '''import hashlib

# INTENTIONAL TESTING SAMPLE: Contains deliberate antipatterns to test analyzers
SECRET_API_TOKEN = "sk-live-99283489234823948239"  # Hardcoded secret warning

def execute_dynamic_calculation(user_formula):
    # DANGEROUS: eval call should trigger Bandit Security warning!
    result = eval(user_formula)
    unused_debug_variable = 42
    return result

def generate_legacy_hash(data_string):
    # INSECURE: MD5 hash triggers Bandit & SpotBugs warning
    hasher = hashlib.md5()
    hasher.update(data_string.encode('utf-8'))
    return hasher.hexdigest()

def long_and_unformatted_routine_demonstrating_pep8_violations_and_excessive_character_length_in_a_single_source_line(x, y):
    return x * y + 100
'''
    }
}
