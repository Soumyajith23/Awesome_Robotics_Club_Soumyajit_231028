from robotic_arm import RoboticArm
import numpy as np


def main():
    # Initial joint positions/angles input by user
    initial_joints = []
    print("Enter initial joint positions (x y z for each joint):")
    for i in range(4):
        x, y, z = map(float, input(f"Joint {i + 1}: ").split())
        initial_joints.append(np.array([x, y, z]))

    # Link lengths
    link_lengths = [23, 15, 8]

    # Target position input by user
    print("Enter target position (x y z):")
    x_target, y_target, z_target = map(float, input().split())
    target = np.array([x_target, y_target, z_target])

    # Create a RoboticArm instance
    arm = RoboticArm(initial_joints, link_lengths)

    # Check reachability
    reachable = arm.is_reachable(target)

    if reachable:
        print("Target point is reachable.")

        # Perform FABRIK algorithm
        tolerance = 0.01
        max_iterations = 1000
        iteration = 0
        while True:
            distance_to_target = arm.distance(arm.joint_positions[-1], target)
            if distance_to_target < tolerance or iteration >= max_iterations:
                break
            arm.forward_pass(target)
            arm.backward_pass(target)
            iteration += 1

        print("Final joint positions:", arm.joint_positions)
    else:
        print("Target point is not reachable.")


if __name__ == "__main__":
    main()
