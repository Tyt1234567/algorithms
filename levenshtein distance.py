a = 'still'
b = 'ill'
c = 'fill'

error = 'sill'

def tail(a):
    return a[1:]

def lev(err,cor):
    if len(err) == 0:
        return len(cor)
    elif len(cor) == 0:
        return len(err)
    elif cor[0] == err[0]:
        return lev(tail(err),tail(cor))
    else:
        return 1+min(lev(tail(err),cor),lev(err,tail(cor)),lev(tail(cor),tail(err)))

simi = lev(c,error)
print(simi)