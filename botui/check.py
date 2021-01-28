
def check(str,usertext,id):
    if id+1>len(str):
        return -1
    else:
        for i in str[id]:
            if i in usertext:
                return id+1

    return check(str,usertext,id+1)                


