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
        assert checkout_solution.checkout("ABnKCD") == -1

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

    def test_checkout_2K(self):
        assert checkout_solution.checkout(2*"K") == 120

    def test_checkout_1K(self):
        assert checkout_solution.checkout(1*"K") == 70

    def test_checkout_VVVV(self):
        assert checkout_solution.checkout("VVVV") == 180

    def test_checkout_RRRQQ(self):
        assert checkout_solution.checkout("RRRQQ") == 180

    def test_checkout_W(self):
        assert checkout_solution.checkout("W") == 20

    def test_checkout_STXYZA(self):
        expected = 45 + 50 + 17 + 20
        assert checkout_solution.checkout("STXYZA") == expected
        
    def test_checkout_STXYZ(self):
        expected = 45 + 17 + 20
        assert checkout_solution.checkout("STXYZ") == expected

    def test_checkout_SSS(self):
        assert checkout_solution.checkout("SSS") == 45

    def test_checkout_SSSZ(self):
        assert checkout_solution.checkout("SSSZ") == 65

    def test_checkout_ZZZ(self):
        assert checkout_solution.checkout("ZZZ") == 45

class TestMultiOffer():
    def test_multi_offer(self):
        cost, _ = checkout_solution.calc_any_three_of_STXYZ("STXYZ")
        assert cost == 45

    def test_multi_offer2(self):
        cost, _ = checkout_solution.calc_any_three_of_STXYZ("STXYZZ")
        assert cost == 90
