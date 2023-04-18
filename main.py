from SonyVISCAController import SonyVISCAController
import time


if __name__ == "__main__":
    controller = SonyVISCAController('/dev/ttyUSB0')
    controller.power_on()
    time.sleep(1)
    controller.pan_tilt_up()
    time.sleep(2)
    controller.pan_tilt_stop()
    time.sleep(1)
    controller.pan_tilt_down()
    time.sleep(2)
    controller.pan_tilt_stop()
    time.sleep(1)
    controller.zoom_tele()
    time.sleep(2)
    controller.zoom_stop()
    time.sleep(1)
    controller.zoom_wide()
    time.sleep(2)
    controller.zoom_stop()
    time.sleep(1)
    controller.pan(180)  # pan right by 45 degrees
    time.sleep(1)
    controller.pan(-180)  # pan left by 45 degrees
    time.sleep(1)
    controller.tilt(30)  # tilt up by 30 degrees
    time.sleep(1)
    controller.tilt(-30)  # tilt down by 30 degrees
    time.sleep(1)
    controller.power_off()
    controller.close()
