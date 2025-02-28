// implement an appllication of DFS such as to find a path from source to gole in a maze

#include <bits/stdc++.h>
using namespace std;

#define MAX 10 // Maximum maze size
// maze dimensions
int n, m;
int maze[MAX][MAX];     // Maze matrix
bool visited[MAX][MAX]; // Visited array for DFS

// Directions to move in the maze(right, down, left, up)

int dx[] = {0, 1, 0, -1};
int dy[] = {1, 0, -1, 0};

// Function to print the maze
void printMaze()
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (maze[i][j] == 1)
            {
                cout << "#"; // wall
            }
            else if (maze[i][j] == 0)
            {
                cout << "."; // path
            }
            else if (maze[i][j] == 2)
            {
                cout << "S"; // source
            }
            else if (maze[i][j] == 3)
            {
                cout << "G"; // Goal
            }

            else if (maze[i][j] == -1)
            {
                cout << "*"; // Path taken
            }
        }
        cout << endl;
    }
}

//DFS function to find the path
bool DFS(int x, int y, int goalX, int goalY)
{
    //if out of bounds or if the cell is a wall
    if (x < 0 || x >= n || y < 0 || y >= m )
    {
        return false;
    }

    //if it's all ready visited
    if (maze[x][y] == 1 || visited[x][y])
    {
        return false;
    }
    

    //mark the path
    maze[x][y] = -1;
    //explore all 4 directions
    for (int i = 0; i < 4; i++)
    {
         int newX = x + dx[i];
            int newY = y + dy[i];
            if (newX == goalX && newY == goalY)
            {
                return true;
            }
    }


}

int main()
{
    cout<<"Enter the dimensions of the maze: ";
    cin>>n>>m;
    //input the maze
    cout<<"Enter the maze (0 for path, 1 for wall, 2 for source, 3 for goal): ";
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            cin>>maze[i][j];
            visited[i][j]=false;
        }
    }
    int startX, startY, goalX, goalY;
    cout<<"Enter the source coordinates: ";
}