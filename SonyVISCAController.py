import serial
import time


class SonyVISCAController:
    def __init__(self, port, baudrate=9600, timeout=0.1):
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        self.address = 1

    def send_command(self, command):
        if not isinstance(command, bytes):
            command = bytes.fromhex(command)
        self.ser.write(command)
        response = self.ser.read(1024)
        return response

    def close(self):
        self.ser.close()

    def power_on(self):
        return self.send_command(f'81 01 04 00 02 FF')

    def power_off(self):
        return self.send_command(f'81 01 04 00 03 FF')

    def pan_tilt_up(self, speed=0x18):
        return self.send_command(f'81 01 06 01 {speed:02X} {speed:02X} 03 01 FF')

    def pan_tilt_down(self, speed=0x18):
        return self.send_command(f'81 01 06 01 {speed:02X} {speed:02X} 03 02 FF')

    def pan_tilt_left(self, speed=0x18):
        return self.send_command(f'81 01 06 01 {speed:02X} {speed:02X} 01 03 FF')

    def pan_tilt_right(self, speed=0x18):
        return self.send_command(f'81 01 06 01 {speed:02X} {speed:02X} 02 03 FF')

    def pan_tilt_stop(self):
        return self.send_command(f'81 01 06 01 00 00 03 03 FF')

    def zoom_tele(self, speed=0x02):
        return self.send_command(f'81 01 04 07 2{speed:X} FF')

    def zoom_wide(self, speed=0x02):
        return self.send_command(f'81 01 04 07 3{speed:X} FF')

    def zoom_stop(self):
        return self.send_command(f'81 01 04 07 00 FF')
    
    def _move_duration(self, angle, rate):
        return abs(angle) / rate

    def pan(self, angle, speed=0x18):
        rate = 90  # degrees per second, adjust according to your camera's specifications
        duration = self._move_duration(angle, rate)
        if angle > 0:
            self.pan_tilt_right(speed)
        else:
            self.pan_tilt_left(speed)
        time.sleep(duration)
        self.pan_tilt_stop()

    def tilt(self, angle, speed=0x18):
        rate = 90  # degrees per second, adjust according to your camera's specifications
        duration = self._move_duration(angle, rate)
        if angle > 0:
            self.pan_tilt_up(speed)
        else:
            self.pan_tilt_down(speed)
        time.sleep(duration)
        self.pan_tilt_stop()
