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

The center square (1, 1) was usually the strongest opening — in the runs above it earned the most visits and the highest win rate against a random-rollout opponent, matching the known theory that the center is the best first move in tic-tac-toe. That said, it was not *always* picked as best: at 1000 iterations the results carry enough sampling noise that other moves, such as (2, 0), occasionally came out on top in individual runs. Over more iterations the center would win out more consistently.

Tracking losses separately (losses count only outright losses, since the win column already folds in draws as half-wins) showed that even the best opening moves still lose a meaningful share of games to a random opponent — the lowest loss rate observed was around 15%.

## Scaling up the iterations

The run-to-run disagreement above is a symptom of too few simulations. Increasing the iteration count ten-fold (to 10,000) and eventually to 1,000,000 removes that noise: at these scales, (1, 1) is picked as the best starting move **consistently**, every run. More simulations let MCTS concentrate its search on the genuinely strongest move instead of being swayed by lucky rollouts.

### 1,000,000 iterations

At one million iterations the engine's play is near-optimal, and the numbers change character. The center draws by far the most visits, and its loss rate collapses to roughly **2.3%** — versus ~8–10% for every other opening. Its win% hovers near 0.52 not because it rarely wins, but because it **draws the overwhelming majority of its games** (a win% of ~0.52 with only ~2.3% losses implies well over 90% draws). That matches the known theory that tic-tac-toe is a draw under good play — so the "best" move is really the one that most reliably avoids losing.

#### Run 1

Root visits: 1,000,000

| Move   | Visits | Wins     | Win%  | Loss% |
| ------ | -----: | -------: | ----: | ----: |
| (1, 1) | 288583 | 149409.0 | 51.77 |  2.30 |
| (0, 2) |  95190 |  48592.5 | 51.05 |  8.07 |
| (2, 0) |  93282 |  47602.5 | 51.03 |  8.09 |
| (0, 0) |  93256 |  47589.0 | 51.03 |  8.05 |
| (2, 2) |  92583 |  47239.5 | 51.02 |  8.10 |
| (1, 0) |  86532 |  44100.5 | 50.96 |  9.81 |
| (0, 1) |  84837 |  43222.0 | 50.95 |  9.88 |
| (2, 1) |  83390 |  42471.5 | 50.93 |  9.76 |
| (1, 2) |  82347 |  41932.0 | 50.92 |  9.92 |

Best move: (1, 1)

#### Run 2

Root visits: 1,000,000

| Move   | Visits | Wins     | Win%  | Loss% |
| ------ | -----: | -------: | ----: | ----: |
| (1, 1) | 294657 | 152627.0 | 51.80 |  2.30 |
| (2, 2) |  92854 |  47394.0 | 51.04 |  8.19 |
| (0, 2) |  92266 |  47089.0 | 51.04 |  8.16 |
| (2, 0) |  92172 |  47040.0 | 51.04 |  8.15 |
| (0, 0) |  90257 |  46046.0 | 51.02 |  8.11 |
| (0, 1) |  85055 |  43351.0 | 50.97 |  9.81 |
| (1, 0) |  84966 |  43301.5 | 50.96 |  9.79 |
| (1, 2) |  84268 |  42939.5 | 50.96 |  9.80 |
| (2, 1) |  83505 |  42543.5 | 50.95 |  9.91 |

Best move: (1, 1)

#### Run 3

Root visits: 1,000,000

| Move   | Visits | Wins     | Win%  | Loss% |
| ------ | -----: | -------: | ----: | ----: |
| (1, 1) | 283948 | 146990.0 | 51.77 |  2.31 |
| (0, 0) |  94043 |  47998.5 | 51.04 |  8.07 |
| (2, 2) |  93621 |  47779.5 | 51.04 |  8.10 |
| (0, 2) |  93384 |  47656.5 | 51.03 |  8.10 |
| (2, 0) |  93146 |  47533.0 | 51.03 |  8.09 |
| (1, 2) |  86159 |  43908.5 | 50.96 |  9.76 |
| (1, 0) |  85620 |  43629.0 | 50.96 |  9.72 |
| (0, 1) |  85459 |  43545.5 | 50.95 |  9.80 |
| (2, 1) |  84620 |  43110.0 | 50.95 |  9.82 |

Best move: (1, 1)