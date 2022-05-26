def variance(val):
    numb = len(val)
    # m will have the mean value
    m = sum(val) / numb
    # Square deviations
    devi = [(x - m) ** 2 for x in val]
    # Variance
    variance = sum(devi) / numb
    return variance