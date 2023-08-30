def solution(cards1, cards2, goal):
    answer = ''
    cards1Stack, cards2Stack = 0, 0

    for temp in goal:
        if cards1Stack < len(cards1) and cards1[cards1Stack] == temp:
            cards1Stack += 1
        elif cards2Stack < len(cards2) and cards2[cards2Stack] == temp:
            cards2Stack += 1
        else:
            answer = "No"

    if answer != "No":
        answer = "Yes"
    return answer
