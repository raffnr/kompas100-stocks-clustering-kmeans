def get_expected_return3 (price_list):
    total = 0

    for i in range(1, len(price_list)):
        total += (price_list[i] - price_list[i-1]) / price_list[i-1]
    
    return total / (len(price_list) - 1)

