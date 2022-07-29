f = lambda n, r=range, d=input: (l := lambda b, t: l((lambda b, t: exit() if [print(l) for l in b] and (
            (c := (lambda b: any(abs(sum(l)) == n for l in b) or abs(sum(b[i][i] for i in r(n))) == n))(b) or c(
        [[b[j][i] for j in r(n)] for i in r(n - 1, -1, -1)]) or sum(map(abs, sum(b, []))) == n ** 2) else (h := (
    lambda b, v: ([[b[k][l] + (v if i == k and l == j else 0) for l in r(n)] for k in r(n)]) if all(
        [0 <= (i := int(d())), (j := int(d())) < n]) and b[i][j] == 0 else h(b, v)))(b, t))(b, t), -t))(
    [[0 for _ in r(n)] for m in r(n)], 1)

f(3)
