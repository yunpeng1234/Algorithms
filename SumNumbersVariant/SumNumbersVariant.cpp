#include <iostream>
#include <array>
#include <vector>
#include <deque>

using namespace std;

// assumes that numbers in number list are integers above 0.
// iterates through number list, finding most efficient paths to all values up to target.
// assumes the resulting vector need not be sorted.
vector<int> find_lowest_index_sum(vector<int> inputs, int target){
    int maxIndex = inputs.size();
    // storage stores vectors of indices, with index 0 containing the sum of the indices for comparison purposes.
    vector<vector<int>> storage(target + 1, {-1});
    storage[0][0] = 0;
    int jump, value;
    
    for (int inputIndex = 0; inputIndex  < maxIndex; inputIndex++){
        value = inputs[inputIndex];
        // iterates through storage from end to start, checking if value can be used to reduce index sum at any position.
        for (int index = target; index >= 0; index--){
            jump = index + value;
            // checks if jump does not overshoot or if current index is accessible before proceeding
            if (jump <= target && storage[index][0] != -1){
                // updates smallest set of indices to jumped position if necessary
                if (storage[jump][0] > storage[index][0] + inputIndex || storage[jump][0] == -1){
                    storage[jump] = storage[index];
                    storage[jump].push_back(inputIndex);
                    storage[jump][0] += inputIndex;
                }
            }
        }
    }

    storage[target][0] = storage[target].back();
    storage[target].pop_back();
    //returns empty vector if impossible
    return storage[target];
}

int main(){
    int cases, input, target;
    vector<int> inputs;
    cin >> cases;
    while(cases--){
        cin >> input;
        inputs.push_back(input);
    }
    cin >> target;
    auto res = find_lowest_index_sum(inputs, target);
    for(int indices : res){
        cout << indices << " ";
    }
    return 0;
}
