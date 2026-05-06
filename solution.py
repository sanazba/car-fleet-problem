"""
LeetCode 853: Car Fleet

There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer arrays position and speed with length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is formed by cars that end up driving bumper to bumper. No two cars can be in the same position at the same time.

Return the number of car fleets that will arrive at the destination.
"""

def carFleet(target, position, speed):
    """
    Solution using stack approach.

    Key insight: Cars behind cannot overtake cars in front. If a car behind
    takes longer or equal time to reach target than the car in front,
    they form a fleet.

    Time Complexity: O(n log n) due to sorting
    Space Complexity: O(n) for the pairs and stack
    """
    # Create pairs of (position, speed) and sort by position in descending order
    # We start from the car closest to target
    pairs = [(p, s) for p, s in zip(position, speed)]
    pairs.sort(reverse=True)

    stack = []

    for pos, spd in pairs:
        # Calculate time to reach target for current car
        time_to_target = (target - pos) / spd

        # If stack is empty or current car takes more time than the car in front,
        # it forms a new fleet
        if not stack or time_to_target > stack[-1]:
            stack.append(time_to_target)
        # If current car takes less or equal time, it catches up with the fleet ahead
        # and doesn't form a new fleet (so we don't add it to stack)

    # Number of fleets = number of elements in stack
    return len(stack)


def carFleetAlternative(target, position, speed):
    """
    Alternative solution without using stack explicitly.
    Same logic but cleaner implementation.
    """
    # Create pairs and sort by position (closest to target first)
    pairs = sorted(zip(position, speed), reverse=True)

    fleets = 0
    prev_time = 0

    for pos, spd in pairs:
        time_to_target = (target - pos) / spd
        # If current car takes more time than previous car, it forms a new fleet
        if time_to_target > prev_time:
            fleets += 1
            prev_time = time_to_target

    return fleets


# Test cases
if __name__ == "__main__":
    # Test case 1
    target1 = 12
    position1 = [10, 8, 0, 5, 3]
    speed1 = [2, 4, 1, 1, 3]
    print(f"Test 1: {carFleet(target1, position1, speed1)}")  # Expected: 3

    # Test case 2
    target2 = 10
    position2 = [3]
    speed2 = [3]
    print(f"Test 2: {carFleet(target2, position2, speed2)}")  # Expected: 1

    # Test case 3
    target3 = 100
    position3 = [0, 2, 4]
    speed3 = [4, 2, 1]
    print(f"Test 3: {carFleet(target3, position3, speed3)}")  # Expected: 1# test
