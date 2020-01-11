#include <bits/stdc++.h>
#define rep(i, n) repe(i, 0, n)
#define repe(i, a, b) for (int i = int(a); i < int(b); ++i)
using namespace std;
using ll = long long;

int main() {
  int h, w, a, b;
  cin >> h >> w >> a >> b;
  rep(i, h) {
    rep(j, w) { cout << ((j < a) ^ (i < b) ? 0 : 1); }
    cout << endl;
  }
}

// #include<iostream>
// using namespace std;
// int H,W,A,B;
// main()
// {
// 	cin>>H>>W>>A>>B;
// 	for(int i=0;i<H;i++)
// 	{
// 		for(int j=0;j<W;j++)
// 		{
// 			cout<<((i<B)^(j<A)?0:1);
// 		}
// 		cout<<endl;
// 	}
// }
