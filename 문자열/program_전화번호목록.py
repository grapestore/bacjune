def solution(phone_book):
    answer = True
    hash_map = {}
    
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        
    for phone_number in phone_book:
        jubdo = ''
        for number in phone_number:
            jubdo += number
            if jubdo in hash_map and jubdo != phone_number:
                return False
    return True

print(solution(["119", "97674223", "1195524421"]))