# %%
import pandas as pd
import matplotlib.pyplot as plt
from mplsoccer.pitch import Pitch
# %%
df = pd.read_csv('messibetis.csv')
# %%
df

# %%
df['x']= df['x']*1.2
df['y'] = df['y']*.8
df['endX']= df['endX']*1.2
df['endY']= df['endY']*.8
# %%
df
# %%
fig,ax = plt.subplots(figsize=[13.5,8])
fig.set_facecolor('#22312b')
ax.patch.set_facecolor('#22312b')

pitch = Pitch(pitch_type='statsbomb', orientation='vertical', pitch_color='#22312b', line_color='white', figsize='16, 11', constrained_layout=True, tight_layout=False)
pitch.draw(ax=ax)

plt.gca().invert_yaxis()

for x in range(len(df['x'])):
    if df['outcome'][x] == 'Successful':
        plt.plot((df['x'][x], df['endX'][x]),(df['y'][x], df['endY'][x]),color='green')
        plt.scatter(df['x'][x],df['y'][x], color='green')
        plt.scatter(df['endX'][x],df['endY'][x], color='green')
    if df['outcome'][x] == 'Unsuccessful':
        plt.plot((df['x'][x], df['endX'][x]),(df['y'][x], df['endY'][x]),color='red')
        plt.scatter(df['x'][x],df['y'][x], color='red')
        plt.scatter(df['endX'][x],df['endY'][x], color='red')

# %%
