def counter(maximum):
    """Generate numbers from 0 to maximum - 1."""
    n = 1
    while n < maximum:
        yield f"hello {n}"
        n += 1
for msg in counter(5):
    print(msg)