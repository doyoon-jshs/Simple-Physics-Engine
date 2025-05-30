import math

def wall_collision(body, screen_width_px, screen_height_px, ppm):
    radius_px = body.radius * ppm
    x_px = body.x * ppm
    y_px = body.y * ppm

    if x_px - radius_px < 0:
        body.vx *= -1
        body.x = radius_px / ppm
    elif x_px + radius_px > screen_width_px:
        body.vx *= -1
        body.x = (screen_width_px - radius_px) / ppm

    if y_px - radius_px < 0:
        body.vy *= -1
        body.y = radius_px / ppm
    elif y_px + radius_px > screen_height_px:
        body.vy *= -1
        body.y = (screen_height_px - radius_px) / ppm

def circle_collision(body1, body2, restitution=1):
    dx = body2.x - body1.x
    dy = body2.y - body1.y
    dist = math.hypot(dx, dy)
    min_dist = body1.radius + body2.radius

    if dist < min_dist:
        # 정규 벡터
        nx = dx / dist
        ny = dy / dist

        # 상대 속도
        rvx = body2.vx - body1.vx
        rvy = body2.vy - body1.vy
        rel_vel = rvx * nx + rvy * ny

        if rel_vel > 0:
            return  # 이미 떨어지고 있음

        # 충돌 반응 계산 (탄성 충돌)
        impulse = -(1 + restitution) * rel_vel
        impulse /= 1 / body1.mass + 1 / body2.mass

        # 속도 반영
        ix = impulse * nx
        iy = impulse * ny
        body1.vx -= ix / body1.mass
        body1.vy -= iy / body1.mass
        body2.vx += ix / body2.mass
        body2.vy += iy / body2.mass

        # 침투 보정 (반쪽씩)
        overlap = min_dist - dist
        correction_ratio = 0.5
        body1.x -= nx * overlap * correction_ratio
        body1.y -= ny * overlap * correction_ratio
        body2.x += nx * overlap * correction_ratio
        body2.y += ny * overlap * correction_ratio
