#include <bits/stdc++.h>
#define REP(i, n) for (int i = 0; i < n; i++)
#define REPR(i, n) for(int i = n; i >= 0; i--)
#define FOR(i, m, n) for(int i = m; i < n; i++)
#define endl    '\n'
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
    int N,A,B;
    int qualified = 0;
    int foreign_index = 0;
    vector<string> ans;
    string S;
    cin>>N>>A>>B;
    cin>>S;
    REP(i,N){
        if(S[i] == 'a'){
            if(qualified<(A+B)){
                ans.push_back("Yes");
                qualified+=1;
            }
            else{
                ans.push_back("No");
            }
        }
        else if(S[i] == 'b'){
            foreign_index+=1;
            if((qualified<(A+B))&&(foreign_index<=B)){
                ans.push_back("Yes");
                qualified+=1;
            }
            else{
                ans.push_back("No");
            }
        }
        else{
            ans.push_back("No");
        }
        
    }
    for(auto v: ans){
        cout << v << endl;
    }
}