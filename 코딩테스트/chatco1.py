def solution(exp1, exp2):

    arr1 = exp1.split(' + ')
    arr1 += exp2.split(' + ')

    result = [0] * 101
    last_value = 101

    for str1 in arr1:
        exp = list(map(int,str1.split('x^')))
        if exp[1] < last_value:
            last_value = exp[1]
        result[exp[1]] += exp[0]
    
    answer = ''
    for i in reversed(range(101)):
        if result[i] >0:
            answer += str(result[i])+'x^'+str(i)
            if i != last_value:
                answer += ' + '

    return answer