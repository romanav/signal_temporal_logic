import pandas as pd
import src.robustness as rb
import matplotlib.pyplot as plt

frame = pd.read_csv('Time_Series_Metrics2.csv')

ego_speed = frame['Host 1 Ego Proj x Speed [m/s]']
actor_speed = frame['Player 2 Self Proj x Speed [m/s]']
distance_to_actor = frame['Host 1 X coordinate distance to closest Player in front bbox [m]']
speed_limit = [10 for i in ego_speed]

distance_limit = distance_to_actor -.1


until = list(rb.until(ego_speed, [0, 10], distance_limit))
plt.plot(range(len(until)), until, 0)
plt.show()
