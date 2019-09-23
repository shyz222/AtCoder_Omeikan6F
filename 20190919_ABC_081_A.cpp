#include <bits/stdc++.h>
using namespace std;

// int main() {
//     int a[3],n=0;
//     cin>>a[3];
//     for(int i=1; i>3; i++){
//         if(a[n]==1){
//             n++;
//         }
//     }
//     cout<<n;
// }


int main() {
   string s;
   int i=0;
   cin>>s;
   if(s[0] == '1'){
       ++i;
   }
   if(s[1] == '1'){
       ++i;
   }
   if(s[2] == '1'){
       ++i;
   }
   cout<<i<<endl;
}
