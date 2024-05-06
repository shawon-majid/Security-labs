# Lab - 2

## Task 1

The given cipher is: “odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo”

The following bruteforce code is used to break the cipher

```cpp
#include <iostream>
#include <string>
using namespace std;

int main(){
    string encryptedText;
    cin >> encryptedText;

    for(int key = 0; key < 26; key++){
        string decryptedText = encryptedText;

        for(int i = 0; i < decryptedText.size(); i++){
            int cur = decryptedText[i]-'a';
            cur = (cur + key) % 26;
            decryptedText[i] = cur + 'a';
        }

        cout <<"key: " <<key<< ", decrypted text: " << decryptedText << "\n";
    }

    return 0;
}
```

The output of the code is:

```
key: 0, decrypted text: odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo
key: 1, decrypted text: pespcpfxtdespmpdedxlcenzyeclneawleqzcxzfeespcp
...
key: 16, decrypted text: ethereumisthebestsmartcontractplatformoutthere
...
key: 25, decrypted text: ncqnandvrbcqnknbcbvjaclxwcajlcyujcoxavxdccqnan
```

From the given output of all possible 26 shifts, we can see that key 16 is the most probable solution. For which the deciphered text is:
"Ethereumisthebestsmartcontractplatformoutthere", which means

`Ethereum is the best smart contract platform out there.`

## Task 2

For task 2, the first given ciphertext is:

```
af p xpkcaqvnpk pfg, af ipqe qpri, gauuikifc tpw, ceiri udvk tiki afgarxifrphni cd ea...
```

There is also a frequency distribution given.

To break the code, I’ve used the frequency distribution to substitute the letters in the ciphertext in the order of frequency. But unfortunately, the code couldn’t be broken.

The algorithm I used is the following:

```
1. Sort the frequency distribution in descending order.
2. Find the frequency distribution of the letters in the ciphertext and sort them in descending order.
3. Then map the letters in the order of frequency distribution to decrypt the text.
```

The code used:

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
using namespace std;

int main(){
    vector<pair<double, int>> freq {{8.05, 0}, {1.67, 1}, {2.23, 2}, {5.10, 3}, {12.22, 4}, {2.14, 5}, {2.30, 6}, {6.62, 7}, {6.28, 8}, {0.19, 9}, {0.95, 10}, {4.08, 11}, {2.33, 12}, {6.95, 13}, {7.63, 14}, {1.66, 15}, {0.06, 16}, {5.29, 17}, {6.02, 18}, {9.67, 19}, {2.92, 20}, {0.82, 21}, {2.60, 22}, {0.11, 23}, {2.04, 24}, {0.06, 25}};
    sort(freq.rbegin(), freq.rend());
    string encryptedText;
    string chunk;
    while(cin >> chunk){
        encryptedText += chunk + " ";
    }
    vector<pair<double, int>> curFreq;
    map<int, int> cf;
    int total = 0;
    for(int i = 0; i < encryptedText.size(); i++){
        if(encryptedText[i] >= 'a' && encryptedText[i] <= 'z'){
            total++;
            cf[encryptedText[i]-'a']++;
        }
    }
    for(auto x: cf){
        double frac = (x.second / (double)total)* 100;
        curFreq.push_back({frac, x.first });
    }
    sort(curFreq.rbegin(), curFreq.rend());
    string decryptedText = encryptedText;

    string list="abcdefghijklmnopqrstuvwxyz";
    string key=list;
    for(int i = 0; i < list.size(); i++){
        int cur = list[i] - 'a';
        for(int j = 0; j < curFreq.size(); j++){
            auto x = curFreq[j];
            if(x.second == cur){
                key[i] = (char)(freq[j].second + 'a');
                break;
            }
        }
    }
    cout << "key: "<< key << "\n";
    for(int i = 0; i < encryptedText.size(); i++){
        int cur = encryptedText[i] - 'a';
        for(int j = 0; j < curFreq.size(); j++){
            auto x = curFreq[j];
            if(x.second == cur){
                decryptedText[i] = (char)(freq[j].second + 'a');
                break;
            }
        }
    }
    cout << "decryptedText: "<<decryptedText << "\n";
    return 0;
}
```

The output was:

```js
key: yjrfdfpiilaohctbuvwgenmxks
decryptedText: yrdyi gts benp nrfo thl benp kefudrtn, thl otl yeeh aoe gihlen iw aoe sorne win srjap petns, eben srhfe ors nemtnvtyde lrstkketnthfe thl uhejkefael neaunh. aoe nrfoes oe otl yniucoa ytfv wnim ors antbeds otl hig yefime t diftd decehl, thl ra gts kikudtndp yedrebel, gotaeben aoe idl widv mrcoa stp, aota aoe ordd ta y

