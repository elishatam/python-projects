import subprocess
import time


MAX_SAMPLES = 1000
samples = []

while True:
    charge_count = subprocess.check_output(["adb", "shell", "cat /sys/class/power_supply/battery/charge_counter"])
    try:
        charge_count = int(charge_count)
    except ValueError:
        continue

    while len(samples) >= MAX_SAMPLES:
        del samples[0]

    newest = (charge_count, time.time())
    samples.append(newest)

    if len(samples) > 2:

        oldest = samples[0]

        watts = -.01 * (newest[0] - oldest[0]) / (newest[1] - oldest[1])
        print("%d samples, averaging %.2f watts" % (len(samples), watts))
