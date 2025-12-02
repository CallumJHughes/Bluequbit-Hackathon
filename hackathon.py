import bluequbit
import qiskit.qasm2
from qiskit import QuantumCircuit, Aer, execute
from collections import Counter

# Get file name from user
file = input('Please write input .qasm file: ')

# Load circuit
qc = QuantumCircuit.from_qasm_file(file)

# Add measurement
qc.measure_all()

token = input('Please enter your Bluequbit token: ')

bq = bluequbit.init(token)

print('CPU Estimate:')
print(bq.estimate(qc, device='cpu'))
print('')

print('MPS CPU Estimation:')
print(bq.estimate(qc, device='mps.cpu'))
print('')

print('QPU Estimation:')
print(bq.estimate(qc, device='quantum'))
print('')

print('GPU Estimation:')
print(bq.estimate(qc, device='gpu'))
print('')

print('MPS GPU Estimation:')
print(bq.estimate(qc, device='mps.gpu'))
print('')

# Check Price is ok
userAnswer = input('Would you like to continue? [Y/N]: ')
if userAnswer == ('Y' or 'y'):
	processor = input('Please write what processor you would like to use (cpu, mps.cpu, quantum, gpu, or mps.gpu): ')
	# Simulate
	result = bq.run(qc, device=processor)
	counts = result.get_counts()

	# Find peak bitstring
	peak = max(counts, key=counts.get)
	print("Peak bitstring: ", peak)
else:
	pass
