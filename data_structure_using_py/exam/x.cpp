 // C++ program to evaluate a prefix expression.
#include <bits/stdc++.h>

using namespace std;
 

bool isOperand(char c)
{
    return isdigit(c);
}
 

double evaluatePrefix(string exprsn)
{

    stack<double> Stack;
 

    for (int j = exprsn.size() - 1; j >= 0; j--) {
 

        // Push operand to Stack

        // To convert exprsn[j] to digit subtract

        // '0' from exprsn[j].

        if (isOperand(exprsn[j]))

            Stack.push(exprsn[j] - '0');
 

        else {
 

            // Operator encountered

            // Pop two elements from Stack

            double o1 = Stack.top();

            Stack.pop();

            double o2 = Stack.top();

            Stack.pop();
 

            // Use switch case to operate on o1

            // and o2 and perform o1 Or o2.

            switch (exprsn[j]) {

            case '+':

                Stack.push(o1 + o2);

                break;

            case '-':

                Stack.push(o1 - o2);

                break;

            case '*':

                Stack.push(o1 * o2);

                break;

            case '/':
                Stack.push(o1 / o2);
                break;
            }
        }
    }
    return Stack.top();
}
 
// Driver code

int main(){
    string exprsn = "%*/*90-/50+23^1251520";
    cout << evaluatePrefix(exprsn) << endl;
    return 0;
}