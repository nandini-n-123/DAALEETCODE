 long long minimumSteps(char* s) {
 int n = strlen(s);
 int* pos = (int*)malloc(n * sizeof(int));
 int count = 0;
 for (int i = 0; i < n; i++) {
 if (s[i] == '1') {
 pos[count++] = i;
 }
 }
 long long swap = 0;
 int target_pos = n- count;
 for (int i = 0; i < count; i++) {
 swap += (target_pos + i- pos[i]);
 }
 free(pos);
 return swap;
 }

