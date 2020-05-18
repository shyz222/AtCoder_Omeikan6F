#include <bits/stdc++.h>
#define INF 2e9
#define int ll
#define vi          vector<int>
#define de          deque<int>
#define SZ(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()//全範囲指定を簡略化
typedef long long ll;
using namespace std;
//配列の要素数は　sizeof(ar)/sizeof(ar[0]) で求める
signed main(){
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);
    int H, N;
    cin >> H >> N;
    vi v(N);
    int sum = 0;

    for(int i=0;i<N;i++){
        cin >> v[i];
        sum += v[i];
    }

    if(sum >= H){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
}