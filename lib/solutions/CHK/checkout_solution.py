

# noinspection PyUnusedLocal
# skus = unicode string

def multi_price_calc(count, offer_multiple, one_price, muliple_price):

    quotient = count // offer_multiple
    remainder = count % offer_multiple

    return remainder * one_price + quotient * muliple_price


def single_price_calc(count, one_price):
    return count * one_price


def isinput_sanitised(skus):
    # Check if there are no values outside of ABCD
    # if so, return false
    allowed_values = "ABCD"
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

    return multi_price_calc(A_counts, 3, 50, 130) + multi_price_calc(B_counts, 2, 30, 45) + single_price_calc(C_counts, C_one_price) + single_price_calc(D_counts, D_one_price)

