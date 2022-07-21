# Note: This is also a valid one-liner, although it's not as cool
[   # Size input
    n := int(input("size: ")),

    # Board creation
    b := [[0 for _ in range(n)] for __ in range(n)],

    # Check for a win
    c := lambda b: any(abs(sum(l)) == len(b) for l in b) or abs(sum(b[i][i] for i in range(len(b)))) == len(b),

    # Print function
    p := lambda b: [print(l) for l in b],

    inp := lambda b, val: ([[b[k][l] + (val if i == k and l == j else 0) for l in range(len(b))] for k in range(len(b))]) if 0 <= (
        i := int(input(f"Enter y cords for {val}: "))) < len(b) and 0 <= (j := int(
        input(f"Enter x cords for {val}: "))) < len(b) and b[i][j] == 0 else inp(b, val),

    # Check if game is a draw
    dn := lambda b: all(v != 0 for l in b for v in l),

    # Single turn
    g := lambda b, turn: exit() if p(b) and (c(b) or c([[b[j][i] for j in range(len(b))] for i in range(len(b) - 1, -1, -1)]) or dn(
     b)) else inp(b, turn),

    # Main loop
    l := lambda b, turn: l(g(b, turn), -turn),

    # Function call
    l(b, 1)]
