f = lambda n: (l := lambda b, t: l((lambda b, t: exit() if [print(l) for l in b] and (
            (c := (lambda b: any(abs(sum(l)) == n for l in b) or abs(sum(b[i][i] for i in range(n))) == n))(b) or c(
        [[b[j][i] for j in range(n)] for i in range(n - 1, -1, -1)]) or sum(map(abs, sum(b, []))) == n ** 2) else (
    h := (lambda b, v: ([[b[k][l] + (v if i == k and l == j else 0) for l in range(n)] for k in range(n)]) if all(
        [0 <= (i := int(input())), (j := int(input())) < len(b)]) and b[i][j] == 0 else h(b, v)))(b, t))(b, t), -t))(
    [[0 for _ in range(n)] for m in range(n)], 1)

f(3)
