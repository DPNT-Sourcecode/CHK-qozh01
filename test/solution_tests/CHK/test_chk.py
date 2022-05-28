from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout(self):
        assert checkout_solution.checkout("ABCD") == 115

    def test_checkout_3A(self):
        assert checkout_solution.checkout("ABACAD") == 195

    def test_checkout_5C(self):
        assert checkout_solution.checkout("CCCCC") == 100

    def test_checkout_5B(self):
        assert checkout_solution.checkout("BBBBB") == 120
