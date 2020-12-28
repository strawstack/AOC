import datetime

def log_minutes(minutes, guard_id, start, end):
    if not guard_id in minutes:
        minutes[guard_id] = {}
        for i in range(60): minutes[guard_id][i] = 0

    while start != end:
        m = int(start.strftime("%M"))
        minutes[guard_id][m] += 1
        start += datetime.timedelta(0, 60)



def sol():
    # [1518-02-06 00:46] falls asleep
    data = [x.strip() for x in open("d4.txt").readlines()]

    lst = []

    DATE, TYPE, ID = 0, 1, 2

    for row in data:
        mydate, msg = row.split("]")
        mydate = datetime.datetime.strptime(mydate, "[%Y-%m-%d %H:%M")
        msg = msg.strip()
        id = None

        if msg[:5] == "Guard":
            # Guard #373 begins shift
            type = "G"
            id = int(msg.split(" ")[1][1:])

        elif msg[:5] == "wakes":
            type = "W"

        else: # falls
            type = "F"

        lst.append( (mydate, type, id) )

    lst = sorted(lst, key=lambda x: x[0])

    guards = {}
    minutes = {}
    cur_guard = lst[0][ID]
    cur_sleep_time = 0

    for item in lst[1:]:
        if item[TYPE] == "W":
            #print("wake:", cur_guard)
            if not cur_guard in guards: guards[cur_guard] = 0
            sleep_time = (item[DATE] - cur_sleep_time).seconds//60

            log_minutes(minutes, cur_guard, cur_sleep_time, item[DATE])

            #print("time:", sleep_time)
            guards[cur_guard] += sleep_time

        elif item[TYPE] == "F":
            #print("fall:", cur_guard)
            cur_sleep_time = item[DATE]

        else:
            #print("new:", item[ID])
            cur_guard = item[ID]

    gid = None
    for k in guards:
        if gid == None: gid = k
        if guards[k] > guards[gid]:
            gid = k

    b_min = 0
    for m in minutes[gid]:
        if minutes[gid][m] > minutes[gid][b_min]:
            b_min = m

    # 48328
    return int(gid) * int(b_min)


# main
ans = sol()
print(ans)
