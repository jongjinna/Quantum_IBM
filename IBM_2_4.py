from qiskit import QuantumCircuit
from qiskit.circuit import Gate
from math import pi
qc = QuantumCircuit(2)
c = 0
t = 1

# a controlled-Z
qc.cz(c,t)
print(qc.draw())

qc = QuantumCircuit(2)
# also a controlled-Z . HXH -> Z
qc.h(t)
qc.cx(c,t)
qc.h(t)
print(qc.draw())

qc = QuantumCircuit(2)
# a controlled-Y
qc.sdg(t)
qc.cx(c,t)
qc.s(t)
print(qc.draw())

qc = QuantumCircuit(2)
# a controlled-H
qc.ry(pi/4,t)
qc.cx(c,t)
qc.ry(-pi/4,t)
print(qc.draw())

# 2. Swapping Qubits
a = 0
b = 1

qc = QuantumCircuit(2)
# swaps states of qubits a and b
qc.swap(a,b)
print(qc.draw())

qc = QuantumCircuit(2)
# swap a 1 from a to b
qc.cx(a,b) # copies 1 from a to b
qc.cx(b,a) # uses the 1 on b to rotate the state of a to 0
print(qc.draw())

# swap a q from b to a
qc.cx(b,a) # copies 1 from b to a
qc.cx(a,b) # uses the 1 on a to rotate the state of b to 0
print(qc.draw())

qc = QuantumCircuit(2)
qc.cx(b,a)
qc.cx(a,b)
qc.cx(b,a)
print(qc.draw())

qc = QuantumCircuit(2)
# swaps states of qubits a and b
qc.cx(b,a)
qc.cx(a,b)
qc.cx(b,a)
print(qc.draw())

qc = QuantumCircuit(2)
# swaps states of qubits a and b
qc.cx(a,b)
qc.cx(b,a)
qc.cx(a,b)
print(qc.draw())

# 3. Controlled Rotations
