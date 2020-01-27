///                ..:: In The Name Of God ::..
#include <bits/stdc++.h>
#define REP(i, n) for (int i = 0; i < n; i++)
#define REPR(i, n) for(int i = n; i >= 0; i--)
#define FOR(j, i, n) for(int j = i+1; j < n; j++)
#define endl    'n'
#define INF 2e9
#define int ll
#define vi          vector<int>
#define de          deque<int>
#define SZ(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()//全範囲指定を簡略化
typedef long long ll;
using namespace std;
//配列の要素数は　sizeof(ar)/sizeof(ar[0]) で求める

int arr[100];
signed main(){
cin.tie(0);
cout.tie(0);
ios::sync_with_stdio(false);
int n ;
cin >> n;

REP(i,n){
    cin >> arr[i];
}

int ans = 0;
for(int i=0;i<n;i++)
    for(int j = i+1;j<n;j++)
        ans += arr[i]*arr[j];

cout << ans << endl;
return 0;
}