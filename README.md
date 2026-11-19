# tiny-chess-01 entry

An original chess engine written from scratch for the 4 KB limit: a 0x88 board with negamax alpha-beta search, iterative deepening under a fixed 120,000-node budget (deterministic, no clock), quiescence search over captures and promotions with check evasions, MVV-LVA capture ordering plus killer moves, and a formula evaluation (material, pawn advancement, piece centrality, king safety/endgame centralisation, bishop pair). The readable source is `engine.py`; `main.py` is the packed entry (2,548 bytes) produced by `makefun compress`.
