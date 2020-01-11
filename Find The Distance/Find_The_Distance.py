from math import sqrt
def find_distance_between_two_points(x,y):
    distance = round(sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2),2)
    return distance

print(find_distance_between_two_points([0,1],[1,0]))
    