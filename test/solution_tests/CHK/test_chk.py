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

    def test_checkout_2E3B(self):
        assert checkout_solution.checkout("EEBBB") == 125

    def test_checkout_2E2B(self):
        assert checkout_solution.checkout("EEBB") == 110

    def test_checkout_5A(self):
        assert checkout_solution.checkout("AAAAA") == 200

    def test_checkout_3A(self):
        assert checkout_solution.checkout("AAA") == 130
    
    def test_checkout_8A(self):
        assert checkout_solution.checkout("AAAAAAAA") == 330

    def test_checkout_9A(self):
        assert checkout_solution.checkout("AAAAAAAAA") == 380

    def test_checkout_2F(self):
        assert checkout_solution.checkout("FF") == 20
    
    def test_checkout_3F(self):
        assert checkout_solution.checkout(3*"F") == 20

    def test_checkout_5F(self):
        assert checkout_solution.checkout(5*"F") == 40

    def test_checkout_6F(self):
        assert checkout_solution.checkout(5*"F") == 40