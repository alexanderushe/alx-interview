#!/usr/bin/python3
''' a game given a set of consecutive
integers starting from 1 upto n
'''


def isWinner(x, nums):
    ''' x: number of rounds
    nums: array of integers
    '''
    maria_wins, ben_wins = 0, 0
    available_primes = set(nums)
    current_player = 'Maria'
    for _ in range(x):
        chosen_prime = min(available_primes)
        available_primes.remove(chosen_prime)
        for num in nums:
            if num % chosen_prime == 0:
                if num in available_primes:
                    available_primes.remove(num)
        if not available_primes:
            if current_player == 'Maria':
                ben_wins += 1
            else:
                maria_wins += 1
            break
        current_player = 'Ben' if current_player == 'Maria' else 'Maria'
    if maria_wins > ben_wins:
        return 'Maria'
    elif maria_wins < ben_wins:
        return 'Ben'
    else:
        return None
