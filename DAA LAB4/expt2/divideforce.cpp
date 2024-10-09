#include <iostream>
#include <string>
#include <algorithm>
#include<cmath>
#include <vector>
using namespace std;


string addStrings(const string& num1, const string& num2) {
    string result;
    int carry = 0;
    int i = num1.length() - 1, j = num2.length() - 1;


    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0) sum += num1[i--] - '0';
        if (j >= 0) sum += num2[j--] - '0';
        carry = sum / 10;
        result.push_back(sum % 10 + '0');
    }


    reverse(result.begin(), result.end());
    return result;
}




string subtractStrings(const string& num1, const string& num2) {
    string result;
    int borrow = 0;
    int i = num1.length() - 1, j = num2.length() - 1;


    while (i >= 0 || j >= 0) {
        int sub = borrow;
        if (i >= 0) sub += num1[i--] - '0';
        if (j >= 0) sub -= num2[j--] - '0';
        if (sub < 0) {
            sub += 10;
            borrow = 1;
        } else {
            borrow = 0;
        }
        result.push_back(sub + '0');
    }


    // Remove leading zeros and reverse the result
    while (result.length() > 1 && result.back() == '0') {
        result.pop_back();
    }
    reverse(result.begin(), result.end());
    return result.empty() ? "0" : result;
}




string karatsuba(const string& num1, const string& num2) {
   
    if (num1.length() == 0 || num2.length() == 0)
        return "0";  
    if (num1.length() == 1 || num2.length() == 1)
        return to_string(stoi(num1) * stoi(num2));


   
    int n = max(num1.length(), num2.length());
    int half = (n + 1) / 2;
   
    string a = num1.substr(0, num1.length() - half);
    string b = num1.substr(num1.length() - half);
    string c = num2.substr(0, num2.length() - half);
    string d = num2.substr(num2.length() - half);


   
    string ac = karatsuba(a, c);
    string bd = karatsuba(b, d);
    string abcd = karatsuba(addStrings(a, b), addStrings(c, d));


   
    string middle_term = subtractStrings(abcd, addStrings(ac, bd));


   
    string result = addStrings(addStrings(ac + string(2 * half, '0'), middle_term + string(half, '0')), bd);
   
    return result;
}




int main()
{
    cout<<"\n";
    cout << "Using karatsuba : " << "\n";
    string num1_10_1 = "1234567890";
    string num2_10_1 = "9876543210";
    cout << "Test Case 1 (10 digits):" << endl;
    cout << "Result: " << karatsuba(num1_10_1, num2_10_1) << endl;


    cout<<"\n";
    string num1_10_2 = "1029384756";
    string num2_10_2 = "5647382910";
    cout << "Test Case 2 (10 digits):" << endl;
    cout << "Result: " << karatsuba(num1_10_2, num2_10_2) << endl;


    cout<<"\n";
    string num1_50_1 = "12345678901234567890123456789012345678901234567890";
    string num2_50_1 = "98765432109876543210987654321098765432109876543210";
    cout << "Test Case 3 (50 digits):" << endl;
    cout << "Result: " << karatsuba(num1_50_1, num2_50_1) << endl;


    cout<<"\n";
    string num1_50_2 = "10293847561029384756102938475610293847561029384756";
    string num2_50_2 = "56473829105647382910564738291056473829105647382910";
    cout << "Test Case 4 (50 digits):" << endl;
    cout << "Result: " << karatsuba(num1_50_2, num2_50_2) << endl;


    cout<<"\n";
    string num1_100_1 = "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890";
    string num2_100_1 = "9876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210";
    cout << "Test Case 5 (100 digits):" << endl;
    cout << "Result: " << karatsuba(num1_100_1, num2_100_1) << endl;


    cout<<"\n";
    string num1_100_2 = "1029384756102938475610293847561029384756102938475610293847561029384756102938475610293847561029384756";
    string num2_100_2 = "5647382910564738291056473829105647382910564738291056473829105647382910564738291056473829105647382910";
    cout << "Test Case 6 (100 digits):" << endl;
    cout << "Result: " << karatsuba(num1_100_2, num2_100_2) << endl;


    cout<<"\n";
    string num1_500_1 = "1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890";
    string num2_500_1 = "9876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210";
    cout << "Test Case 7 (500 digits):" << endl;
    cout << "Result: " << karatsuba(num1_500_1, num2_500_1) << endl;


    cout<<"\n";
    string num1_500_2 = "1029384756102938475610293847561029384756102938475610293847561029384756102938475610293847561029384756102938475610293847561029384756102938475610293847561029384756102938475610293847561029384756102938475610293847561029384756102938475610293847561029384756";
    string num2_500_2 = "5647382910564738291056473829105647382910564738291056473829105647382910564738291056473829105647382910564738291056473829105647382910564738291056473829105647382910564738291056473829105647382910564738291056473829105647382910564738291056473829105647382910";
    cout << "Test Case 8 (500 digits):" << endl;
    cout << "Result: " << karatsuba(num1_500_2, num2_500_2) << endl;


    cout<<"\n";
    string num1_1000_1 = "123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890";
    string num2_1000_1 = "987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210987654321098765432109876543210";
    cout << "Test Case 9 (1000 digits):" << endl;
    cout << "Result: " << karatsuba(num1_1000_1, num2_1000_1) << endl;
    return 0;
}