tc ehl gts wudd iw auhheds sauwwel grao anetsune. thl rw aota gts hia ehiuco win wtme, aoene gts tdsi ors knidihcel brciun ai mtnbed ta. arme gine ih, yua ra seemel ai otbe draade ewwefa ih mn. ytccrhs. ta hrheap oe gts mufo aoe stme ts ta wrwap. ta hrheap-hrhe aoep yecth ai ftdd orm gedd-knesenbel; yua uhfothcel giudl otbe yeeh hetnen aoe mtnv. aoene gene sime aota soiiv aoern oetls thl aoiucoa aors gts aii mufo iw t ciil aorhc; ra seemel uhwtrn aota
```

Similarly, for the second ciphertext:

```
aceah toz puvg vcdl omj puvg yudqecov, omj loj auum klu thmjuv hs klu zlcvu shv zcbkg guovz, upuv zcmdu lcz vuwovroaeu...
```

The output was:

```js
key: ujnylfpoidthscakwvgfermxbi
decryptedText: unluo fai kerp rnyh asd kerp beywlnar, asd had uees the fosder og the ihnre gor injtp peari, eker insye hni remarvaule dniabbearasye asd wsejbeyted retwrs. the rnyhei he had urowcht uayv grom hni trakeli had sof ueyome a loyal lecesd, asd nt fai bobwlarlp uelneked, fhateker the old golv mncht iap, that the hnll at uac esd fai gwll og twsseli itwgged fnth treaiwre. asd ng that fai sot esowch gor game, there fai alio hni brolosced kncowr to markel at. tnme fore os, uwt nt ieemed to hake lnttle eggeyt os mr. uaccnsi. at snsetp he fai mwyh the iame ai at gngtp. at snsetp-snse thep uecas to yall hnm fell-breierked; uwt wsyhasced fowld hake uees searer the marv. there fere iome that ihoov thenr headi asd thowcht thni fai too mwyh og a cood thnsc; nt ieemed wsganr that aspose ihowld boiieii (abbarestlp) berbetwal powth

 ai fell ai (rebwtedlp) nsejhawitnule fealth. nt fnll hake to ue band gor, thep iand. nt nist satwral, asd trowule fnll yome og nt! uwt io gar trowule had sot yome; asd ai mr. uaccnsi fai ceserowi fnth hni mosep, moit beoble fere fnllnsc to gorcnke hnm hni oddntnei asd hni cood gortwse. he remansed os knintnsc termi fnth hni relatnkei (ejyebt, og yowrie, the iayvknlleuaccnsiei), asd he had masp dekoted admnreri amosc the houunti og boor asd wsnmbortast gamnlnei. uwt he had so yloie grnesdi, wstnl iome og hni powscer yowinsi uecas to crof wb. the eldeit og theie, asd unluoi gakowrnte, fai powsc grodo uaccnsi. fhes unluo fai snsetp-snse he adobted grodo ai hni henr, asd urowcht hnm to lnke at uac esd; asd the hobei og the iayvknlle- uaccnsiei fere gnsallp daihed. unluo asd grodo habbesed to hake the iame unrthdap, iebtemuer 22sd. pow had uetter yome asd lnke here, grodo mp lad, iand unluo ose dap; asd thes fe yas yeleurate owr unrthdap-bartnei yomgortaulp tocether. at that tnme grodo fai itnll ns hni tfeesi, ai the houunti yalled the nrreibosinule tfestnei uetfees yhnldhood asd yomnsc og ace at thnrtp-three
```

## Analysis:

From the second ciphertext, we can see that some of the words are understandable, like `“he”`, `“had”`, `“the”`, etc. And some of the words are close to our understandable word, like the last word, `“thnrtp-three”`, which may refer to `“thirty-three”`. I think that the frequency distribution is not proper to break the ciphertext, and a more sophisticated approach is needed with many iterations to break the code.
