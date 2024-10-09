#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Function to perform long multiplication of two numbers as strings
string longMultiplication(string num1, string num2) {
    int len1 = num1.size();
    int len2 = num2.size();

    // Result can be at most len1 + len2 digits long
    vector<int> result(len1 + len2, 0);

    // Reverse both numbers for easier multiplication from least significant digit
    reverse(num1.begin(), num1.end());
    reverse(num2.begin(), num2.end());

    // Multiply each digit of num1 by each digit of num2
    for (int i = 0; i < len1; ++i) {
        for (int j = 0; j < len2; ++j) {
            int digit1 = num1[i] - '0';
            int digit2 = num2[j] - '0';
            result[i + j] += digit1 * digit2;
            result[i + j + 1] += result[i + j] / 10;  // Carry over
            result[i + j] %= 10;  // Keep remainder in current position
        }
    }

    // Convert result to a string
    string resultStr;
    bool foundNonZero = false;  // To avoid leading zeros

    for (int i = result.size() - 1; i >= 0; --i) {
        if (result[i] != 0) {
            foundNonZero = true;
        }
        if (foundNonZero) {
            resultStr.push_back(result[i] + '0');
        }
    }

    // If resultStr is empty, the result is 0
    return resultStr.empty() ? "0" : resultStr;
}

int main() {
    // Input two large numbers as strings
    string num1 = "12345678901234567890";  // 20-digit number
    string num2 = "98765432109876543210";  // 20-digit number

    // Perform long multiplication
    string result = longMultiplication(num1, num2);

    // Output the result
    cout << "Multiplication of " << num1 << " and " << num2 << ":\n";
    cout << result << endl;

    return 0;
}


