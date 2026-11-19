# tiny-chess-01 entry

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/dimasganteng77/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/DimasGanteng77/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

An original chess engine written from scratch for the 4 KB limit: a 0x88 board with negamax alpha-beta search, iterative deepening under a fixed 120,000-node budget (deterministic, no clock), quiescence search over captures and promotions with check evasions, MVV-LVA capture ordering plus killer moves, and a formula evaluation (material, pawn advancement, piece centrality, king safety/endgame centralisation, bishop pair). The readable source is `engine.py`; `main.py` is the packed entry (2,548 bytes) produced by `makefun compress`.
