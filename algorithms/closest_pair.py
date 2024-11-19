import math

# Distance function
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Brute force for small datasets
def brute_force(points):
    min_dist = float('inf')
    closest_pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = euclidean_distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])
    return min_dist, closest_pair

# Combine step
def strip_closest(strip, min_dist):
    strip.sort(key=lambda p: p[1])  # Sort by y-coordinate
    min_dist_pair = None
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= min_dist:
                break
            dist = euclidean_distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                min_dist_pair = (strip[i], strip[j])
    return min_dist, min_dist_pair

# Main divide-and-conquer function
def closest_pair_recursive(points):
    if len(points) <= 3:
        return brute_force(points)
    
    mid = len(points) // 2
    left = points[:mid]
    right = points[mid:]
    
    dl, pl = closest_pair_recursive(left)
    dr, pr = closest_pair_recursive(right)
    
    d = min(dl, dr)
    closest_pair = pl if dl < dr else pr

    # Create a strip of points within d distance from the dividing line
    strip = [p for p in points if abs(p[0] - points[mid][0]) < d]
    ds, ps = strip_closest(strip, d)
    
    if ds < d:
        return ds, ps
    else:
        return d, closest_pair

# Wrapper function
def closest_pair(points):
    points.sort(key=lambda p: p[0])  # Sort by x-coordinate
    return closest_pair_recursive(points)
