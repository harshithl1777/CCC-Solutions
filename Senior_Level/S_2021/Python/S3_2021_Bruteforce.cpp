#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int streamer(string startStr) {
    unsigned long long finNum;
    stringstream toNum(startStr);
    toNum >> finNum;
    return finNum;
}

vector<unsigned long long> split(string str) { 
    vector<unsigned long long> singleData;
    istringstream ss(str); 
    string word;
    while (ss >> word) { 
        singleData.push_back(streamer(word));
    };
    return singleData;
}

int calculateTime(int pos, int speed, int hear, int c) {
  unsigned long long toReturn;
    if (c > pos) {
        unsigned long long walkDPre = c - pos;
        if (hear >= walkDPre) {
            toReturn = 0;
        } else {
           unsigned long long walkD = (walkDPre - hear) * speed;
            toReturn = walkD;
        }
    } else if (c == pos) {
        toReturn = 0;
    } else if (c < pos) {
        unsigned long long walkDP = pos - c;
        if (hear >= walkDP) {
            toReturn = 0;
        } else {
            unsigned long long walkDD = (walkDP - hear) * speed;
            toReturn = walkDD;
        }
    }
    return toReturn;
}

bool sortcol( const vector<unsigned long long>& v1, 
               const vector<unsigned long long>& v2 ) { 
 return v1[1] < v2[1];
}

int getIndex(vector<vector<unsigned long long> > v, vector<unsigned long long> K)
{
    auto it = find(v.begin(), v.end(), K);
    int index = it - v.begin();
    return index;
}

void recurseMin(vector<vector <unsigned long long> > theVec, unsigned long long lg) {
  unsigned long long lgC;
  unsigned long long lgTot;
  for (int x = 0; x <= lg; x++) {
    int totalVal = 0;
    for (auto& y : theVec) {
      totalVal = totalVal + calculateTime(y[0], y[1], y[2], x);
    }
    if (x == 0) {
      lgC = x;
      lgTot = totalVal;
    } else {
      if (totalVal < lgTot) {
        lgTot = totalVal;
        lgC = x;
      }
    }
  }
  cout << lgTot << endl;
}

int main() {
    string startStr;
    getline(cin, startStr);
    unsigned long long iterNum = streamer(startStr);
    vector<vector<unsigned long long> > totalData;
    unsigned long long largestPos, smallestPos;
    for (int a = 0; a < iterNum; a++) {
        string inputHold;
        getline(cin, inputHold);
        vector<unsigned long long> toBeAppended = split(inputHold);
        if (a == 0) {
            largestPos = toBeAppended[0];
            smallestPos = toBeAppended[0];
        } else {
            if (toBeAppended[0] > largestPos) {
                largestPos = toBeAppended[0];
            } else if (toBeAppended[0] < smallestPos) {
                smallestPos = toBeAppended[0];
            }
        }
        totalData.push_back(toBeAppended);
    }
    recurseMin(totalData, largestPos);
}