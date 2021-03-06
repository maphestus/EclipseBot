import dice


def check(skill):
    roll = dice.roll('2d10')
    if roll[0] == 10:
        roll[0] = 0
    else:
        roll[0] = roll[0]*10
    if roll[1] == 10:
        roll[1] = 0
    print('Player rolled', roll[0], roll[1])
    result = roll[0] + roll[1]
    print('Target:', skill, 'Result:', result)
    if roll[0]/10 == 9 and roll[1] == 9:
        msg = 'Critical Failure!'
        return result, msg
    if roll[0] == 0 and roll[1] == 0:
        msg = 'Critical Success!'
        return result, msg

    if result <= skill:
        if roll[0]/10 == roll[1]:
            msg = 'Critical Success!'
            return result, msg
        if result >= 66:
            msg = 'Double Superior Success'
            return result, msg
        if result >= 33:
            msg = 'Superior Success'
            return result, msg
        msg = 'Success'
        return result, msg
    else:
        if roll[0]/10 == roll[1]:
            msg = 'Critical Failure!'
            return result, msg
        if result <= 33:
            msg = 'Double Superior Failure'
            return result, msg
        if result <= 66:
            msg = 'Superior Failure'
            return result, msg
        msg = 'Failure'
        return result, msg

# print(check(70))
