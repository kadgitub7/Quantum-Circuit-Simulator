# PROJECT TIMELINE & OBJECTIVES

**Short Disclaimer**
This .md file is for people that want to understand what process as well as stuggles I went through to complete this project. Through this approach I will learn a lot and hit many roadblocks, which I hope to overcome. By following this file, you can see what my objectives, by path to implementation, and learning is.

## 1. Learning phase
Reading through Quantum Computing for Everyone by Chris Bernhardt to learn the concept necessary for this project

Chapter 1.
Quantum computing is similar but very different from normal computing. The basic unit of data in computing is the bit, it acts as a switch 0 or 1. In quantum computing the basic unit is a qubit which can be 0, 1 or a uperposition of both. It is computed based on the spin of an electoron or the polarization of a photon. The value of a qubit is difficult to determine and based on observations there are three things to note:
1) repeating the same experiment over an over will lead to the same results

2) Randomness occurs in a sequence of questions 

3) if you switch the experiment, view one direction sswitch direction and switch back, the third time where you were viewing the same thing might not be the same

Quantom computing has real random nature compared to the deterministic qseudorandomness in classical computers. Even a coin toss is not actually random, since it follows some phyical properties if you managed every single parameter like where you hit the coin, how much force you apply, how high it goes, where it lands, etc you will get the same results. This is only percieved as random because even a small change in these values can lead to large change in outcome. In Quantum there is actual randomness and therefore it can be used in some cases classical computers fail at.


Chapter 2.
Quantum Mechanics relies heavily on linear algebra. All of the spin and subsequence gates and logic for circuits are all build from linear algebra concepts.

Complex number include i, real numbers are what we are used to. For this textbook we only discuss real numbers for quantum computing also generally includes also imaginary numbers.

Vectors are a way to represent direction and magnitude. They can be represented for 2 or 3d visualization as an arrow. They are simply a set of values representing magnitudes in each dimension.

The length of a vector is similar to doing pythagorean theorum. You do the square root of the sum of all squared values in the vector.

Scalar multiplication of a vector involves multiplying each value by the scalar.

Vector addition requires the two vectors be the same exact dimensions. If they are the resulting sum is a vector of the same dimension but has each entry as the sum of the entries in the two added vectors in those specific positions.

Orthogonal vectors are vectors that are perpendicular to each other. This is the case when a^2 + b^2 = (a+b)^2 from pythagorean theorum but also works for higher order matrices.

A bra is (<a|) and a ket is |b>. These are just notations and a bra is a row or horizontal and a ket is a column or vertical. The length of a vector can also be calculated by multiplying it with its transpose and square rooting.

Unit vectors are very important and they have a lenght of 1.

A basis is when the set of vectors are linearly independent or orthogonal to each other.

Transpose of a matrix is flipping its rows with columns and columsn with rows. A * A^T is equal to the identify matrix.

There are three operations to be of note and will be used extensively:
1) To check if something is an orthonormal basis:
Multiply A by its transpose and if it is the identity matrix then it is else it is not
2) To find the combination of values (constants) that you need to multiply with a vector to get a particular value, just multiply that value by the transpose of the vector.
3) to find the length of a vector given byt he sum of constants and vector, get the sum of the squares of the constants.

Chapter 3.

Combining these previous two chapters to illustrate spin and qubits.

Probability is how likely something is to happen. It is put into contect and comes about based ona  finite number of outcomes each with an associated probability which stems from out of a given number of tries how often a particular outcome arrives. With a fair coin this is usually 0.5 for each side. The probabilities are between 0 and 1 and all sum to 1.

FOr a qubit if you make the same measurement again and again the same results arrives. Therefore if you make a measurement in the vertical direction and it is north, p_n = 1, and p_s = 0 for the next measurement in that same direction. Now if you make the measurement in the horizontal direction that is completely random and therefore p_n = 0.5, and p_s = 0.5.

Spin has two values and therefore the dimention of vectors i 2d. There are associated probability amplitudes for each direction and their square represents the probability when the electron is measured we will get that spin. Therefore c_1 ^ 2 + c_2 ^2 = 1. Once a measurement has been made the spin is set for concequent sam emeasurements. Therefore the probability anmplitudes get set to 1 and 0 depending on which one was observed first. Once this is done if we make a measurement in the opposite direction we don't know the probability amplitudes but the vectors are x = [1/root(2), -1/root(2)], and y = [1/root(2), 1/root(2)]. To solve the amplitudes we can set the equation as:
v = c_1 * x + c_2 * y
We can construct A = x|y = [[1/root(2), -1/root(2)], [1/root(2), 1/root(2)]]. If we take the transpose then we can multiply this my V and that will give us the values of x and y: [1/root(2), 1/root(2)]. If we square both these values they both are 0.5 which means there is an actual random change of each one. Similarly if you do this again for the first measurement now that this amplitudes are set you will find that is also random now.

Now since the probability amplitudes are squared to get the probabilities, a negative value is indistinguishable from a positive value. We can also envision thisi by understanding that the basis vectors can be given as [[1,0], [0,1]]. We can then represent rotations by [[cos(a), -sin(a)], [sin(a), cos(a)]]. Using this convention we can calculate the probability of measurement in N and S direction based on any degree change.

A qubit is any unit ket in R^2. 

Chapter 4.
Entanglement
The Tesor product is a way to join two vector spaces together to make a bigger space and therefore can engtangle the spaces. Therefore you can get instances where observing one qubit can change the value of another qubit.

This is mathematically modelled by the FOIL method and is represented by an XOR gate symbol. Since it is represented as:
[c_0(|a_0>) + c_1(|a_1>)] * [d_0(|b_0>) + d_1(|b_1>)] = 
c_0 * d_0 (|a_0> |b_0>) + c_0 * d_1 (|a_0> |b_1>) + c_1 * d_0 (|a_1> |b_0>) + c_1 * d_1 (|a_1> |b_1>).

We must be careful to note that the order of these values matters since this is vector multiplication and therefore if the order is switched a different results may occur. These final values a_0 *b_0, a_0 * b_1, a_1 * b_0, a_1 * b_1 are all orthonormal basis of the new vector space. They are all orthogonal to each other and unit. Each of the values in front of the combination of orthonormal basis vectors are the respective probability amplitudes for those states. Squaring them gives the probability. For example c_0 * d_0 is a probability amplitude and squaring it gives the probability of that given state. 

We can then convert the values of c_0 * d_0 and subsequent values as r,s,t,u where r^2 + s^2 + t^2 + u^2 = 1 and ru = st. This is true if the system is untangled(the values can be serperated and are therfore independent of each other). If ru /= st then the system is entangled as you are therfore not able to seperate the two states and get independent values for A and B.

When unentangled the tensor product is fully spereable and this means measurement on one qubit has no effect on another. If they are not seperable and must be mized together, then measurement on one qubit can affect the other. 

Chapter 5.
This chapter is a discussion on the debate between quantum theory and classical model of determinism. It ddebates and a test from Bell shows which one is accurate. Through this debate it is widely recognized that the classical model is incorrect.

Chapter 6.