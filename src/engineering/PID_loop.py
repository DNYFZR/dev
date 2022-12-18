# PID controller class
class PID:
    def __init__(self, p, i, d, dT):
        self.n_p, self.n_i, self.n_d = p, i, d
        self.i = 0
        self.d = 0
        self.dT = dT
        self.prev = 0

    def control(self, e):
        self.i += self.dT * e                # integral term
        self.d += (self.d - self.prev) / self.dT  # derivative term
        self.prev = e 

        return self.n_p * e + self.n_i * self.i + self.n_d * self.d


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    duration_seconds = 10_000
    
    control_response = [1]
    
    for i in range(1, duration_seconds):
        e = i/i**0.5
        loop = PID(p=0.05, i=0.01, d=0.0001, dT=i).control(e=e) 
        control_response.append(loop)
    
    plt.plot(control_response)
    plt.show()