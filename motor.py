class Motor:
    def __init__(self, channel, pwm):
        self.channel = channel
        self.pwm = pwm
        self.pwmValue = 0

    def arm(self):
        print('Arming motor on channel: '+str(self.channel))
        self.pwmValue = 260
        self.pwm.set_pwm(self.channel,0,260)

    def setSpeed(self, pwmValue):
        self.pwmValue = pwmValue
        self.pwm.set_pwm(self.channel,0,pwmValue)

    def stop(self):
        print('Stopping motor on channel: '+str(self.channel))
        self.speed = 260
        self.pwm.set_pwm(self.channel,0,260)
