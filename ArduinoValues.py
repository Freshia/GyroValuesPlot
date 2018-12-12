import serial  # import Serial Library
import numpy  # Import numpy
import matplotlib.pyplot as plt  # import matplotlib library
from drawnow import *

X = []
Y = []
Z = []
arduinoData = serial.Serial('com8', 115200)  # Creating our serial object named arduinoData
plt.ion()  # Tell matplotlib you want interactive mode to plot live data
cnt = 0


def makeFig():  # Create a function that makes our desired plot
    plt.ylim(-5, 5)  # Set y min and max values
    plt.title('My Live Streaming Sensor Data')  # Plot the title
    plt.grid(True)  # Turn the grid on
    plt.ylabel('Y')  # Set ylabels
    plt.plot(X, 'ro-', label='X VALUES',c='BLUE')  # plot the xvalues
    plt.plot(Z, 'ro-', label='Z VALUES', c='YELLOW')#plot the Y values
    plt.legend(loc='upper left')  # plot the legend
    plt.plot(Y, 'ro-', label='Y VALUES',c='RED')  # plot the temperature



while True:  # While loop that loops forever
    while (arduinoData.inWaiting() == 0):  # Wait here until there is data
        pass  # do nothing
    arduinoString = arduinoData.readline() # read the line of text from the serial port
    dataArray = arduinoString.decode("utf-8").split(',')  # Split it into an array called dataArray
    P = float(dataArray[0])  # Convert second element to floating number and put in P
    S=float(dataArray[1])
    Q=float(dataArray[2])
    X.append(P)  # Build our tempF array by appending temp readings
    Z.append(Q)
    Y.append(S)  # Building our pressure array by appending P readings
    drawnow(makeFig)  # Call drawnow to update our live graph
    plt.pause(.000001)  # Pause Briefly. Important to keep drawnow from crashing
    cnt = cnt + 1
    if (cnt > 50):  # If you have 50 or more points, delete the first one from the array
        X.pop(0)  # This allows us to just see the last 50 data points
        Y.pop(0)
        Z.pop(0)

