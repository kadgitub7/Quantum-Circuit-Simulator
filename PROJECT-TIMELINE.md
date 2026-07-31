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
