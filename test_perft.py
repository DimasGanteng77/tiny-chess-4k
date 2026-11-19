import main, time

def perft(d):
    if d == 0:
        return 1
    n = 0
    for m in main.gen():
        main.make(m)
        if not main.atk(main.KW if main.SD < 0 else main.KB, main.SD):
            n += perft(d - 1)
        main.unmake()
    return n

main.parse("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
for d, want in ((1, 20), (2, 400), (3, 8902)):
    t = time.time()
    got = perft(d)
    print(f"perft({d}) = {got} want {want} {'OK' if got == want else 'FAIL'} {time.time()-t:.2f}s", flush=True)

# Kiwipete (position 2) perft 1-3: 48, 2039, 97862
main.parse("r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1")
for d, want in ((1, 48), (2, 2039), (3, 97862)):
    got = perft(d)
    print(f"kiwipete perft({d}) = {got} want {want} {'OK' if got == want else 'FAIL'}")

# Position 3 (ep + promotions): perft 1-3: 14, 191, 2812
main.parse("8/2p5/3p4/KP5r/1R3p1k/8/4P1P1/8 w - - 0 1")
for d, want in ((1, 14), (2, 191), (3, 2812)):
    got = perft(d)
    print(f"pos3 perft({d}) = {got} want {want} {'OK' if got == want else 'FAIL'}")

# Position 4 (bad castling/pins): perft 1-3: 6, 264, 9467
main.parse("r3k2r/Pppp1ppp/1b3nbN/nP6/BBP1P3/q4N2/Pp1P2PP/R2Q1RK1 w kq - 0 1")
for d, want in ((1, 6), (2, 264), (3, 9467)):
    got = perft(d)
    print(f"pos4 perft({d}) = {got} want {want} {'OK' if got == want else 'FAIL'}")

# Fool's mate: black to move mates in 1 (Qh4#) after 1.f3 e5 2.g4
main.parse("rnbqkbnr/pppp1ppp/8/4p3/6P1/5P2/PPPPP2P/RNBQKBNR b KQkq - 0 2")
mv = main.best("rnbqkbnr/pppp1ppp/8/4p3/6P1/5P2/PPPPP2P/RNBQKBNR b KQkq - 0 2",
               [main.uc(m) for m in main.gen()])
print("fools mate best:", mv, "(want d8h4)", flush=True)

# Speed: one best() call from startpos with the real node budget
main.parse("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
main.NB = 120000
t = time.time()
mv = main.best("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
               [main.uc(m) for m in main.gen()])
print(f"best() startpos: {mv} {main.NN} nodes in {time.time()-t:.2f}s = {main.NN/max(time.time()-t,0.01):.0f} nps", flush=True)
