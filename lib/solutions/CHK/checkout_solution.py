

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    A_one_price = 50
    B_one_price = 30
    C_one_price = 20
    D_one_price = 15

    A_counts = skus.count('A')
    B_counts = skus.count('B')
    C_counts = skus.count('C')
    D_counts = skus.count('D')

    return A_counts * A_one_price + B_one_price * B_counts + C_one_price * 

