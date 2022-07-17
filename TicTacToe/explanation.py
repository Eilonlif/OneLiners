# Note: This is also a valid one-liner, although it's not as cool
[   # Size input
    n := int(input("size: ")),

    # Board creation
    b := [[0 for _ in range(n)] for __ in range(n)],

    # Check for a win
    c := lambda b: any(abs(sum(l)) == len(b) for l in b) or abs(sum(b[i][i] for i in range(len(b)))) == len(b),

    # Print function
    p := lambda b: [print(l) for l in b],

    # Summing two matrices function, this is for the input
    sm := lambda a, b: list(map(list, map(lambda i: map(lambda x, y: x + y, a[i], b[i]), range(len(a))))),

    # Creating temporary matrix for the input
    cm := lambda y, x, s, val: [[0 if j != x else 0 if y != i else val for j in range(s)] for i in range(s)],

    # Taking an input
    inp := lambda b, val: (x := sm(b, cm(i, j, len(b), val)), p(x)) if 0 <= (
     i := int(input(f"Enter y cords for {val}: "))) < len(b) and 0 <= (j := int(
     input(f"Enter x cords for {val}: "))) < len(b) and b[i][j] == 0 else inp(b, val)[0],

    # Check if game is a draw
    dn := lambda b: all(v != 0 for l in b for v in l),

    # Single turn
    g := lambda b, turn: exit() if c(b) or c([[b[j][i] for j in range(len(b))] for i in range(len(b) - 1, -1, -1)]) or dn(
     b) else inp(b, turn)[0],

    # Main loop
    l := lambda b, turn: l(g(b, turn), -turn),

    # Function call
    l(b, 1)]
