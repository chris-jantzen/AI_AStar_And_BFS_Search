# AI_AStar_And_BFS_Search

Implementation of BFS and A\* search for AI class using Python

## Heuristics for A\*

Calculated by checking how many are not in their correct spots or by the Manhattan distance (Shortest path to the correct spot on the board)

### To Run

python3 main.py 'Search Type' 'Start State' 'Goal State'

| Item        | Type           | Values                                                             |
| ----------- | -------------- | ------------------------------------------------------------------ |
| Search Type | String         | 'bfs', 'h1', 'h2'                                                  |
| Start State | List as String | List of numbers 0-19 with no duplicates with quotes surrounding it |
| Goal State  | List as String | List of numbers 0-19 with no duplicates with quotes surrounding it |

#### Example State Input

```bash
python3 CAJSourceCodeFile.py 'bfs' '[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 12, 13, 14, 15, 16, 17, 18, 19]' '[1, 2, 3, 0, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]'
```
