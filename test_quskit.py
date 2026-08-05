from qiskit import QuantumCircuit
import numpy as np

qc = QuantumCircuit(2,2)
qc.h(0) # H gate on qubit 0 to put it into superposition
qc.cx(0, 1) # CNOT gate with qubit 0 as control
qc.cx(0,1) 
qc.h(0)
qc.measure([0, 1], [0, 1])

print(qc.draw(output='text')) # Draw the circuit

