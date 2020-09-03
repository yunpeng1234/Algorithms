#include <iostream>
#include <array>
#include <vector>

using namespace std;
//assumes over small range, numbers above 0.
int find_lowest_index_sum(vector<int> inputs, int target){
    int maxIndex = inputs.size();
    vector<int> storage(target + 1, -1);
    storage[0] = 0;
    int jump;
    int value;

    for (int inputIndex = 0; inputIndex  < maxIndex; inputIndex++){
        value = inputs[inputIndex];
        //iterates through storage from end to start, checking if value can be used to reduce index sum at any position.
        for (int index = target; index >= 0; index--){
            jump = index + value;
            //breaks if jump overshoots target or current index is inaccessible
            if (jump <= target && storage[index] != -1){
                //updates lowest index sum to given index
                if (storage[jump] > storage[index] + inputIndex || storage[jump] == -1){
                    //cout << storage[jump] << " -> " << storage[index] + inputIndex << endl;
                    storage[jump] = storage[index] + inputIndex;
                }
            }
        }
    }
    return storage[target];
}

int main(){
    vector<int> a = {3,5,6,7};
    int target = 7;
    cout << find_lowest_index_sum(a, target) << endl;
    return 0;
}