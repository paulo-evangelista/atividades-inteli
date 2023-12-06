from perceptron import Perceptron
import numpy as np

AND_gate = Perceptron()
OR_gate = Perceptron()
NAND_gate = Perceptron()

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

AND_y = np.array([0, 0, 0, 1])
OR_y = np.array([0, 1, 1, 1])
NAND_y = np.array([1, 1, 1, 0])


print("-> training AND gate...")
AND_gate.train(X, AND_y)
print("-> AND gate predictions:")
for x in X:
    y_pred = AND_gate.predict(x)
    print(f"{x} -> {y_pred}")

print("-> training OR gate...")
OR_gate.train(X, OR_y)
print("-> OR gate predictions:")
for x in X:
    y_pred = OR_gate.predict(x)
    print(f"{x} -> {y_pred}")

print("-> training NAND gate...")
NAND_gate.train(X, NAND_y)
print("-> NAND gate predictions:")
for x in X:
    y_pred = NAND_gate.predict(x)
    print(f"{x} -> {y_pred}")