#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
using namespace std;

int main()
{
    vector<pair<double, int>> freq{{8.05, 0}, {1.67, 1}, {2.23, 2}, {5.10, 3}, {12.22, 4}, {2.14, 5}, {2.30, 6}, {6.62, 7}, {6.28, 8}, {0.19, 9}, {0.95, 10}, {4.08, 11}, {2.33, 12}, {6.95, 13}, {7.63, 14}, {1.66, 15}, {0.06, 16}, {5.29, 17}, {6.02, 18}, {9.67, 19}, {2.92, 20}, {0.82, 21}, {2.60, 22}, {0.11, 23}, {2.04, 24}, {0.06, 25}};
    sort(freq.rbegin(), freq.rend());
    string encryptedText;
    string chunk;
    while (cin >> chunk)
    {
        encryptedText += chunk + " ";
    }
    vector<pair<double, int>> curFreq;
    map<int, int> cf;
    int total = 0;
    for (int i = 0; i < encryptedText.size(); i++)
    {
        if (encryptedText[i] >= 'a' && encryptedText[i] <= 'z')
        {
            total++;
            cf[encryptedText[i] - 'a']++;
        }
    }
    for (auto x : cf)
    {
        double frac = (x.second / (double)total) * 100;
        curFreq.push_back({frac, x.first});
    }
    sort(curFreq.rbegin(), curFreq.rend());
    string decryptedText = encryptedText;

    string list = "abcdefghijklmnopqrstuvwxyz";
    string key = list;
    for (int i = 0; i < list.size(); i++)
    {
        int cur = list[i] - 'a';
        for (int j = 0; j < curFreq.size(); j++)
        {
            auto x = curFreq[j];
            if (x.second == cur)
            {
                key[i] = (char)(freq[j].second + 'a');
                break;
            }
        }
    }
    cout << "key: " << key << "\n";
    for (int i = 0; i < encryptedText.size(); i++)
    {
        int cur = encryptedText[i] - 'a';
        for (int j = 0; j < curFreq.size(); j++)
        {
            auto x = curFreq[j];
            if (x.second == cur)
            {
                decryptedText[i] = (char)(freq[j].second + 'a');
                break;
            }
        }
    }
    cout << "decryptedText: " << decryptedText << "\n";
    return 0;
}