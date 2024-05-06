#include <iostream>
#include <string>
using namespace std;

int main()
{
    string encryptedText;
    cin >> encryptedText;

    for (int key = 0; key < 26; key++)
    {
        string decryptedText = encryptedText;

        for (int i = 0; i < decryptedText.size(); i++)
        {
            int cur = decryptedText[i] - 'a';
            cur = (cur + key) % 26;
            decryptedText[i] = cur + 'a';
        }

        cout << "key: " << key << ", decrypted text: " << decryptedText << "\n";
    }

    return 0;
}