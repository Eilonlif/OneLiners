[n := int(input("Size: ")), b := [[0 for _ in range(n)] for __ in range(n)], (l := lambda b, turn: l((lambda b, turn: exit() if (lambda b: [print(l) for l in b])(b) and ((c := (lambda b: any(abs(sum(l)) == len(b) for l in b) or abs(sum(b[i][i] for i in range(len(b)))) == len(b)))(b) or c([[b[j][i] for j in range(len(b))] for i in range(len(b) - 1, -1, -1)]) or (lambda b: all(v != 0 for l in b for v in l))(b)) else (inp := (lambda b, val: ([[b[k][l] + (val if i == k and l == j else 0) for l in range(len(b))] for k in range(len(b))]) if 0 <= (i := int(input(f"y {val}: "))) < len(b) and 0 <= (j := int(input(f"x {val}: "))) < len(b) and b[i][j] == 0 else inp(b, val)))(b, turn))(b, turn), -turn))(b, 1)]
