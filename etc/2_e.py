import numpy as np
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import execute
from qiskit import BasicAer
from qiskit.tools.visualization import plot_state_city

q = QuantumRegister(2, 'q')
circuit = QuantumCircuit(q)
circuit.h(0)
circuit.cx(0, 1)

print(circuit.draw())

backend = BasicAer.get_backend('statevector_simulator')

job = execute(circuit, backend)

result = job.result()

outputstate = result.get_statevector(circuit, decimals=2)

print(outputstate)

plot_state_city(outputstate)

# Note : https://m.blog.naver.com/PostView.naver?blogId=simhc0714&logNo=221567009487&targetKeyword=&targetRecommendationCode=1
