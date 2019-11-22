#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> v = {1, 2, 3, 4, 5};
  auto it = lower_bound(v.begin(), v.end(), 3);

  int index = it - v.begin();

  // output
  //   index: 2
  //   value: 3
  cout << "index: " << index << endl;
  cout << "value: " << v[index] << endl;
  return 0;
}