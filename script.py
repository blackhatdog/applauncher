from machine import Pin
from time import sleep
import machine

# Create a UART object
uart = machine.UART(0, baudrate=115200)


led = Pin(0, Pin.OUT)    # 22 number in is Output
push_button1 = Pin(2, Pin.IN)  # 23 number pin is input
push_button2 = Pin(0, Pin.IN)

while True:
  logic_state1 = push_button1.value()
  logic_state2 = push_button2.value()
  
  if logic_state1 == False:     # if pressed the push_button
      led.value(0)
      uart.write("first")
      sleep(1)# led will turn OFF# led will turn ON
  if logic_state2 == False:     # if pressed the push_button
      led.value(1)
      uart.write("second")
      sleep(1)# led will turn OFF# led will turn ON
  
  else:
      # if push_button not pressed
      led.value(1)
      