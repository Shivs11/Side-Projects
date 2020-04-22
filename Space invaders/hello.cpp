#include<iostream>

using namespace std;

class Stack{
    private:
    int arr[100];
    int top;
    public:
    Stack(){
        top = -1;
    }
    void push(int n){
        if(top == (100-1)){
            return;
        }
        else if(top == -1){
            top = 0;
            arr[top] = n;
        }
        else{
            top = top + 1;
            arr[top] = n;
        }
            

    }

    void pop(){
        if(top == -1){
            return;
        }
        else{
            cout<<arr[top]<<"has been removed";
            top--;
        }
    }

    void display(){
        if(top == -1){
            return;
        }
        else{
            for(int i = top; i>=0; i--){
                cout<<arr[i];
            }
        }
    }
};


int main(){
    Stack S;
    S.push(100);
    S.display();
    S.pop();
    S.display();
    
}