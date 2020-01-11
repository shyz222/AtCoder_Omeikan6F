#include <bits/stdc++.h>
#define rep(i, n) repe(i, 0, n)
#define repe(i, a, b) for (int i = int(a); i < int(b); ++i)
using namespace std;
using ll = long long;

int main() {
  int n;
  cin >> n;
  vector<int> x(n), y(n);
  rep(i, n) cin >> x[i] >> y[i];
  // 距離関数
  auto dist = [&](int i, int j) {
    double dx = x[i] - x[j];
    double dy = y[i] - y[j];
    return sqrt(dx * dx + dy * dy);
  };
  vector<int> p(n);
  rep(i, n) p[i] = i;
  double len = 0;
  int cnt = 0;
  do {
    rep(i, n - 1) { len += dist(p[i], p[i + 1]); }
    cnt++;  //経路パターン（n!なんどけどね...）
  } while (next_permutation(p.begin(), p.end()));
  // next_permutationは配列を与えると次の順列を返してくれる
  // 次の順列がないとfalseを返す
  double ans = len / cnt;
  printf("%.10f\n", ans);
  return 0;
}