#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define MAX 100
const int MOD = 1e9 + 7;
/*

*/

int gdc(int a, int b) {
    if(b==0) return a;

    while(b!=0) {
        cout<< "q= " << int(a/b) << "   ";
        cout << "a= " << a << "    ";
        cout << "b= " << b << "    ";
        int temp=a%b;
        cout <<  "r= " << temp << endl;
        a=b;
        b=temp;
    }
    return a;
}

int main() {
ios_base::sync_with_stdio(false);
cin.tie(NULL);
cout.tie(NULL);

cout << gdc(13510740, 50760);
return 0;
}