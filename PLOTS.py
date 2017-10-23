import math#for math functions
import matplotlib.pyplot as plt# for the graph
import itertools#for the count function

try:
    legend_name = []
    start = input("How many trajectories?")
    for x in range(int(start)):
        legend_name.append("Ball {}".format(x + 1))#for the legend to have a name/title Exp:'Ball 1'
        init_velocity = input("Enter the initial velocity for trajectory {} (m/s) >> ".format(x + 1))
        angle = input("Enter the angle of projection for trajectory {} (degrees) >> ".format(x + 1))

        speed_x = float(init_velocity) * math.cos(math.radians(float(angle)))#for X's speed
        speed_y = float(init_velocity) * math.sin(math.radians(float(angle)))#for Y's Speed

        s_size = list()#list for X's coordinate
        s_height = list()#list for Y's coordinate

        for z in itertools.count():#for unlimited counting
            sx = speed_x * (z / 1000)
            sy = speed_y * (z / 1000) - 0.5 * 10 * (z / 1000) ** 2
            if sy >= 0:
                s_size.append(sx)
                s_height.append(sy)
            else:
                break

        plt.scatter(s_size, s_height, s =10)#to print the coordinates

    #Titles&Labels for graph
    plt.title("Projectile motion of a ball")
    plt.xlabel("X-Coordinate")
    plt.ylabel("Y-Coordinate")
    plt.legend(legend_name)
    plt.show()
except:
    print("[ERROR] string inputted")
