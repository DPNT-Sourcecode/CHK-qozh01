

# noinspection PyUnusedLocal
# skus = unicode string

allowed_values = "ABCDE"


def multi_price_calc_A(count, price1, price3, price5):
    remainder = count

    quotient5 = remainder // price5
    remainder = remainder % price5

    quotient3 = remainder // price3
    remainder = remainder % price3

    quotient1 = remainder // price1

    return remainder * one_price + quotient * muliple_price


def multi_price_calc(count, offer_multiple, one_price, muliple_price):

    quotient = count // offer_multiple
    remainder = count % offer_multiple

    return remainder * one_price + quotient * muliple_price


def single_price_calc(count, one_price):
    return count * one_price


def buy_one_get_one_free(count, one_price, offer_bundle):
    return 0


def isinput_sanitised(skus):
    # Check if there are no values outside of ABCD
    # if so, return false
    for i in skus:
        if i not in allowed_values:
            return False
    return True


def checkout(skus):
    if not isinput_sanitised(skus):
        return -1

    C_one_price = 20
    D_one_price = 15

    A_counts = skus.count('A')
    B_counts = skus.count('B')
    C_counts = skus.count('C')
    D_counts = skus.count('D')
    E_counts = skus.count('E')

    total = 0
    total += multi_price_calc_A(A_counts, 50, 130, 200)
    total += multi_price_calc(B_counts, 2, 30, 45)
    total += single_price_calc(C_counts, C_one_price)
    total += single_price_calc(D_counts, D_one_price)
    # total += buy_one_get_one_free(E_counts, 40, )

    return total
