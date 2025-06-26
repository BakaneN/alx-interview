def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    def count_primes(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        return sum(primes)

    maria = 0
    ben = 0

    for n in nums:
        prime_moves = count_primes(n)

        if prime_moves % 2 == 1:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
