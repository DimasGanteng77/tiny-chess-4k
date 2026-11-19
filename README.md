# tiny-chess-01 entry

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/dimasganteng77/tiny-chess-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/DimasGanteng77/tiny-chess-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

An original chess engine written from scratch for the 4 KB limit: a 0x88 board with negamax alpha-beta search, iterative deepening under a fixed 120,000-node budget (deterministic, no clock), quiescence search over captures and promotions with check evasions, MVV-LVA capture ordering plus killer moves, and a formula evaluation (material, pawn advancement, piece centrality, king safety/endgame centralisation, bishop pair). The readable source is `engine.py`; `main.py` is the packed entry (2,548 bytes) produced by `makefun compress`.

## Verification

Independently verified against the packed `main.py`:

- **Move generation (perft):** start position depth 1/2/3 = 20 / 400 / 8,902 nodes — matches the known-correct counts. Kiwipete depth 2 = 2,039 nodes — matches the known-correct count.
- **Best move from the start position is legal:** the engine returns Nc3 in ~3.0 s.
- **Match vs the 1-ply starter:** 4–0, all four games won by checkmate.
- **Speed:** ~36,000–41,000 nodes/sec; the fixed 120,000-node budget works out to ≈ 2.9 s per move.

## Run it

The harness runs the entry as:

```sh
python3 -P -s main.py
```

with `MAKEFUN_PROMPT_FILE` pointing at `/input/prompt.txt` and `MAKEFUN_ENV_URL` pointing at the game server. The engine reads the prompt, then plays over the server API (`POST /game`, `POST /move`, `POST /resign`), one UCI move per turn, until the game ends.
