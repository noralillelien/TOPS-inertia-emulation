import json
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
results = []
names = []
folder_path = Path('Results/SI/sensitivity')
for name in sorted(folder_path.iterdir()):
    with open(name,'r') as file:
        res = json.load(file)
        results.append(res)
        formatted_string = name.stem.replace('_', '=')

        names.append(formatted_string)

for res in results:
    for key, value in res.items():
        if key != 't' and key != 'VSC':
            # Iterate through the list of timesteps (assumed to be lists or arrays)
            for i, timestep in enumerate(value):  # Use enumerate to modify the list in-place
                for j, v in enumerate(res[key][i]):  # Iterate through each value in the timestep
                    if isinstance(v, str) and 'j' in v:  # Check if it's a string that represents a complex number
                        try:
                            res[key][i][j] = complex(v)  # Convert the string back to a complex number
                        except ValueError:
                            pass  # In case the string is not a valid complex number


# fig = plt.figure()
# i = 0
# for res in results:
#     bus7 = [row[8] for row in res['v']]
#     plt.plot(res['t'], np.abs(np.array(bus7)),label = names[i] + ' bus 7')
#     i+=1
# i = 0
# for res in results:
#     bus7 = [row[10] for row in res['v']]
#     plt.plot(res['t'], np.abs(np.array(bus7)),label = str(names[i]) + ' bus 9')
#     i+=1
# plt.xlabel('Time [s]')
# plt.ylabel('Bus voltage')
# plt.legend()
# # plt.show()
# plt.figure()
# for res in results:
#     plt.plot(res['t'], np.abs(np.array(res['gen_P'])),label = res['gen_name'][0])
# plt.legend()
# fig = plt.figure()
# # for res in results:
# plt.plot(res['t'], res['VSC'], label = ['HVDC','Wind'])

# plt.xlabel('Time [s]')
# plt.ylabel('MW')
# plt.legend()
# plt.figure()
# plt.plot(res['t'], res['HVDC_SI'],label = ['HVDC_SI','Wind_SI'])
# plt.xlabel('Time [s]')
# plt.ylabel('MW')
# plt.legend()
# plt.figure()
# ROCOF = np.gradient(50+50*np.mean((res['gen_speed']),axis=1),res['t'])
# plt.plot(res['t'],ROCOF)
# plt.plot(res['t'],res['VSC_rocof'])
# plt.figure()
# i = 0
# for res in results:
#     plt.plot(res['t'],50+50*np.mean((res['gen_speed']),axis = 1), label = names[i])
#     i+=1
# plt.xlabel('Time [s]')
# plt.ylabel('Frequency [Hz]')
# plt.grid()
# plt.legend()
# plt.figure()
# i = 0
# for res in results:
#     ROCOF = np.gradient(50+50*np.mean((res['gen_speed']),axis=1),res['t'])
#     plt.plot(res['t'],ROCOF, label = names[i])
#     i+=1
# plt.xlabel('Time [s]')
# plt.ylabel('ROCOF [Hz/s]')
# plt.grid()
# plt.legend()

fig = plt.figure()
# plt.plot(res['t'], np.abs(res['VSC']))
i = 0
for res in results:
    plt.plot(res['t'],np.abs(res['VSC']), label = names[i])
    i+=1
plt.xlabel('Time [s]')
plt.ylabel('MW')


plt.figure()
i = 0
for res in results:
    plt.plot(res['t'],50+50*np.mean((res['gen_speed']),axis = 1), label = names[i])
    i+=1
plt.xlabel('Time [s]')
plt.ylabel('Frequency [Hz]')
#plt.ylim(49,51)
plt.grid()
plt.legend()
plt.show()

plt.show()