import numpy as np

class RoboticArm:
    def __init__(self, joint_positions, link_lengths):
        self.joint_positions = joint_positions
        self.link_lengths = link_lengths

    def distance(self, p1, p2):
        return np.linalg.norm(p2 - p1)

    def forward_pass(self, target):
        self.joint_positions[-1] = target
        for i in range(len(self.joint_positions) - 2, -1, -1):
            direction = np.sign(np.subtract(self.joint_positions[i + 1], self.joint_positions[i]))
            self.joint_positions[i] = self.joint_positions[i + 1] - direction * self.link_lengths[i]

    def backward_pass(self, target):
        self.joint_positions[0] = target
        for i in range(len(self.joint_positions) - 1):
            direction = np.sign(np.subtract(self.joint_positions[i], self.joint_positions[i + 1]))
            self.joint_positions[i + 1] = self.joint_positions[i] - direction * self.link_lengths[i]

    def is_reachable(self, target):
        total_distance = sum(self.link_lengths)
        distance_to_target = self.distance(self.joint_positions[0], target)
        return distance_to_target <= total_distance
