def max_points(n, sequence):
    
    freq = [0] * (max(sequence) + 1)
    for num in sequence:
        freq[num] += num
        
    if len(freq) == 1:
        return freq[0]
    if len(freq) == 2:
        return max(freq)
    
    
    dp = [0] * len(freq)
    dp[0], dp[1] = freq[0], max(freq[0], freq[1])
    
   
    for i in range(2, len(freq)):
        dp[i] = max(dp[i-1], dp[i-2] + freq[i])
        
    return dp[-1]

n = int(input())
sequence = list(map(int, input().split()))
print(max_points(n, sequence))






