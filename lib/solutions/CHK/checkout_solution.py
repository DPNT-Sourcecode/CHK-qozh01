

# noinspection PyUnusedLocal
# skus = unicode string

allowed_values = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def three_price_calc(count, price1, price3, price5, qty1, qty2, qty3):
    remainder = count

    quotient5 = remainder // qty3
    remainder = remainder % qty3

    quotient3 = remainder // qty2
    remainder = remainder % qty2

    quotient1 = remainder // qty1

    return quotient5 * price5 + quotient3 * price3 + quotient1 * price1


def two_price_calc(count, offer_multiple, one_price, muliple_price):

    quotient = count // offer_multiple
    remainder = count % offer_multiple

    return remainder * one_price + quotient * muliple_price


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


def calc_xA_get_yB_free(count_B, count_A, priceB):

    # minus off Bs until its zero
    free_Bs = get_free_Bs(count_A)
    count_B = special_minus(count_B, free_Bs)
    return count_B * priceB


def checkout(skus):
    if not isinput_sanitised(skus):
        return -1

    # Check these counts
    B_counts = skus.count('B')
    E_counts = skus.count('E')

    N_counts = skus.count('N')
    M_counts = skus.count('M')

    R_counts = skus.count('R')
    Q_counts = skus.count('Q')

    B_counts = special_minus(B_counts, get_free_Bs(E_counts))
    M_counts = special_minus(M_counts, get_free_Bs(N_counts))
    Q_counts = special_minus(Q_counts, get_free_Bs(R_counts))


    total = 0
    total += three_price_calc(skus.count('A'), 50, 130, 200, 1, 3, 5)
    total += two_price_calc(B_counts, 2, 30, 45)
    total += single_price_calc(skus.count('C'), 20)
    total += single_price_calc(skus.count('D'), 15)
    total += single_price_calc(E_counts, 40)
    total += buy_n_get_k_free_calc(skus.count('F'), 10, 2, 1)


    total += single_price_calc(skus.count('G'), 20)
    total += three_price_calc(skus.count('H'), 10, 45, 80, 1, 5, 10)
    total += single_price_calc(skus.count('I'), 35)
    total += single_price_calc(skus.count('J'), 60)
    total += two_price_calc(skus.count('K'), 2, 80, 150)

    total += single_price_calc(skus.count('L'), 90)
    total += single_price_calc(M_counts, 15)
    total += single_price_calc(N_counts, 40)

    total += single_price_calc(skus.count('O'), 10)

    total += two_price_calc(skus.count('P'), 5, 50, 200)
    total += two_price_calc(Q_counts, 3, 30, 80)
    total += single_price_calc(R_counts, 50)

    total += single_price_calc(skus.count('S'), 30)
    total += single_price_calc(skus.count('T'), 20)


    total += buy_n_get_k_free_calc(skus.count('U'), 40, 3, 1)

    total += three_price_calc(skus.count('V'), 50, 90, 130, 1, 3, 5)

    return total





