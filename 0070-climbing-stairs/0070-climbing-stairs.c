int climbStairs(int n){
    int i = 0;
    int one = 1;
    int two = 0;
    while (i<=n){
        two += one;
        one = two - one;
        i++;
        //printf("%d: %d\n", i, two);
    }
    return two;
}
