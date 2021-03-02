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

void nestPrinter(vector<vector<unsigned long long> > nested) {
    for (auto& it : nested) {
      cout << it[0] << " " << it[1] << " " << it[2];
    }
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

int calculateTime(int pos, int speed, int hear, unsigned long long c) {
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

vector<unsigned long long> findMin(vector<vector <unsigned long long> > dataTab, unsigned long long lg, unsigned long long sm, unsigned long long interval) {
  vector<vector<unsigned long long> > iterData;
    for (unsigned long long g = sm; g <= lg; g = g + interval) {
      unsigned long long totalVal = 0;
      for (auto& f : dataTab){
        totalVal = totalVal + calculateTime(f[0], f[1], f[2], g);
      }
      vector<unsigned long long> singleCalc;
      if (g != 0 && totalVal != 0) {
        singleCalc.push_back(g);
        singleCalc.push_back(totalVal);
        iterData.push_back(singleCalc);
      }
    }
    vector<vector<unsigned long long> > iterDataCopy = iterData;
    sort(iterData.begin(), iterData.end(), sortcol);
    vector<unsigned long long> vecReturn;
    if (interval == 1) {
      vecReturn.push_back(iterData[0][1]);
    } else {
      unsigned long long rC;
      unsigned long long lC;
      int theInd = getIndex(iterDataCopy, iterData[0]);
      if (theInd+1 == iterDataCopy.size()) {
        lC = iterDataCopy[theInd-1][0];
        rC = iterDataCopy[theInd][0];
        vecReturn.push_back(rC);
        vecReturn.push_back(lC);
      } else if (theInd+1 == 1) {
        lC = iterDataCopy[theInd][0];
        rC = iterDataCopy[theInd+1][0];
        vecReturn.push_back(rC);
        vecReturn.push_back(lC);
      } else {
        lC = iterDataCopy[theInd-1][0];
        rC = iterDataCopy[theInd+1][0];
        vecReturn.push_back(rC);
        vecReturn.push_back(lC);
      }
    }
    return vecReturn;
}

void recurseMin(vector<vector <unsigned long long> > allDataTab, unsigned long long lg, unsigned long long sm) {
  unsigned long long diff = lg - sm;
  if (diff == 0) {
    cout << 0 << endl;
  } else if (0 < diff && diff <= 30) {
    vector<unsigned long long> rA1 = findMin(allDataTab, lg, sm, 1);
    cout << rA1[0] << endl;
  } else if (30 < diff && diff <= 200) {
    vector<unsigned long long> rA2 = findMin(allDataTab, lg, sm, 10);
    recurseMin(allDataTab, rA2[0], rA2[1]);
  } else if (200 < diff && diff <= 500) {
    vector<unsigned long long> rA3 = findMin(allDataTab, lg, sm, 50);
    recurseMin(allDataTab, rA3[0], rA3[1]);
  } else if (500 < diff && diff <= 4000) {
    vector<unsigned long long> rA4 = findMin(allDataTab, lg, sm, 100);
    recurseMin(allDataTab, rA4[0], rA4[1]);
  } else if (1500 < diff && diff <= 10000) {
    vector<unsigned long long> rA5 = findMin(allDataTab, lg, sm, 500);
    recurseMin(allDataTab, rA5[0], rA5[1]);
  } else if (10000 < diff && diff <= 50000) {
    vector<unsigned long long> rA6 = findMin(allDataTab, lg, sm, 1000);
    recurseMin(allDataTab, rA6[0], rA6[1]);
  } else if (50000 < diff && diff <= 1000000) {
    vector<unsigned long long> rA7 = findMin(allDataTab, lg, sm, 25000);
    recurseMin(allDataTab, rA7[0], rA7[1]);
  } else if (1000000 < diff && diff <= 10000000) {
    vector<unsigned long long> rA8 = findMin(allDataTab, lg, sm, 250000);
    recurseMin(allDataTab, rA8[0], rA8[1]);
  } else if (10000000 < diff && diff <= 50000000) {
    vector<unsigned long long> rA9 = findMin(allDataTab, lg, sm, 1000000);
    recurseMin(allDataTab, rA9[0], rA9[1]);
  } else if (50000000 < diff && diff <= 1000000000) {
    vector<unsigned long long> rAz = findMin(allDataTab, lg, sm, 23750000);
    recurseMin(allDataTab, rAz[0], rAz[1]);
  }
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
    recurseMin(totalData, largestPos, smallestPos);
}