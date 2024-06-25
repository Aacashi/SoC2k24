# ass1.py

class MathTools:
    total_calls = 0

    @staticmethod
    def derivative(func, x, h=1e-5):
        MathTools.total_calls += 1
        return (func(x + h) - func(x - h)) / (2 * h)

    @staticmethod
    def gradient(func, point, h=1e-5):
        MathTools.total_calls += 1
        grad = []
        for i in range(len(point)):
            def partial_func(x):
                point_copy = point.copy()
                point_copy[i] = x
                return func(point_copy)
            grad.append(MathTools.derivative(partial_func, point[i], h))
        return grad
