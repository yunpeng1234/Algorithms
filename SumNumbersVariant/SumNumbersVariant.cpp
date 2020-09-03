#include <iostream>
#include <array>
#include <vector>

using namespace std;

// assumes that numbers in number list are integers above 0.
// iterates through number list, finding most efficient paths to all values up to target.
int find_lowest_index_sum(vector<int> inputs, int target){
    int maxIndex = inputs.size();
    vector<int> storage(target + 1, -1);
    storage[0] = 0;
    int jump, value;

    for (int inputIndex = 0; inputIndex  < maxIndex; inputIndex++){
        value = inputs[inputIndex];
        //iterates through storage from end to start, checking if value can be used to reduce index sum at any position.
        for (int index = target; index >= 0; index--){
            jump = index + value;
            //breaks if jump overshoots target or current index is inaccessible
            if (jump <= target && storage[index] != -1){
                //updates lowest index sum to given index
                if (storage[jump] > storage[index] + inputIndex || storage[jump] == -1){
                    storage[jump] = storage[index] + inputIndex;
                }
            }
        }
    }
    
    //returns -1 if unable to obtain target
    return storage[target];
}

//input format:
//length of number list, n
//n numbers
//target sum to add up to
int main(){
    int cases, input, target;
    vector<int> inputs;
    cin >> cases;
    while(cases--){
        cin >> input;
        inputs.push_back(input);
    }
    cin >> target;
    cout << find_lowest_index_sum(inputs, target) << endl;
    return 0;
}
