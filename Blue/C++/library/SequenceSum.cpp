#include <bits/stdc++.h>
int ArithmeticSum(int a, int d, int n){
    /*等差数列の和

    Args:
        a (int): 初項
        d (int): 公差
        n (int): 項数

    Returns:
        int: 等差数列の和
    */
    return ((n * (2 * a + (n - 1) * d)) / 2);
}

int GeometricSum(int a, int r, int n)
{
    /*等差数列の和

    Args:
        a (int): 初項
        r (int): 公比(r != 1)
        n (int): 項数

    Returns:
        int: 等比数列の和
    */
    return a * (1 - pow(r,2)) / (1 - r);
}