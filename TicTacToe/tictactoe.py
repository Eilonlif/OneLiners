[n := int(input("Size:")), b := [[0 for _ in range(n)] for __ in range(n)], (l := lambda b, turn: l((lambda b,
                                                                                                            turn: exit() if (
                                                                                                                                lambda
                                                                                                                                    b: [
                                                                                                                                    print(
                                                                                                                                        l)
                                                                                                                                    for
                                                                                                                                    l
                                                                                                                                    in
                                                                                                                                    b])(
    b) and ((c := (lambda b: any(abs(sum(l)) == n for l in b) or abs(sum(b[i][i] for i in range(n))) == n))(b) or c(
    [[b[j][i] for j in range(n)] for i in range(n - 1, -1, -1)]) or (lambda b: sum(map(abs, sum(b, []))) == n ** 2)(
    b)) else (inp := (
    lambda b, val: ([[b[k][l] + (val if i == k and l == j else 0) for l in range(n)] for k in range(n)]) if 0 <= (
        i := int(input(f"y {val}:"))) < n and 0 <= (j := int(input(f"x {val}:"))) < len(b) and b[i][j] == 0 else inp(b,
                                                                                                                     val)))(
    b, turn))(b, turn), -turn))(b, 1)]
