# I2C with Rasberry Pi

# Demonstrate using I2C by interfacing with a light intensity sensor

import smbus
import time

ONE_TIME_HIGH_RES_MODE_1 = 0x20
lightSensorAddr = 0x23

# Setup I2C interface
currentSmbus = smbus.SMBus(1)

def readLightLevel():
  rawData = currentSmbus.read_i2c_block_data(lightSensorAddr, ONE_TIME_HIGH_RES_MODE_1)

  # Convert 2 bytes of raw data to number
  data = (rawData[1] + (256 * rawData[0])) / 1.2

  return int(data)

while True:
  lightLevel = readLightLevel()

  print("Light Level: ", lightLevel)
  if lightLevel >= 400:
      print("too bright")
  elif lightLevel >= 300 and lightLevel < 400:
      print("bright")
  elif lightLevel >= 200 and lightLevel < 300:
      print("medium")
  elif lightLevel >= 100 and lightLevel < 200:
      print("dark")
  elif lightLevel < 100:
      print("too dark")

  time.sleep(1)
