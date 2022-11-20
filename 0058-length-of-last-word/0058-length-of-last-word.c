int lengthOfLastWord(char * s){
    int i = 0;
    int len = 0;
    int loopBool = 0;
    
    for(i = 0; (s[i] > 64 && s[i] < 123) || (s[i] == ' '); i++){
        printf("%c ", s[i]);
        if (s[i] != ' ') len++; 
        while (s[i] == ' '){
            //if (loopBool == 0) printf("%d\n", len);
            i++;
            loopBool = 1;
            //printf("\t\tinside loop\n");
        }
        if (s[i] > 64 && s[i] < 123 && loopBool == 1){
            len = 0;
            i -= 1;
            loopBool = 0;
            //printf("\t\tloop exit\n");
        }
        if (!((s[i] > 64 && s[i] < 123) || (s[i] == ' '))) break;
    }
    return(len);
}