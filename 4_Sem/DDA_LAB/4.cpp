#include <bits/stdc++.h>
using namespace std;

#define MAX 10
int adj[MAX][MAX];
bool visited[MAX];
int Stack[MAX];
int top = -1;
int v;
void push(int v)
{
    Stack[++top] = v;
}
int pop()
{
    return Stack[top--];
}
void topologicalSortUtil(int v)
{
    visited[v] = true;
    for (int i = 0; i < v; i++)
    {
        if (adj[v][i] == 1 && !visited[i])
        {
            topologicalSortUtil(i);
        }
    }
    push(v);
}

void topologicalSort()
{
    for (int i = 0; i < v; i++)
    {
        visited[i] = false;
    }
    for (int i = 0; i < v; i++)
    {
        if (!visited[i])
        {
            topologicalSortUtil(i);
        }
    }
    cout << "Topological Sort: ";
    while (top != -1)
    {
        cout << pop() << " ";
    }
    cout << endl;
}

int main()
{
    cout << "Enter no. of vertices: ";
    cin >> v;
     
    for (int i = 0; i < v; i++)
    {
        for (int j = 0; j < v; j++)
        {
            adj[i][j];
        }
    }
    int E;
    cout << "Enter no. of edges: ";
    cin >> E;
    cout << "Enter edges(U V) format (from U to V) : ";
    for (int i = 0; i < E; i++)
    {
        int u, v;
        cin >> u >> v;
        adj[u][v] = 1;
    }
    topologicalSort();
}
