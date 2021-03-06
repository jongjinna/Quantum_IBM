# The Atoms of Computation

from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

sim = Aer.get_backend('aer_simulator') 

# qc_output = QuantumCircuit(8)
# qc_output.measure_all()
# print(qc_output.draw(initial_state=True))

# sim = Aer.get_backend('aer_simulator') 
# result = sim.run(qc_output).result()
# counts = result.get_counts()
# plot_histogram(counts)
# plt.show()

# qc_encode = QuantumCircuit(8)
# qc_encode.x(7)
# print(qc_encode.draw())

# qc_encode.measure_all()
# print(qc_encode.draw())

# sim = Aer.get_backend('aer_simulator') 
# result = sim.run(qc_encode).result()
# counts = result.get_counts()
# plot_histogram(counts)
# plt.show()

# qc_encode = QuantumCircuit(8)
# qc_encode.x(1)
# qc_encode.x(5)

# print(qc_encode.draw())

# qc_cnot = QuantumCircuit(2)
# qc_cnot.cx(0,1)
# print(qc_cnot.draw())

# qc = QuantumCircuit(2,2)
# qc.x(0)
# qc.cx(0,1)
# qc.measure(0,0)
# qc.measure(1,1)
# print(qc.draw())

qc_ha = QuantumCircuit(4,2)
# encode inputs in qubits 0 and 1
qc_ha.x(0) # For a=0, remove this line. For a=1, leave it.
qc_ha.x(1) # For b=0, remove this line. For b=1, leave it.
qc_ha.barrier()
# use cnots to write the XOR of the inputs on qubit 2
qc_ha.cx(0,2)
qc_ha.cx(1,2)
qc_ha.barrier()
# extract outputs
qc_ha.measure(2,0) # extract XOR value
qc_ha.measure(3,1)

print(qc_ha.draw())

qobj = assemble(qc_ha)
counts = sim.run(qobj).result().get_counts()
print(counts)
# plot_histogram(counts)
# plt.show()