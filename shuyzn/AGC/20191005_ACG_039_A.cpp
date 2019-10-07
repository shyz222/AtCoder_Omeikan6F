#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

//同じ文字がk個連続する場合、そのうちのk/2（切り捨て）文字を変更する必要あり
// 1.   Sがすべて同じ文字の場合、S*K/2
// 2-1. Sの先頭と末尾が異なる場合、
// 2-2. Sの先頭と末尾が同じ場合、

long long solve(string str) {
  long long cnt = 0, ret = 0;
  rep(i, str.size()) {
    cnt++;
    //　最後の文字または、連続する文字が異なる場合
    if (i == (int)str.size() - 1 || str[i] != str[i + 1]) {
      // cnt/2が変更する文字の回数になるので、retに加算していく
      ret += cnt / 2;  // 除算は切り捨て
      cnt = 0;
    }
  }
  return ret;
}

int main() {
  string S;
  cin >> S;
  long long K;  // 1
  cin >> K;

  bool sameCharFlag = true;    //全て同じ文字フラグ
  rep(i, (int)S.size() - 1) {  // 2
    if (S[i] != S[i + 1]) sameCharFlag = false;
  }

  if (sameCharFlag == true) {  //全て同じ文字だった場合
    long long len = 1LL * (long long)(S.size()) * K;
    cout << len / 2LL << endl;  // 3

  } else {  //そうでない場合
    string V1 = S;
    string V2 = S + S;
    long long R1 = solve(V1);
    long long R2 = solve(V2);
    cout << R1 + (R2 - R1) * (K - 1LL) << endl;
  }
  return 0;
}

// 1
// int,long,long longについて
//サイズは指定されておらず実装依存
//             int      long      long long
// 16bit CPU    16        32             64
// 32bit CPU    32        32             64
// 64bit CPU    64        64             64
// 目安         10^10     10^10          10^19

// 2
// S="abc"ならS.size()=3
// repは0起点なのでS.size()-1してる

// 3
// LLはlong long の整数リテラル
// 整数リテラルは、指定した型の上限値を超えた値が入る場合、その型を昇格させる