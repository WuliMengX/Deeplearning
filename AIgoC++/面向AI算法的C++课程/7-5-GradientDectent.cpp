#include <iostream>

using namespace std;

int main(){

    float x = 2;
    float t = x / 2;
    float L = (t * t - x) * (t * t - x);
    float a = 0.005;

    while (L > 1e-5)
    {
        float delta = 2 * (t * t - x) * 2 * t;
        t = t - a * delta;
        L = (t * t -x ) * (t * t - x);
    }
    
    cout << "result: " << t << endl;

    cout << "hello,world" << endl;
    
    return 0;
    
}