# # The Atoms of Computation

# from qiskit import QuantumCircuit, assemble, Aer
# from qiskit.visualization import plot_histogram
# import matplotlib.pyplot as plt

# sim = Aer.get_backend('aer_simulator') 

# # qc_ha = QuantumCircuit(4,4)
# qc_ha = QuantumCircuit(1,1)
# qc_ha.x(0)
# qc_ha.u(0)
# qc_ha.barrier()
# qc_ha.measure(0,0)

# # qc_ha.x(0)
# # qc_ha.x(1) 
# # qc_ha.y(1)
# # qc_ha.h(0)
# # qc_ha.barrier()

# # qc_ha.cx(0,2)
# # qc_ha.cx(1,2)
# # qc_ha.barrier()

# # qc_ha.measure(0,0)
# # qc_ha.measure(1,1)
# # qc_ha.measure(2,2)
# # qc_ha.measure(3,3)

# # print(qc_ha.draw())

# qobj = assemble(qc_ha)
# counts = sim.run(qobj).result().get_counts()
# print(counts)

import pandas as pd
import numpy as np
import pandas_datareader.data as web

FB = web.YahooOptions('FB')
for exp in FB.expiry_dates:
  print(exp.isoformat())
