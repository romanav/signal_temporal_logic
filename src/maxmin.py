from collections import deque


def supermaxmin(a, w):

    maxfifo, minfifo = deque((0,)), deque((0,))
    lena = len(a)
    maxvalues = [None] * (lena - w + 1)
    minvalues = [None] * (lena - w + 1)
    for i in range(1, lena):
        if i >= w:
            maxvalues[i - w] = a[maxfifo[0]]
            minvalues[i - w] = a[minfifo[0]]
        if a[i] > a[i - 1]:
            maxfifo.pop()
            while maxfifo:
                if a[i] <= a[maxfifo[-1]]:
                    break
                maxfifo.pop()
        else:
            minfifo.pop()
            while minfifo:
                if a[i] >= a[minfifo[-1]]:
                    break
                minfifo.pop()
        maxfifo.append(i)
        minfifo.append(i)
        if i == (w + maxfifo[0]):
            maxfifo.popleft()
        elif i == (w + minfifo[0]):
            minfifo.popleft()
        maxvalues[lena - w] = a[maxfifo[0]]
        minvalues[lena - w] = a[minfifo[0]]
    return maxvalues, minvalues


if __name__ == '__main__':
    a = [9, 0, 5, 1, 11, 23, 55, 4, 16, 47, 33]
    w = 3
    print(supermaxmin(a, 3))