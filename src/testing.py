from src.Queue import Queue


def test():
    arr = [
        ["P1", 6, 3],
        ["P2", 1, 6],
        ["P3", 4, 4],
        ["P5", 3, 2]
    ]
    arr.sort(key=lambda x:x[1])
    print(arr)

    tQ = Queue()
    for item in arr:
        tQ.add(item)

    print(tQ.queue)
