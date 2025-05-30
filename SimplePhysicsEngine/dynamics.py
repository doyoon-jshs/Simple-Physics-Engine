PIXELS_PER_METER = 100

class Body:
    def __init__(self, x_m, y_m, radius_m, mass_kg=1.0):
        self.x = x_m
        self.y = y_m
        self.vx = 0.0
        self.vy = 0.0
        self.ax = 0.0
        self.ay = 9.8  # 중력
        self.radius = radius_m
        self.mass = mass_kg

    def apply_force(self, fx, fy):
        self.ax += fx / self.mass
        self.ay += fy / self.mass

    def update(self, dt):
        self.vx += self.ax * dt
        self.vy += self.ay * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.ax = 0
        self.ay = 9.8  # 계속 중력 유지
