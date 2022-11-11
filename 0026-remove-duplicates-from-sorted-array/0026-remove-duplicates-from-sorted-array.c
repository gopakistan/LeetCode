#include <stdio.h>
int removeDuplicates(int* nums, int numsSize){
    int i; int j = 0;
    for(i = 1; i < numsSize; i++){
        if (nums[i-1] != nums[i]){
            nums[++j] = nums[i];
        }
    }
    return ++j;
}