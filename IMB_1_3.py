from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram, plot_bloch_vector
from math import sqrt, pi
import matplotlib.pyplot as plt

# qc = QuantumCircuit(1) # Create a quantum circuit with one qubit

# qc = QuantumCircuit(1)  # Create a quantum circuit with one qubit
# initial_state = [0,1]   # Define initial_state as |1>
# qc.initialize(initial_state, 0) # Apply initialisation operation to the 0th qubit
# print(qc.draw())  # Let's view our circuit

sim = Aer.get_backend('aer_simulator')  # Tell Qiskit how to simulate our circuit

# qc = QuantumCircuit(1)  # Create a quantum circuit with one qubit
# initial_state = [0,1]   # Define initial_state as |1>
# qc.initialize(initial_state, 0) # Apply initialisation operation to the 0th qubit
# qc.save_statevector()   # Tell simulator to save statevector
# qobj = assemble(qc)     # Create a Qobj from the circuit for the simulator to run
# result = sim.run(qobj).result() # Do the simulation and return the result

# out_state = result.get_statevector()
# print(out_state) # Display the output state vector

# qc.measure_all()
# print(qc.draw())

# qobj = assemble(qc)
# result = sim.run(qobj).result()
# counts = result.get_counts()
# plot_histogram(counts)
# plt.show()

# initial_state = [1/sqrt(2), 1j/sqrt(2)]  # Define state |q_0>

# qc = QuantumCircuit(1) # Must redefine qc
# qc.initialize(initial_state, 0) # Initialize the 0th qubit in the state `initial_state`
# qc.save_statevector() # Save statevector
# qobj = assemble(qc)
# state = sim.run(qobj).result().get_statevector() # Execute the circuit
# print(state)           # Print the result

# qobj = assemble(qc)
# results = sim.run(qobj).result().get_counts()
# plot_histogram(results)
# plt.show()

vector = [1,1]
qc.initialize(vector, 0)

# Run the code in this cell to interact with the widget
from qiskit_textbook.widgets import state_vector_exercise
state_vector_exercise(target=1/3)

qc = QuantumCircuit(1) # We are redefining qc
initial_state = [0.+1.j/sqrt(2),1/sqrt(2)+0.j]
qc.initialize(initial_state, 0)
qc.draw()

qc.save_statevector()
result = sim.run(assemble(qc)).result()
state = result.get_statevector()
print("Qubit State = " + str(state))

qc = QuantumCircuit(1) # We are redefining qc
initial_state = [0.+1.j/sqrt(2),1/sqrt(2)+0.j]
qc.initialize(initial_state, 0)
qc.measure_all()
qc.save_statevector()
print(qc.draw())

qobj = assemble(qc)
state = sim.run(qobj).result().get_statevector()
print("State of Measured Qubit = " + str(state))

from qiskit_textbook.widgets import plot_bloch_vector_spherical
coords = [pi/2,0,1] # [Theta, Phi, Radius]
plot_bloch_vector_spherical(coords) # Bloch Vector with spherical coordinates

from qiskit_textbook.widgets import bloch_calc
bloch_calc()