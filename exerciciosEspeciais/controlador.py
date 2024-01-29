import matplotlib.pyplot as plt
import numpy as np
import control as ctrl

# Parâmetros do sistema
Kv = 20
n1 = 1
n2 = 2

# Adiciona um zero no numerador para evitar o erro de divisão por zero
sys = ctrl.TransferFunction([Kv, 0], [1, n1, n2, 0])

# Especificações de projeto
MF_spec = 50  # Margem de fase desejada
MG_spec = 10  # Margem de ganho desejada

# Projeto do compensador por avanço de fase
compensator = ctrl.phase_crossover_frequencies(sys)[0]  # Frequência de crossover de fase
alpha = (1 + np.sin(np.radians(MF_spec))) / (1 - np.sin(np.radians(MF_spec)))

# Zero do compensador por avanço de fase
T1 = 1 / (alpha * compensator)

# Compensador por avanço de fase
compensator_tf = ctrl.TransferFunction([T1, 1], [alpha * T1, 1])

# Sistema compensado
sys_compensated = ctrl.series(compensator_tf, sys)

# Plotagem do diagrama de Bode
plt.figure(figsize=(10, 6))
ctrl.bode_plot([sys, sys_compensated], Hz=True, dB=True, omega_limits=(0.01, 100))
plt.title('Diagrama de Bode - Sistema Original e Compensado')
plt.legend(['Sistema Original', 'Sistema Compensado'])
plt.grid(True)
plt.show()
