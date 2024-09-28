# Quantum Random Number Generator (QRNG)
## Overview
This project implements a Quantum Random Number Generator (QRNG) using Qiskit. It leverages the principles of quantum mechanics to generate true random numbers. The QRNG uses quantum superposition and measurement to generate random bits, which are then combined to form a random integer within a specified range.

## Features
- Generates random bits using quantum circuits.
- Maps the generated bits to a random integer within a user-defined range.
- Visualizes the random bits and the generated random number using Matplotlib.

## Requirements
- Python 3.11
- Qiskit 1.2.2
- Matplotlib 3.8.1

## Installation
To set up the project, follow these steps:
1. Clone the repository:
```bash
git clone https://github.com/yourusername/quantum-rng.git
cd quantum-rng
```
2. Install the required packages:
```bash
pip install qiskit matplotlib
```

## Usage
1. Run the script:
```bash
python quantum_random_number_generator.py 
```
2. Input the desired minimum and maximum range when prompted:
```bash
Enter the minimum range: 0
Enter the maximum range: 255 
```
3. The program will display the generated random bits and the corresponding random number, as well as a plot visualizing the bits and the random number.

## Code Structure
- **quantum_random_number_generator.py**: The main script that generates random numbers and visualizes the results.

## Example Output
When the script is run, you will see an output similar to:
```bash
Random bits generated: ['1', '0', '1', '1', '0']
Random number generated: 22 
```
And a plot displaying the random bits and the random number.
## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.
