def resolve_collision(body1, body2):
    overlap_x = min(body1.x + body1.width, body2.x + body2.width) - max(body1.x, body2.x)
    overlap_y = min(body1.y + body1.height, body2.y + body2.height) - max(body1.y, body2.y)

    if overlap_x < overlap_y:
        if body1.x < body2.x:
            body1.x -= overlap_x
        else:
            body1.x += overlap_x
        body1.vx *= -1
    else:
        if body1.y < body2.y:
            body1.y -= overlap_y
        else:
            body1.y += overlap_y
        body1.vy *= -1
