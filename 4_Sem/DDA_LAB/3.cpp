#include <bits/stdc++.h>
using namespace std;

const int INF = 1000000;
int n, dis[10][10], dp[10][10];
bool visited[10];
int tsp(int pos, int count)
{
    if (count == n)
        return dis[pos][0];
    if (dp[pos][count] != -1)
        return dp[pos][count];
    int ans = INF;
    for (int city = 0; city < n; city++)
    {
        if (!visited[city])
        {
            visited[city] = true;
            ans = min(ans, dis[pos][city] + tsp(city, count + 1));
            visited[city] = false;
        }
    }
    return dp[pos][count] = ans;
}
int main()
{
    cout << "enter no. of cities: ";
    cin >> n;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            dp[i][j] = -1;
    cout << "distance matrix: ";
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cin >> dis[i][j];
    visited[0] = true;
    cout << "min list: " << tsp(0, 1) << endl;
    return 0;
}