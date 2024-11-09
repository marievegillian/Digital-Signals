import streamlit as st
import matplotlib.pyplot as plt

def nrzl_encode(data):
    """Non-Return to Zero-Level (NRZ-L) encoding"""
    return [1 if bit == '1' else -1 for bit in data]

def nrzi_encode(data):
    """Non-Return to Zero Inverted (NRZ-I) encoding"""
    signal = []
    level = -1
    for bit in data:
        if bit == '1':
            level *= -1
        signal.append(level)
    return signal

def bipolar_ami_encode(data):
    """Bipolar Alternate Mark Inversion (AMI) encoding"""
    signal = []
    last_non_zero = -1
    for bit in data:
        if bit == '1':
            last_non_zero *= -1
            signal.append(last_non_zero)
        else:
            signal.append(0)
    return signal

def pseudoternary_encode(data):
    """Pseudoternary encoding"""
    signal = []
    last_non_zero = -1
    for bit in data:
        if bit == '0':
            last_non_zero *= -1
            signal.append(last_non_zero)
        else:
            signal.append(0)
    return signal

def manchester_encode(data):
    """Manchester encoding"""
    signal = []
    for bit in data:
        if bit == '1':
            signal.extend([1, -1])  # High-to-low transition
        else:
            signal.extend([-1, 1])  # Low-to-high transition
    return signal
    
def differential_manchester_encode(data, initial_state='high'):
    """Differential Manchester encoding with selectable initial state"""
    signal = []
    current_level = 1 if initial_state == 'high' else -1  # Start with high or low

    for bit in data:
        # Differential encoding: transition at start if bit is '0'
        if bit == '0':
            signal.append(current_level)
            current_level *= -1  # Toggle mid-bit
            signal.append(current_level)
        else:
            # Transition only mid-bit for '1'
            current_level *= -1
            signal.append(current_level)
            current_level *= -1
            signal.append(current_level)
    
    return signal

st.title("Digital Signal Encoder")

data = st.text_input("Enter binary data (e.g., 101010):", "")
encoding_type = st.selectbox("Choose Encoding Technique", 
                             ["NRZ-L", "NRZ-I", "Bipolar AMI","Pseudoternary","Manchester","Differential Manchester"])

if st.button("Plot Signal"):
    if data:
        if encoding_type == "NRZ-L":
            signal = nrzl_encode(data)
        elif encoding_type == "NRZ-I":
            signal = nrzi_encode(data)
        elif encoding_type == "Bipolar AMI":
            signal = bipolar_ami_encode(data)
        elif encoding_type == "Pseudoternary":
            signal = pseudoternary_encode(data)
        elif encoding_type == "Manchester":
            signal = manchester_encode(data)
        elif encoding_type == "Differential Manchester":
            signal = differential_manchester_encode(data)
            
        plt.figure(figsize=(10, 2))
        plt.step(range(len(signal)), signal, where='mid')
        plt.ylim(-2, 2)
        plt.title(f"{encoding_type} Encoding")
        plt.xlabel("Bit Position")
        plt.ylabel("Voltage Level")
        st.pyplot(plt)
    else:
        st.error("Please enter binary data.")
