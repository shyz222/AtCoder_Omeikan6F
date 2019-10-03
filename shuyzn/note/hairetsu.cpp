#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

//配列がどんなものか備忘録
int main() {
  int a[3] = {0, 1, 2};  // int型が入る箱を3つ作る※0~3の4つの箱作るわけではない
  // int a[3] = {0};         //これはa[0]=1,a[1]=0,a[2]=0になる
  // int a[3] = {1};         //これはa[0]=1,a[1]=0,a[2]=0になる
  // int a[3] = {1, 2};      //これはa[0]=1,a[1]=2,a[2]=0になる
  cout << a[-1] << endl;  // 毎回違うよくわからん数値出る
  cout << a[0] << endl;   // 0 ※箱は0起点
  cout << a[1] << endl;   // 1
  cout << a[2] << endl;   // 2
  cout << a[3] << endl;   // 毎回違うよくわからん数値出る

  string b[3] = {"さ", "ん", "ま"};  // string型は？
  cout << b[-1] << endl;
  cout << b[0] << endl;
  cout << b[1] << endl;
  cout << b[2] << endl;
  cout << b[3] << endl;
  // コンパイルできるが、
  // a[i]のcoutがあると、Segmentation fault (core dumped)ってでる
  // a[i]のcoutがないと、何も表示されない
}