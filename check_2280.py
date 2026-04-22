#!/usr/bin/env python3

# Check the generated 2280.mv file

# Read the file
with open("/workspace/problem_008/code/2280.mv", "r") as f:
    lines = f.readlines()

# Parse initialization lines
mem = {}
for line in lines:
    line = line.strip()
    if line.startswith("[") and "]<" in line:
        # Parse [addr]<value
        parts = line.split("<")
        addr_str = parts[0][1:]  # Remove leading '['
        if addr_str.endswith(']'):
            addr_str = addr_str[:-1]
        addr = int(addr_str)
        value = int(parts[1])
        mem[addr] = value

# Check for input '9' (ASCII 57)
A = 57
addr_hundreds = 1000 + A
addr_tens = 2000 + A
addr_ones = 3000 + A

print(f"Input '9' (ASCII {A})")
print(f"Hundreds address {addr_hundreds}: value {mem.get(addr_hundreds, 'NOT FOUND')} (char: {chr(mem.get(addr_hundreds, 0)) if mem.get(addr_hundreds, 0) >= 32 else 'null'})")
print(f"Tens address {addr_tens}: value {mem.get(addr_tens, 'NOT FOUND')} (char: {chr(mem.get(addr_tens, 0))})")
print(f"Ones address {addr_ones}: value {mem.get(addr_ones, 'NOT FOUND')} (char: {chr(mem.get(addr_ones, 0))})")

# Also check a few other values
print("\nChecking some other values:")
for test_val in [48, 49, 65, 97, 255]:
    if test_val <= 255:
        h = mem.get(1000 + test_val, 0)
        t = mem.get(2000 + test_val, 0)
        o = mem.get(3000 + test_val, 0)
        print(f"ASCII {test_val}: hundreds={h}({chr(h) if h else 'null'}), tens={t}({chr(t) if t else 'null'}), ones={o}({chr(o)})")