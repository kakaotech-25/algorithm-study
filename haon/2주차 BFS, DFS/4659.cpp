#include <iostream>
#include <string.h>
 
using namespace std;
 
int main()
{
    string N;
    char vowel[5] = {'a','e','i','o','u'};
    
    
    while(true){
        cin >> N;
        int a = 0;
        int v = 0;
        int c = 0;
        if(N=="end"){
            break;
        }
        for(int i=0; i<N.length(); i++){
            for(int j=0; j<5; j++){   // 1번조건
                if(N[i]==vowel[j]){
                    a = 1; break;
                }
            }
        }
        if(!a){ cout << "<" << N << ">" << " is not acceptable." << endl; }
        else{
            for(int i=0; i<N.length(); i++){
                int b = 1;
                if(N[i]==N[i+1] && N[i]!='o' && N[i]!='e'){  // 3번조건
                    a = 0; break;
                }
                for(int j=0; j<5; j++){  //2번조건
                    if(N[i]==vowel[j])
                        b = 0;  // v이면 0, c이면 1
                }
                if(b==0){ v++; c=0; }
                else{ c++; v=0; }
                if(c==3 || v==3){
                    a = 0; break;
                }
            }
            if(!a){ cout << "<" << N << ">" << " is not acceptable." << endl; }
            else{ cout << "<" << N << ">" << " is acceptable." << endl; }
        }
    }
    return 0;
}