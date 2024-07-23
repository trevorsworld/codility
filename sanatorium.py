def solution(A):
    A.sort()

    rooms = 0
    i = 0

    while i < len(A):
        rooms += 1
        current_room_max = A[i]
        count = 0

        while i < len(A) and count < current_room_max:
            count += 1
            i += 1
    
    return rooms

# print(solution([1, 1, 1, 1, 1]))
# print(solution([2, 4, 4, 4, 4, 4]))
# print(solution([7, 3, 1, 1, 4, 5, 4, 9]))