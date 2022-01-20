def game(cash, user, sell, cost):
    orzi = cost//10
    rest = cost - cost//10
    if cost>=10:
        cash[sell] += rest
        if user[sell]:
            game(cash, user, user[sell], orzi)
    else:
        cash[sell] += cost
    

def solution(enroll, referral, seller, amount):
    user = {
        "minho":[]
    }
    cash = {
        "minho":0
    }
    for i, name in enumerate(enroll):
        if name not in user:
            user[name] = []
            cash[name] = 0
        if referral[i] == "-":
            user[name] = "minho"
        else:
            user[name] = referral[i]
    for i, sell in enumerate(seller):
        game(cash, user, sell, amount[i]*100)
    
    answer = []
    for name in enroll:
        answer.append(cash[name])
    return answer