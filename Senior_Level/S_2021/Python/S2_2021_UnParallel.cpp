#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
    string theRowsie, colsPre, iterationNumberPre;
    int rows, col, itNumPost;
    getline(cin, theRowsie);
    getline(cin, colsPre);
    getline(cin, iterationNumberPre);
    stringstream changer2(colsPre);
    stringstream changer3(iterationNumberPre);
    stringstream changer(theRowsie);
    changer >> rows;
    changer2 >> col;
    changer3 >> itNumPost;
    vector<vector<char> > preMatrix;
    for (int bed = 1; bed <= rows; bed++) {
            vector<char> rowHolderThing;
            for (int ceed = 1; ceed <= col; ceed++) {
                rowHolderThing.push_back('B');
            }
            preMatrix.push_back(rowHolderThing);
    }
    for (int abe = 1; abe <= itNumPost; abe++){
        string stringCase;
        getline(cin, stringCase);
        char ringRow = stringCase[0];
        string toBeRC = stringCase.substr(2);
        stringstream streamingNumber(toBeRC);
        int numberTingEh;
        streamingNumber >> numberTingEh;
        if (ringRow == 'R'){
                vector<char> row = preMatrix[numberTingEh-1];
                for(int xolo = 0; xolo <= row.size()-1; xolo++) {
                    char theSinSquare = row[xolo];
                    if (theSinSquare == 'B') {
                        preMatrix[numberTingEh-1][xolo] = 'G';
                    } else if (theSinSquare == 'G') {
                        preMatrix[numberTingEh-1][xolo] = 'B';
                    }
                }
        } else if (ringRow == 'C'){
                for(int loPhone = 0; loPhone <= preMatrix.size()-1; loPhone++) {
                    vector<char> row2 = preMatrix[loPhone];
                    if (row2[numberTingEh-1] == 'B') {
                        preMatrix[loPhone][numberTingEh-1] = 'G';
                    } else if (row2[numberTingEh-1] == 'G') {
                        preMatrix[loPhone][numberTingEh-1] = 'B';
                    }
                }
        }
    }
    int gSq = 0;
    for (int pe = 0; pe <= preMatrix.size()-1; pe++) {
        vector<char> row = preMatrix[pe];
        for (int je = 0; je <= row.size()-1; je++) {
            char singleSquareThing = row[je];
            if (singleSquareThing == 'G') {
                gSq++;
            }
        }
    }
    cout << gSq << endl;
}