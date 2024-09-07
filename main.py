import math

# 1. Defining the Points
points = [(1, 2), (4, 6), (7, 8), (10, 12)]

# 2. Writing a Function for Euclidean Distance
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 3. Calculating the Distances
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# 4. Finding the Minimum Distance
min_distance = min(distances)
print(f"Minimum Distance: {min_distance}")
