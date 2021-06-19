def PID_control(cx, Kp, Ki, Kd, maxSpeed=150, baseSpeed=100, lastError=0, I=0):
    position = cx
    error = 120 - position

    P = error
    I = I + error
    D = error - lastError
    lastError = error
    motorSpeed = P*Kp + I*Ki + D*Kd
    motorSpeed = baseSpeed + motorSpeed

    if motorSpeed > maxSpeed:
        motorSpeed = maxSpeed
    if motorSpeed < baseSpeed:
        motorSpeed = baseSpeed

    return motorSpeed
    