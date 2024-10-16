def solve_circuit(voltage, resistances):
    # Calculate total resistance
    total_resistance = sum(resistances)
    
    # Calculate total current (Ohm's law: V = IR => I = V/R)
    total_current = voltage / total_resistance
    
    # Calculate voltage drop across each resistor (V_drop = I * R)
    voltage_drops = [total_current * r for r in resistances]
    
   
    currents = [total_current for _ in resistances]
    
    return currents, voltage_drops

# Example usage
voltage = float(input("Enter the voltage: "))  # Convert to float
resistances = list(map(float, input("Enter the resistances (space-separated): ").split()))

currents, voltage_drops = solve_circuit(voltage, resistances)

print("Currents:", currents)
print("Voltage Drops:", voltage_drops)
