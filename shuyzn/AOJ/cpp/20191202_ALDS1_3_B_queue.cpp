#include <bits/stdc++.h>
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
using namespace std;
using ll = long long;
// n個のプロセスが1ループ目で全て処理途中だった場合最大100000個領域が必要
#define MAX 100005

struct P {
  string name;
  int time;
};

P p[MAX];
int head, tail;

// O(1)
void enqueue(P p1) {
  p[tail] = p1;
  tail = (tail + 1) % MAX;
  // tail == MAXだったら0にしてポインタリセット（リングバッファ！！）
  // それ以外はtail + 1
}

// O(1)
P dequeue() {
  P rtn = p[head];
  head = (head + 1) % MAX;
  // head == MAXだったら0にしてポインタリセット（リングバッファ！！）
  // それ以外はtail + 1
  return rtn;
}

// O(n)
int main() {
  int n, q;
  int cnt = 0;
  P buf;
  cin >> n >> q;
  rep(i, n) cin >> p[i].name >> p[i].time;
  head = 0;  // 要素が入っている先頭インデックス
  tail = n;  // 要素が入ってない先頭インデックス（次要素を入れるところ）
  // キューにあるプロセスが無くなるまで(つまり、head==tailになるまで)続ける
  while (head != tail) {
    buf = dequeue();
    // min(q,buf.time)はbufプロセスの処理時間
    cnt += min(q, buf.time);  // 累計処理時間に加算
    buf.time -= min(q, buf.time);  // bufプロセスの残りの処理時間を算出
    if (buf.time > 0) {
      enqueue(buf);  // bufプロセスが処理途中であればキューに追加
    } else {
      cout << buf.name << " " << cnt << endl;
    }
  }
  return 0;
}