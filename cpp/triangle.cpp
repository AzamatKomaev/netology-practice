#include<iostream>
#include <cmath>

using namespace std;



int main() {
    float xa, ya, xb, yb, xc, yc;

    cout << "Enter coordinates for a: \n";
    cin >> xa;
    cin >> ya;

    cout << "Enter coordinates for b: \n";
    cin >> xb;
    cin >> yb;

    cout << "Enter coordinates for c: \n";
    cin >> xc;
    cin >> yc;

    float ab, bc, ca;
    ab = sqrt(pow(xb - xa, 2) + pow(yb - ya, 2)); // Length of ab
    bc = sqrt(pow(xc - xb, 2) + pow(yc - yb, 2)); // Length of bc
    ca = sqrt(pow(xa - xc, 2) + pow(ya - yc, 2)); // Length of ca

    float area = 0.5 * fabs(xa * (yb - yc) + xb * (yc - ya) + xc * (ya - yb));
    
    cout << "The perimeter of triangle is " << ab + bc + ca << "\n";
    cout << "The area of triangle is " << area;

    return 0;
}
