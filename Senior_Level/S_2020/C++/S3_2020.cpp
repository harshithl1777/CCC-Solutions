#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

vector<string> findComb(string needle, string hay) {
    vector<string> combs;
    int len = needle.length();
    for (int x = 0; x <= hay.length()-len; x++) {
        string strHold = hay.substr(x, len);
        combs.push_back(strHold);
    }
    return combs;
}

int main() {
    string needle;
    string hay;
    getline(cin, needle);
    getline(cin, hay);
    if (needle.length() > hay.length()) {
        cout << 0 << endl;
    } else {
        vector<string> finCombs = findComb(needle, hay);
    int passed = 0;
    vector<string> doneCombs;
    for (int x = 0; x <= finCombs.size()-1; x++) {
      bool prevDone = false;
      if (x != 0) {
        for (int f = 0; f <= doneCombs.size()-1; f++) {
            if (finCombs[x] == doneCombs[f]) {
            prevDone = true;
            }
        }
      }
      if (prevDone) {
        continue;
      }
        vector<char> charArray;
        for (int y = 0; y <= needle.length()-1; y++) {
            charArray.push_back(needle[y]);
        }
        string combination = finCombs[x];
        bool noProblemsComb = false;
        for (int z = 0; z <= combination.length()-1; z++) {
            char combChar = combination[z];
            auto valToErase = find(charArray.begin(), charArray.end(), combChar);
            if (valToErase != charArray.end()) {
                int indexToErase = valToErase - charArray.begin();
                charArray.erase(charArray.begin() + indexToErase);
                noProblemsComb = true;
            } else {
                noProblemsComb = false;
                break;
            }
        }
        if (noProblemsComb) {
          passed = passed + 1;
        }
        doneCombs.push_back(finCombs[x]);
    }
    cout << passed << endl;
    }
}