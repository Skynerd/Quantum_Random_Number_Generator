from qiskit import QuantumCircuit
from qiskit_aer import Aer
import matplotlib.pyplot as plt
import math

### Ask the user for input
min_range = int(input("Enter the minimum range: "))
max_range = int(input("Enter the maximum range: "))
 
### Functions 
#region: functions  
def generate_random_bits(n):
    random_bits = []
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    simulator = Aer.get_backend('qasm_simulator')
    for _ in range(n):
        result = simulator.run(qc, shots=1).result()
        counts = result.get_counts()
        random_bits.append(list(counts.keys())[0])
    return random_bits

def random_number(bits):
    return int(''.join(bits), 2)

def number_of_bits_required():
    return math.ceil(math.log(max_range - min_range + 1,2))

def random_number_between(min_val,max_val): 
    random_num = max_val + 1
    while random_num > max_val:
        # Generate random bits and map to an integer between 0 and max - min
        random_bits = generate_random_bits(number_of_bits_required())
        # map the value to integer between max and min
        random_num = random_number(random_bits) + min_val
    return random_num, random_bits 
#endregion

# Generate random number and bits
random_num, random_bits = random_number_between(min_range,max_range)
print("Random bits generated:", random_bits) 
print("Random number generated:", random_num)

 
### Plotting the results

# Convert random bits to numeric values for plotting
bit_values = [int(bit) for bit in random_bits]

# Create a figure with two subplots (one for the number and one for the bar plot)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), gridspec_kw={'height_ratios': [1, 2]})

# Text annotation for the random number at the top
ax1.text(0.5, 0.5, f'Random Number: {random_num}', fontsize=20, ha='center', va='center')
ax1.axis('off')  # Hide axes for the random number display

# Bar plot for random bits at the bottom
ax2.bar(range(len(random_bits)), bit_values, tick_label=[f'Bit {i}' for i in range(len(random_bits))])
ax2.set_xlabel('Bit Position')
ax2.set_ylabel('Bit Value (0 or 1)')
ax2.set_title('Random Bits')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()

