def reachDestination(sx,sy,dx,dy):
    if sx > dx or sy > dy:
        return 0
    if sx == dx and sy == dy:
        return 1
    
    if dx > dy:
        return reachDestination(sx, sy, dx-dy, dy)
    else:
        return reachDestination(sx, sy, dx, dy-dx)