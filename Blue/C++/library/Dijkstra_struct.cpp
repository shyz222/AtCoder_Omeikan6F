#include <bits/stdc++.h>
#define int ll
#define REP(i, a, n) for (int i = a; i < n; i++)
struct edge{int to, cost;};
typedef long long ll;
typedef pair<int,int> P;

struct graph{
    int V;
    vector<vector<edge> > G;
    vector<int> d;

    graph(int n){
        init(n);
    }

    void init(int n){
        V = n;
        G.resize(V);
        d.resize(V);
        REP(i,0,V){
            d[i] = INF;
        }
    }

    void add_edge(int s, int t, int cost){
        edge e;
        e.to = t, e.cost = cost;
        G[s].push_back(e);
    }

    void dijkstra(int s){
        REP(i,0,V){
            d[i] = INF;
        }
        d[s] = 0;
        priority_queue<P,vector<P>, greater<P> > que;
        que.push(P(0,s));
        while(!que.empty()){
            P p = que.top(); que.pop();
            int v = p.second;
            if(d[v]<p.first) continue;
            for(auto e : G[v]){
                if(d[e.to]>d[v]+e.cost){
                d[e.to] = d[v]+e.cost;
                que.push(P(d[e.to],e.to));
                }
            }
        }
    }
};