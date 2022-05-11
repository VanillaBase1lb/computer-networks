#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int parent[11] = {-1};
int dis[11] = {0};

vector<vector<pair<int, int>>> FormAdjList()
{
    vector<vector<pair<int, int>>> adjList;

    const int n = 11;

    for (int i = 0; i < n; i++)
    {
        vector<pair<int, int>> row;
        adjList.push_back(row);
    }

    adjList[0].push_back(make_pair(1, 2));
    adjList[0].push_back(make_pair(2, 3));
    adjList[0].push_back(make_pair(7, 6));

    adjList[1].push_back(make_pair(0, 2));
    adjList[1].push_back(make_pair(1, 9));
    adjList[1].push_back(make_pair(2, 4));
    adjList[1].push_back(make_pair(3, 4));
    adjList[1].push_back(make_pair(5, 1));
    adjList[1].push_back(make_pair(7, 10));

    adjList[2].push_back(make_pair(0, 3));
    adjList[2].push_back(make_pair(1, 4));
    adjList[2].push_back(make_pair(5, 2));

    adjList[3].push_back(make_pair(1, 4));
    adjList[3].push_back(make_pair(4, 1));
    adjList[3].push_back(make_pair(6, 2));
    adjList[3].push_back(make_pair(8, 1));

    adjList[4].push_back(make_pair(3, 1));
    adjList[4].push_back(make_pair(5, 2));
    adjList[4].push_back(make_pair(6, 1));

    adjList[5].push_back(make_pair(1, 1));
    adjList[5].push_back(make_pair(2, 2));
    adjList[5].push_back(make_pair(4, 2));
    adjList[5].push_back(make_pair(6, 7));
    adjList[5].push_back(make_pair(7, 3));

    adjList[6].push_back(make_pair(3, 2));
    adjList[6].push_back(make_pair(4, 1));
    adjList[6].push_back(make_pair(5, 7));
    adjList[6].push_back(make_pair(7, 4));
    adjList[6].push_back(make_pair(9, 3));

    adjList[7].push_back(make_pair(5, 3));
    adjList[7].push_back(make_pair(6, 4));
    adjList[7].push_back(make_pair(9, 5));

    adjList[8].push_back(make_pair(3, 1));
    adjList[8].push_back(make_pair(7, 9));
    adjList[8].push_back(make_pair(9, 20));
    adjList[8].push_back(make_pair(10, 11));

    adjList[9].push_back(make_pair(6, 3));
    adjList[9].push_back(make_pair(7, 5));
    adjList[9].push_back(make_pair(8, 20));
    adjList[9].push_back(make_pair(10, 7));

    adjList[10].push_back(make_pair(8, 11));
    adjList[10].push_back(make_pair(9, 7));

    return adjList;
}

void printPath(int parent[], int j)
{
    if (parent[j] == -1)
        return;

    printPath(parent, parent[j]);

    cout << " ->" << j;
}

int printSPT(int dist[], int n, int parent[])
{
    int src = 0;
    cout << "Vertex\t  Distance  \t\tPath";
    for (int i = 0; i < n; i++)
    {
        cout << "\n"
             << src << "-> " << i << "\t\t " << dist[i] << "\t\t " << src;
        printPath(parent, i);
    }
}

vector<int> Dijkstra(vector<vector<pair<int, int>>> &adjList, int &source)
{
    cout << "\nGetting the shortest path from " << source << " to all other nodes.\n";

    vector<int> dist;

    int n = adjList.size();

    for (int i = 0; i < n; i++)
    {
        dist.push_back(10000000);
    }

    // Yuvraj Mishra
    // 19XJ1A0576
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    pq.push(make_pair(source, 0));
    dist[source] = 0;

    while (pq.empty() == false)
    {
        int u = pq.top().first;
        cout << "U = " << u << endl;

        pq.pop();

        cout << "-----------------------" << endl;
        for (int i = 0; i < adjList[u].size(); i++)
        {

            int v = adjList[u][i].first;
            int weight = adjList[u][i].second;

            cout << "The Nodes adjacent to " << u << " are: \t";
            cout << "\t Node: " << v << "\t With Weight:" << weight << endl;

            if (dist[v] > dist[u] + weight)
            {
                parent[v] = u;
                dist[v] = dist[u] + weight;

                pq.push(make_pair(v, dist[v]));
                dis[v] = dist[v];
            }
            else
            {
                dis[v] = dist[v];
            }
        }
    }
    printSPT(dis, n, parent);
    return dist;
}

void PrintShortestPathTree(vector<int> &dist, int &source)
{

    cout << "\nPrinting the shortest path tree from node " << source << ".\n";
    for (int i = 0; i < dist.size(); i++)
    {
        cout << "The distance from node " << source << " to node " << i << " is: " << dist[i] << endl;
    }
}

int main(int argc, char *argv[])
{

    vector<vector<pair<int, int>>> adjList = FormAdjList();
    int node = 0;
    vector<int> dist = Dijkstra(adjList, node);
    PrintShortestPathTree(dist, node);

    return 0;
}

// Yuvraj Mishra
// 19XJ1A0576
