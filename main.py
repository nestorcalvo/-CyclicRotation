def solution(A, K):
    # write your code in Python 3.6
    temp = A[:]
    if len(A) == 0:
        return A
    if K >= len(A) or K == 0:
        K = K % len(A)
        if K == 0:
            return A
    for i in range(len(A)):
        if i < K:
            temp[i] = A[len(A) + i - K]
        else:
            temp[i] = A[i - K]
    return temp


if __name__ == '__main__':
    A = [2, 4, 6, 8]
    K = 2
    print(solution(A, K))
