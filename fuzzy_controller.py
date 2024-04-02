class FuzzyController:

    def mem_colse_L(self, x):
        if 0 <= x < 50:
            return 1 - x / 50
        return 0

    def mem_far_L(self, x):
        if 100 >= x > 50:
            return x / 50 - 1
        return 0

    def mem_moderate_L(self, x):
        if 35 < x < 50:
            return x / 15 - 7 / 3
        if 65 > x >= 50:
            return 13 / 3 - x / 15
        return 0

    def mem_colse_R(self, x):
        if 0 <= x < 50:
            return 1 - x / 50
        return 0

    def mem_far_R(self, x):
        if 100 >= x > 50:
            return x / 50 - 1
        return 0

    def mem_moderate_R(self, x):
        if 35 < x < 50:
            return x / 15 - 7 / 3
        if 65 > x >= 50:
            return 13 / 3 - x / 15
        return 0




    def mem_high_right(self, x):
        if -50 <= x <= -20:
            return x / 30 + 50 / 30
        if -20 < x < -5:
            return -1 / 3 - x / 15
        return 0

    def mem_high_left(self, x):
        if 20 <= x < 50:
            return -x / 30 + 50 / 30
        if 20 > x > 5:
            return -1 / 3 + x / 15
        return 0

    def mem_low_right(self, x):
        if -10 > x > -20:
            return x / 10 + 2
        if -10 <= x < 0:
            return - x / 10
        return 0

    def mem_low_left(self, x):
        if 10 < x < 20:
            return -x / 10 + 2
        if 10 >= x > 0:
            return x / 10
        return 0

    def mem_nothing(self, x):
        if -10 < x <= 0:
            return x / 10 + 1
        if 10 > x > 0:
            return 1 - x / 10
        return 0

    def __init__(self):
        pass

    def decide(self, left_dist, right_dist):

        low_right = min(self.mem_colse_L(left_dist), self.mem_moderate_R(right_dist))
        high_right = min(self.mem_colse_L(left_dist), self.mem_far_R(right_dist))
        low_left = min(self.mem_moderate_L(left_dist), self.mem_colse_R(right_dist))
        high_left = min(self.mem_far_L(left_dist), self.mem_colse_R(right_dist))
        nothing = min(self.mem_moderate_L(left_dist), self.mem_moderate_R(right_dist))

        def max_function(x):
            return max(min(low_right, self.mem_low_right(x)),
                       min(high_right, self.mem_high_right(x)),
                       min(low_left, self.mem_low_left(x)),
                       min(high_left, self.mem_high_left(x)),
                       min(nothing, self.mem_nothing(x)))

        x = -50
        b = +50
        makhraj = 0.0
        soorat = 0.0
        while x < b:
            x = x + 0.1
            makhraj = makhraj + max_function(x) * 0.1
            soorat = soorat + max_function(x) * 0.1 * x
        if makhraj != 0:
            return float(soorat) / float(makhraj)
        return 0
