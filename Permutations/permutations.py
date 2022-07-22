f = lambda s: s if len(s) == 1 else set(s[i] + p for i in range(len(s)) for p in f(s[:i] + s[i + 1:]))
