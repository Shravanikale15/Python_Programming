def filterX(task,elements):
    result=[]
    for no in elements:
        ret=task(no)   #checkeven(no)
        if(ret==True):
            result.append(no)
    return result

def mapX(task,elements):
    result=[]
    for no in elements:
        ret=task(no)  #increment(no)
        result.append(ret)
    return result

def reduceX(task,elements):
    sum=0
    for no in elements:
        sum=task(sum,no)
    return sum
