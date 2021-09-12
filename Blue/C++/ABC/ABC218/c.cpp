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

vector<string> rotate90(vector<string> a){
    const int h = a.size();
    const int w = a.front().size();

    vector<string> b(h, string(w, ' '));
    REP(i,0,h){
        REP(j,0,w){
            b[j][h-i-1] = a[i][j];
        }
    }
    return b;
}

//配列の要素数は　sizeof(ar)/sizeof(ar[0]) で求める
signed main(){
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);

    int N;
    cin>>N;
    int S_count=0,T_count=0;
    vector<string> S(N), T(N);
    REP(i,0,N)cin >> S[i];
    REP(i,0,N) cin >> T[i];
    REP(i,0,N){
        REP(j,0,N){
            if(S[i][j]=='#') S_count+=1;
            if(T[i][j]=='#') T_count+=1;
        }
    }
    if (S_count != T_count) {
        cout << "No" << endl;
        return 0;
    }

    REP(i,0,4){
        pair<int, int> S_topleft{-1, -1}, T_topleft{-1,-1};
        REP(i,0,N){
            REP(j,0,N){
                if(S_topleft.first < 0 && S[i][j]=='#'){
                    S_topleft = {i, j};
                }
                if(T_topleft.first < 0 && T[i][j]=='#'){
                    T_topleft = {i, j};
                }
                if (S_topleft.first >= 0 && T_topleft.first >= 0) break;
            }
            if (S_topleft.first >= 0 && T_topleft.first >= 0) break;
        }

        bool ans = true;

        REP(i,0,N){
            REP(j,0,N){
                const int offset_i = T_topleft.first - S_topleft.first;
                const int offset_j = T_topleft.second - S_topleft.second;

                const int offset_ii = i+offset_i;
                const int offset_jj = j+offset_j;
                
                if ((0<=offset_ii&&offset_ii<=N-1)&&(0<=offset_jj&&offset_jj<=N-1)){
                    ans = S[i][j] == T[offset_ii][offset_jj];
                }
                else{
                    ans = S[i][j] == '.';
                }
                if (!ans) break;
            }
            if (!ans) break;
        }
        if (ans) {
            cout << "Yes" << endl;
            return 0;
        }
        S = rotate90(S);
    }
    cout << "No" << endl;
}