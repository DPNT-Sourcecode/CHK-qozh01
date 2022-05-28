

# noinspection PyUnusedLocal
# skus = unicode string

allowed_values = "ABCDE"


def multi_price_calc_A(count, price1, price3, price5):
    remainder = count

    quotient5 = remainder // 5
    remainder = remainder % 5

    quotient3 = remainder // 3
    remainder = remainder % 3

    quotient1 = remainder // 1

    return quotient5 * price5 + quotient3 * price3 + quotient1 * price1


def multi_price_calc(count, offer_multiple, one_price, muliple_price):

    quotient = count // offer_multiple
    remainder = count % offer_multiple

    return remainder * one_price + quotient * muliple_price


def single_price_calc(count, one_price):
    return count * one_price


def get_free_Bs(E_count):
    return E_count//2


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

    free_Bs = get_free_Bs(E_counts)

    # minus off Bs until its zero.
    if (B_counts - free_Bs) > 0:
        B_counts = B_counts - free_Bs
    else:
        B_counts = 0

    total = 0
    total += multi_price_calc_A(A_counts, 50, 130, 200)
    total += multi_price_calc(B_counts, 2, 30, 45)
    total += single_price_calc(C_counts, C_one_price)
    total += single_price_calc(D_counts, D_one_price)
    total += single_price_calc(E_counts, 40)

    return total



