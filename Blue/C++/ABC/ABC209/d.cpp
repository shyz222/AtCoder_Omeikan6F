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
using Graph = vector<vector<int>>;
//配列の要素数は　sizeof(ar)/sizeof(ar[0]) で求める


signed main(){
    cin.tie(0);
    cout.tie(0);
    ios::sync_with_stdio(false);
    int N,Q;
    cin>>N>>Q;
    Graph G(N);
    vector<vector<int>> c_d(Q, vector<int>(2));
    for (int i = 0; i < N-1; i++) {
        int a, b;
        cin >> a >> b;
        G[a-1].push_back(b-1);
        G[b-1].push_back(a-1);
    }
    //BFS
    vector<int> dist(N, -1),number_of_pass(N);
    queue<int> que;
    dist[0] = 0;
    que.push(0);
    while (!que.empty()) {
        int v = que.front(); 
        que.pop();
        for (int nv : G[v]) {
            if (dist[nv] != -1) continue; 
            dist[nv] = dist[v] + 1;
            que.push(nv);
        }
    }
    REP(i,0,Q){
        int C,D;
        cin >> C >> D;
        if(dist[C-1]%2 == dist[D-1]%2) cout << "Town" << endl;
        if(dist[C-1]%2 != dist[D-1]%2) cout << "Road" << endl;
    }    
}