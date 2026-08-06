# Quantum Circuit Simulator

A quantum circuit simulator built from scratch in Python. This project implements core quantum computing concepts including qubit state vectors, quantum gates, measurement, entanglement, and a depolarizing noise model.

## Overview

This simulator represents qubits as probability amplitude vectors and applies quantum gates through matrix multiplication using NumPy. It supports both single-qubit and two-qubit operations, with measurement collapsing the qubit state according to the Born rule.

## Features

### Qubit Representation

Qubits are represented as two-dimensional state vectors where each element is a probability amplitude. The square of each amplitude gives the probability of measuring that basis state, and the sum of squared amplitudes equals 1.

### Single-Qubit Gates

- **I (Identity):** Acts as a wire, leaving the qubit state unchanged.
- **X (Pauli-X):** Analogous to a classical NOT gate. Swaps the probability amplitudes of |0> and |1>.
- **Y (Pauli-Y):** Similar to a NOT gate with a phase shift, using a real-valued approximation of the Y matrix.
- **Z (Pauli-Z):** Changes the relative phase of the qubit without affecting measurement probabilities.
- **H (Hadamard):** Places a qubit into an equal superposition of |0> and |1>.

### Two-Qubit Gates

- **CNOT (Controlled-NOT):** Flips the target qubit if the control qubit is in state |1>. The two qubits become entangled and are represented as a combined four-dimensional state vector using the tensor product.

### Measurement

Measurement collapses the qubit state into either |0> or |1> based on the squared probability amplitudes. The simulator also accounts for measurement direction, resetting the state to equal superposition when the measurement basis changes.

### Depolarizing Noise Model

A simple noise model that randomly applies X, Y, or Z errors after each gate operation with a small probability (threshold of 0.001). This simulates real-world quantum hardware where gate operations are not perfectly precise.

## Dependencies

- Python 3
- NumPy

## Usage

```bash
pip install numpy
python quantum_circuit_sim.py
```

The `main()` function creates a qubit with random initial amplitudes and performs a series of measurements, printing the results.

## Reference

This project was built using concepts from:

Bernhardt, Chris. *Quantum Computing for Everyone*. MIT Press, 2019. ISBN: 978-0262539531.
