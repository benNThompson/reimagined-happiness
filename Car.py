import random
from math import pi

# Config type values
maxVectorsPerSegment = 8
maxWheelsPerSegment = 4

minVectorMagnitude = 5
maxVectorMagnitude = 150

minWheelSize = 5
maxWheelSize = 75


# Represents a single vector component of a car segment, plus the optional wheel
class Vector:
    def __init__(self, magnitude, direction, wheel_size):
        self.Magnitude = magnitude  # Length of the vector
        self.Direction = direction  # direction in radians, 0 is straight left
        self.WheelSize = wheel_size  # size of the wheel at the end of this segment, or 0 for no wheel


# Represents half a car
class CarSegment:
    def __init__(self, vectors):
        self.Vectors = vectors  # a car segment is just a list of vectors. They should be sorted by direction


# Represents a full car with all info
class Car:
    def __init__(self, left_segment, right_segment, left_join_vector, right_join_vector):
        # A car is the two segments, with the indices of the vectors to join them at
        self.LeftSegment = left_segment
        self.RightSegment = right_segment
        self.LeftJoinVector = left_join_vector
        self.RightJoinVector = right_join_vector


# Generate a new, fully random car
def random_car():
    segments = []
    for x in range(2):
        vectors = []
        num_wheels = 0
        for y in range(8):
            magnitude = random.randint(minVectorMagnitude, maxVectorMagnitude)
            direction = random.uniform(0, 2 * pi)
            wheel_size = 0
            if num_wheels < maxWheelsPerSegment:
                num_wheels += 1
                wheel_size = random.randint(minWheelSize, maxWheelSize)

            vectors.apppend(Vector(magnitude, direction, wheel_size))
        segments.append(vectors)
    return Car(segments[0], segments[1], random.randint(0, 7), random.randint(0, 7))
