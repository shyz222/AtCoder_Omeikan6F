def ArithmeticN(a, d, n) -> int:
    """等差数列の一般項

    Args:
        a (int): 初項
        d (int): 公差
        n (int): 求めたい一般項
    
    Returns:
        int: 等差数列のn項目
    """
    return a+(n-1)*d

def GeometricN(a, d, n) -> int:
    """等比数列の一般項

    Args:
        a (int): 初項
        r (int): 公比
        n (int): 求めたい一般項
    
    Returns:
        int: 等比数列のn項目
    """
    return a*r**(n-1)