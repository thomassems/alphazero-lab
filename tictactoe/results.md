The results below come from running MCTS for 1000 iterations on an empty tic-tac-toe board, repeated across three independent runs. Each table shows, for every possible opening move, how many simulations MCTS spent on it (visits), the accumulated reward (wins), and the resulting win rate (win%).

## Run 1

Root visits: 1000

| Move   | Visits | Wins  | Win% |
| ------ | -----: | ----: | ---: |
| (1, 1) |    219 | 166.5 | 0.76 |
| (0, 0) |    165 | 119.0 | 0.72 |
| (0, 2) |    161 | 116.0 | 0.72 |
| (2, 2) |    118 |  78.5 | 0.67 |
| (1, 2) |    100 |  64.0 | 0.64 |
| (2, 1) |     76 |  44.5 | 0.59 |
| (1, 0) |     70 |  39.5 | 0.56 |
| (0, 1) |     47 |  21.5 | 0.46 |
| (2, 0) |     44 |  19.5 | 0.44 |

Best move: (1, 1)

## Run 2

Root visits: 1000

| Move   | Visits | Wins  | Win% |
| ------ | -----: | ----: | ---: |
| (1, 1) |    185 | 139.5 | 0.75 |
| (0, 2) |    158 | 115.5 | 0.73 |
| (2, 2) |    155 | 112.5 | 0.73 |
| (2, 0) |    123 |  86.0 | 0.70 |
| (0, 1) |     85 |  53.0 | 0.62 |
| (2, 1) |     82 |  50.5 | 0.62 |
| (1, 2) |     79 |  48.0 | 0.61 |
| (0, 0) |     76 |  45.0 | 0.59 |
| (1, 0) |     57 |  30.0 | 0.53 |

Best move: (1, 1)

## Run 3

Root visits: 1000

| Move   | Visits | Wins  | Win% |
| ------ | -----: | ----: | ---: |
| (1, 1) |    226 | 177.0 | 0.78 |
| (0, 2) |    149 | 108.0 | 0.72 |
| (2, 2) |    149 | 108.0 | 0.72 |
| (0, 1) |    107 |  72.0 | 0.67 |
| (1, 2) |     93 |  59.5 | 0.64 |
| (2, 0) |     87 |  55.0 | 0.63 |
| (0, 0) |     70 |  40.5 | 0.58 |
| (2, 1) |     62 |  34.5 | 0.56 |
| (1, 0) |     57 |  30.5 | 0.54 |

Best move: (1, 1)

Across all three runs, MCTS consistently chose the center square (1, 1) as the best opening move. It earned both the most visits and the highest win rate against a random-rollout opponent, which matches the known theory that the center is the strongest first move in tic-tac-toe.