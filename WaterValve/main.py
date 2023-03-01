# https://replit.com/@kreier/WaterValveSimulation#main.py
from AnalogSensorSim import WaterFlowValve

myWaterValve = WaterFlowValve()
currentValue = 0.0


#Your task is to send the valve a correct signal to get the flow rate to be 4.5 L/s.

currentTime = 0.0
currentSignal = 0
setpoint = 4.5

while(currentTime < 10.0):
  valveFlowSensorValue = myWaterValve.getFlowRate()
  
  myWaterValve.setSignal(currentSignal)
  print(currentTime,",",valveFlowSensorValue)
  currentTime += 0.1
  
