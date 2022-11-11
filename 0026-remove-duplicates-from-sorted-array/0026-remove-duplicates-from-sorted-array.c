#include <stdio.h>
int removeDuplicates(int* nums, int numsSize){
    int i; int j = 0;
    for(i = 1; i < numsSize; i++){
        if (nums[i-1] != nums[i]){
            nums[++j] = nums[i];
        }
    }
    for(i = 0; i < numsSize; i++){
        printf(" %d", nums[i]);
    }
    printf("\n");
    //nums[j] = nums[numsSize-1];
    for(i = 0; i < numsSize; i++){
        printf("%d ", nums[i]);
    }
    return ++j;
}