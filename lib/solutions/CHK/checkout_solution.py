

# noinspection PyUnusedLocal
# skus = unicode string

allowed_values = "ABCDEF"


def three_price_calc(count, price1, price3, price5, qty1, qty2, qty3):
    remainder = count

    quotient5 = remainder // qty3
    remainder = remainder % qty3

    quotient3 = remainder // qty2
    remainder = remainder % qty2

    quotient1 = remainder // qty1

    return quotient5 * price5 + quotient3 * price3 + quotient1 * price1


def two_price_calc(count, price1, price2, offer_multiple):

    quotient = count // offer_multiple
    remainder = count % offer_multiple

    return remainder * price1 + quotient * price2


def single_price_calc(count, one_price):
    return count * one_price


def buy_n_get_k_free_calc(count, single_price, n, k):
    quotient = count // (n+k)
    remainder = count % (n+k)

    return quotient * single_price * n + remainder * single_price


def get_free_Bs(E_count):
    return E_count//2


def get_free_Fs(F_count):
    return F_count//2


def isinput_sanitised(skus):
    # Check if there are no values outside of ABCD
    # if so, return false
    for i in skus:
        if i not in allowed_values:
            return False
    return True


def special_minus(B_counts, free_Bs):

    # minus off Bs until its zero.
    if (B_counts - free_Bs) > 0:
        B_counts = B_counts - free_Bs
    else:
        B_counts = 0

    return B_counts


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
    F_counts = skus.count('F')

    # minus off Bs until its zero
    free_Bs = get_free_Bs(E_counts)
    B_counts = special_minus(B_counts, free_Bs)

    total = 0
    total += three_price_calc(A_counts, 50, 130, 200, 1, 3, 5)
    total += two_price_calc(B_counts, 2, 30, 45)
    total += single_price_calc(C_counts, C_one_price)
    total += single_price_calc(D_counts, D_one_price)
    total += single_price_calc(E_counts, 40)
    total += buy_n_get_k_free_calc(F_counts, 10, 2, 1)

    return total





