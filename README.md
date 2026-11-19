# tiny-chess-01 entry

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/dimasganteng77/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/DimasGanteng77/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

An original chess engine written from scratch for the 4 KB limit: a 0x88 board with negamax alpha-beta search, iterative deepening under a time budget of ~8.0 s per move (leaving ~2 s of margin under the 10 s limit), a transposition table with incremental Zobrist hashing, null-move pruning, late-move reductions, captures-only quiescence search with check evasions, MVV-LVA capture ordering plus killer and transposition-table move ordering, and a formula evaluation (material, pawn advancement, piece centrality, development bonus, doubled/passed pawns, king safety/endgame centralisation, bishop pair). The readable source is `engine.py`; `main.py` is the packed entry (3,329 bytes) produced by `makefun compress`.

## Verification

Independently verified against the packed `main.py`:

- **Move generation (perft):** start position depth 1/2/3 = 20 / 400 / 8,902 nodes — matches the known-correct counts. Kiwipete depth 2 = 2,039 and depth 3 = 97,862 nodes — matches the known-correct counts. A promotion-heavy test position gives depth 1/2 = 24 / 496 — matches.
- **Captures-only generator:** `gen(1)` produces exactly the same move set as the filtered full generator on 92 test positions (0 mismatches), including promotions, en passant and castling cases.
- **Best move is legal and on time:** from the start position the engine returns d2d3 in ~8.0 s; the slowest move observed across five test positions (start, Kiwipete, Sicilian, Italian, endgame) is 8.07 s, under the 10 s limit. Every returned move is legal.
- **Speed:** ~23,000–36,000 nodes/sec depending on position (Kiwipete slowest, endgames fastest); ~160,000–350,000 nodes per move at the 8.0 s budget.
- **Match vs the previous version:** 2–2 over four games at a matched ~0.4 s/move budget, plus one draw at 1.0 s/move — an even, noisy signal at matched time; the new version's edge is the longer budget it uses in real play (8.0 s vs the old 3.0 s per move).

## Run it

The harness runs the entry as:

```sh
python3 -P -s main.py
```

with `MAKEFUN_PROMPT_FILE` pointing at `/input/prompt.txt` and `MAKEFUN_ENV_URL` pointing at the game server. The engine reads the prompt, then plays over the server API (`POST /game`, `POST /move`, `POST /resign`), one UCI move per turn, until the game ends.
