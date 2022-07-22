from permutations import f


def permutations(s: str):
    # Edge case
    if len(s) == 1:
        return {s}
    # Calculating sub-permutations
    perms = set()
    for i in range(len(s)):
        for perm in permutations(s[:i] + s[i + 1:]):
            perms.add(s[i] + perm)
    return perms


print(permutations('abc'))
print(f('abc'))
