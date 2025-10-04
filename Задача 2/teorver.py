from random import sample
import plotly.graph_objs as go
import numpy as np

def random_comb():
    group = ['Girl'] * 8 + ['Boy'] * 6
    return sample(group, 7)

N_values = np.array(range(10, 10001, 50))
P_A_values = []
for N in N_values:
    N_A = 0
    for _ in range(N):
        comb = random_comb()
        if comb.count('Girl') == 4:
            N_A += 1
    P_A_values.append(N_A / N)
print(round(P_A_values[-1], 4))
P = [0.4079] * len(N_values)

fig = go.Figure(layout=dict(width=600, height=300))
fig.update_layout(margin=dict(l=0, t=0, b=0))
fig.add_trace(go.Scatter(x=N_values, y=P_A_values, name='Чистота'))
fig.add_trace(go.Scatter(x=N_values, y=P, name='Вероятность', line_dash='dash'))
fig.update_xaxes(title_text='N')
fig.update_yaxes(title_text='P(A)')
fig.show()
