def solution(new_id):
    step1 = []
    for i in new_id:
        if ord('A') <= ord(i) <= ord('Z'):
            step1.append(chr(ord(i) + 32))
        else:
            step1.append(i)

    step2 = []
    for i in step1:
        if ord('a') <= ord(i) <= ord('z') or i.isdigit() == True or i == "-" or i == "_" or i == ".":
            step2.append(i)

    step3 = "".join(step2)
    for i in range(1000):
        if step3.find("..") != -1:
            step3 = step3.replace("..", ".")
        else:
            break

    step4 = []
    for i in range(len(step3)):
        if step3[i] != ".":
            step4.append(step3[i])
        elif step3[i] == ".":
            if i == 0 or i == len(step3) - 1:
                continue
            else:
                step4.append(step3[i])

    if len(step4) == 0:
        return ("a" * 3)

    step5 = step4
    while len(step5) >= 16:
        step5.pop()
    if step5[-1] == ".":
        step5.pop()

    step6 = step5
    while len(step6) <= 2:
        step6.append(step6[-1])

    step7 = "".join(step6)
    return (step7)