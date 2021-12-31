def solution(progresses, speeds):
    day = 0
    answer = []
    while progresses:
        result = []
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        for i in range(len(speeds)):
            if progresses[i]>99:
                result.append(i)
            else:
                break
        for _ in result:
            progresses.pop(0)
            speeds.pop(0)
        if result:
            answer.append(len(result))

    return answer