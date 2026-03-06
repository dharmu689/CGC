#include <bits/stdc++.h>
using namespace std;

int main()
{
    string S;
    cout << "Enter String : ";
    cin >> S;

    if (S.empty())
    {
        cout << 0 << endl;
        return 0;
    }

    int max_length = 1, current_length = 1;
    for (int i = 1; i < S.length(); i++)
    {
        if (S[i] == S[i - 1])
        {
            current_length++;
            if (current_length > max_length)
                max_length = current_length;
        }
        else
        {
            current_length = 1;
        }
    }

    cout << "Max consecutive: " << max_length << endl;
    return 0;
}
