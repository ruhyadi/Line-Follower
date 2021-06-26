def get_speed(direction):
    baseSpeed = 120
    maxSpeed = 150
    direction = direction
    threshSpeed = (maxSpeed - baseSpeed)/120 * abs(direction)

    speedMotor = baseSpeed + (maxSpeed - baseSpeed)/120 * abs(direction)

    if speedMotor <= threshSpeed:
        speedMotor = maxSpeed
    else:
        speedMotor = speedMotor

    return str(speedMotor)