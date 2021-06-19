def PID_control(cx, Kp, Ki, Kd, maxSpeed=150, baseSpeed=100, lastError=0):
    position = cx
    error = abs(120 - position)*-1

    P = error
    I = I + error
    D = error - lastError
    lastError = error
    motorSpeed = P*Kp + I*Ki + D*Kd
    motorSpeed = baseSpeed + motorSpeed

    if motorSpeed > maxSpeed:
        motorSpeed = maxSpeed
    if motorSpeed < 0:
        motorSpeed = 0

    return motorSpeed
    