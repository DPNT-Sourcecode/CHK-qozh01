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

    def test_checkout_Illigal_chars(self):
        assert checkout_solution.checkout("ABJKCD") == -1

    def test_checkout_2E(self):
        assert checkout_solution.checkout("EE") == 80

    def test_checkout_2E1B(self):
        assert checkout_solution.checkout("EEB") == 80

    def test_checkout_5A(self):
        assert checkout_solution.checkout("EEEEE") == -1

    def test_checkout_3A(self):
        assert checkout_solution.checkout("AAA") == 130
    
    def test_checkout_8A(self):
        assert checkout_solution.checkout("AAAAAA") == 

