#TempConvert.py
#Name: Jessica Pusher
#Date: 1/9/25
#Assignment: TempConvert.py


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = input("Give me a Farenheit temperature to convert to Celcius:")
  tempF = float(tempF)
  
  tempC = (tempF-32) * 5/9
  tempC = round(tempC, 2)

  print(tempF, "degrees fahrenheit is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
