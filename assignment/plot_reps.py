import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('rep_data.csv')


time = df['time']      
angle = df['angle']     
reps = df['reps']       


plt.figure(figsize=(10, 5))
plt.plot(time, angle, label='Elbow Angle', color='blue')


completed_reps = df[df['reps'].diff() > 0]

for t in completed_reps['time']:
    plt.axvline(x=t, color='red', linestyle='--', alpha=0.7, label='Rep Completed')


plt.xlabel('Time (s)')
plt.ylabel('Angle (degrees)')
plt.title('Bicep Curl Repetition Counter')
plt.grid(True)


handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())


plt.savefig('rep_plot.png')
print("Graph saved as rep_plot.png!")


plt.show()