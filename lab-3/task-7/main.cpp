// Bismillahir Rahman-ir Rahim
#include <bits/stdc++.h>
using namespace std;
int main()
{

    string h1, h2;
    cin >> h1 >> h2;
    int same = 0;
    for (int i = 0; i < h1.size(); i++)
    {
        if (h1[i] == h2[i])
        {
            same++;
        }
    }
    cout << "Number of same bit: " << same << "\n";
    return 0;
}