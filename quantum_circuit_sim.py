import random

class Qubit:
    def __init__(self, ID, prob_amplitudes):
        self.Id = ID
        self.prob_amplitudes = prob_amplitudes

def create_qubit(ID):
    # This function creates a vector representing a qubit
    # The vector is two dimensional and the first number represents the probability amplitude of state 0, seconds number is probability amplitude of state 1
    # The sum of the squares of the amplitudes must equal 1

    amplitude_0 = random.random()
    amplitude_1 = (1-(amplitude_0**2))**0.5
    Id = ID
    return Qubit(Id, [amplitude_0, amplitude_1])

def create_entangled_qubits(ID1, ID2, prob_amplitudes):
    # This function creates two entangled qubits
    # The qubits are represented as a single state vector
    # The state vector is four dimensional and the first number represents the probability amplitude of state 00, second number is probability amplitude of state 01, third number is probability amplitude of state 10, fourth number is probability amplitude of state 11
    # The sum of the squares of the amplitudes must equal 1

    """
    Figure out how to represent entangled qubits properly
    """

    return


def measure_qubit(qubit):
    # This function meaures a qubit and returns the result of the measurement (0 or 1)
    '''
    To do items:
    We need to make sure that the measurements are done according to the three rules of quantum mechanics
    1) repeating the same experiment over an over will lead to the same results

    2) Randomness occurs in a sequence of questions 

    3) if you switch the experiment, view one direction sswitch direction and switch back, the third time where you were viewing the same thing might not be the same
    '''

    probability_0 = qubit.prob_amplitudes[0] **2
    probability_1 = qubit.prob_amplitudes[1] **2

    if random.random() < probability_0:
        return 0
    else:
        return 1

''' Gates '''

def I(qubit):
    # Equivalent to a wire in a normal circuit
    qubit.prob_amplitudes = qubit.prob_amplitudes @ [[1, 0], [0, 1]]

def Z(qubit):
    # changes relative phase of the qubit but does not affect basis or probabilities, similar to a wire
    qubit.prob_amplitudes = qubit.prob_amplitudes @ [[1,0], [0,-1]]

def X(qubit):
    # similar to a NOT gate
    qubit.prob_amplitudes = qubit.prob_amplitudes @ [[0,1], [1,0]]

def Y(qubit):
    # similar to a NOT gate but with a phase shift
    qubit.prob_amplitudes = qubit.prob_amplitudes @ [[0,-1], [1,0]]

def H(qubit):
    # puts the qubit into a superposition state
    qubit.prob_amplitudes = qubit.prob_amplitudes @ [[1/(2**0.5),1/(2**0.5)], [1/(2**0.5),-1/(2**0.5)]]

def CNOT(control_qubit, target_qubit):
    # flips the target qubit if the control qubit is 1
    # They become entangled and therefore cannot be represented seperately anymore, so we need to represent them as a single state vector
    CNOT_matrix = [[1,0,0,0], [0,1,0,0], [0,0,0,1], [0,0,1,0]]
    state_vector = [control_qubit.prob_amplitudes[0] * target_qubit.prob_amplitudes[0],
                    control_qubit.prob_amplitudes[0] * target_qubit.prob_amplitudes[1],
                    control_qubit.prob_amplitudes[1] * target_qubit.prob_amplitudes[0],
                    control_qubit.prob_amplitudes[1] * target_qubit.prob_amplitudes[1]]
    new_state_vector = CNOT_matrix @ state_vector


def main():
    GLOBAL_ID_COUNT = 0
    qubit = create_qubit(GLOBAL_ID_COUNT)
    print(qubit.prob_amplitudes)
    result = measure_qubit(qubit)
    print(f"Measurement result: {result}")
    result = measure_qubit(qubit)
    print(f"Measurement result: {result}")
    result = measure_qubit(qubit)
    print(f"Measurement result: {result}")
    GLOBAL_ID_COUNT += 1

if __name__ == "__main__":
    main()