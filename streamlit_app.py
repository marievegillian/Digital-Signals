import streamlit as st
import matplotlib.pyplot as plt

# Encoding functions as defined above...
def nrzl_encode(data):
    """Non-Return to Zero-Level (NRZ-L) encoding"""
    return [1 if bit == '1' else -1 for bit in data]

def nrzi_encode(data):
    """Non-Return to Zero Inverted (NRZ-I) encoding"""
    signal = []
    level = -1
    for bit in data:
        if bit == '1':
            level *= -1  # Toggle level on '1'
        signal.append(level)
    return signal

def bipolar_ami_encode(data):
    """Bipolar Alternate Mark Inversion (AMI) encoding"""
    signal = []
    last_non_zero = -1
    for bit in data:
        if bit == '1':
            last_non_zero *= -1  # Alternate between +1 and -1
            signal.append(last_non_zero)
        else:
            signal.append(0)  # Zero stays zero
    return signal

# Streamlit app layout
st.title("Digital Signal Encoder")

# User input for binary data
data = st.text_input("Enter binary data (e.g., 101010):", "")
encoding_type = st.selectbox("Choose Encoding Technique", 
                             ["NRZ-L", "NRZ-I", "Bipolar AMI"])

if st.button("Plot Signal"):
    if data:
        if encoding_type == "NRZ-L":
            signal = nrzl_encode(data)
        elif encoding_type == "NRZ-I":
            signal = nrzi_encode(data)
        elif encoding_type == "Bipolar AMI":
            signal = bipolar_ami_encode(data)
        
        # Plotting
        plt.figure(figsize=(10, 2))
        plt.step(range(len(signal)), signal, where='mid')
        plt.ylim(-2, 2)
        plt.title(f"{encoding_type} Encoding")
        plt.xlabel("Bit Position")
        plt.ylabel("Voltage Level")
        st.pyplot(plt)
    else:
        st.error("Please enter binary data.")
