# Note: This is also a valid one-liner, although it's not as cool
[  # Size input
    n := int(input("size: ")),

    # Board creation
    b := [[0 for _ in range(n)] for __ in range(n)],

    # Check for a win
    c := lambda b: any(abs(sum(l)) == n for l in b) or abs(sum(b[i][i] for i in range(n))) == n,

    # Print function
    # Swap 1 for X, -1 for O, 0 for space
    p := lambda b: [print([{x==1: "X", x==-1: "O"}.get(True, " ") for x in l]) for l in b],

    inp := lambda b, val: (
        [[b[k][l] + (val if i == k and l == j else 0) for l in range(n)] for k in range(n)]) if 0 <= (
        i := int(input(f"Enter y cords for {val}: "))) < n and 0 <= (j := int(
        input(f"Enter x cords for {val}: "))) < n and b[i][j] == 0 else inp(b, val),

    # Check if game is a draw
    dn := lambda b: sum(map(abs, sum(b, []))) == n ** 2,

    # Single turn
    g := lambda b, turn: exit() if p(b) and (
            c(b) or c([[b[j][i] for j in range(n)] for i in range(n - 1, -1, -1)]) or dn(b)) else inp(b, turn),

    # Main loop
    l := lambda b, turn: l(g(b, turn), -turn),

    # Function call
    l(b, 1)]
