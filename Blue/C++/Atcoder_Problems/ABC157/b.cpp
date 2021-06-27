#include <bits/stdc++.h>
#define REP(i, a, n) for (int i = a; i < n; i++)
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
    int N;
    vector<vector<int>> vec(3,vector<int>(3));
    vector<vector<int>> result(3, vector<int>(3, 0));
    REP(i,0,3){
        REP(j,0,3){
            cin >> vec[i][j];
        }
    }
    cin >> N;
    vi b(N);
    REP(i,0,N){
        cin >> b[i];
    }
    REP(i,0,3){
        REP(j,0,3){
            REP(k,0,N){
                if(vec[i][j]==b[k]){
                    result[i][j] = 1;
                }
            }
        }
    }
    bool ans = false;
    if((result[0][0]==1&&result[1][1]==1&&result[2][2]==1)or(result[2][0]==1&&result[1][1]==1&&result[0][2]==1)){
        ans = true;
    }

    REP(i,0,3){
        int count = 0;
        REP(j,0,3){
            if(result[i][j]==1){
                count++;
            }
            if(count==3){
                ans = true;
            }
        }
    }
    REP(i,0,3){
        int count = 0;
        REP(j,0,3){
            if(result[j][i]==1){
                count++;
            }
            if(count==3){
                ans = true;
            }
        }
    }
    if(ans){
        cout << "Yes" << endl;
    }
    else{cout << "No" << endl;}
}