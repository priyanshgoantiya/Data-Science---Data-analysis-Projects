###Streamlitwebapp
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def plot_transformed_square(matrix):
    # Define original square points
    square = np.array([
        [-1, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]  # Closed loop
    ])
    
    # Apply transformation
    transformed_square = square @ matrix.T  # Transpose to match dimensions
    
    # Plot original and transformed squares
    fig, ax = plt.subplots()
    ax.plot(square[:, 0], square[:, 1], 'b-', label='Original Square')
    ax.plot(transformed_square[:, 0], transformed_square[:, 1], 'r-', label='Transformed Square')
    ax.fill(transformed_square[:, 0], transformed_square[:, 1], 'r', alpha=0.3)  # Fill color for transformed
    
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.grid(True)
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.legend()
    return fig

st.title("Matrix Transformation Visualizer")

matrix_input = st.text_input("Enter a 2x2 matrix (comma-separated values):", "0.70,0.70,-0.70,0.70")

if st.button("Apply transformation"):
    try:
        matrix_values = np.array([float(x) for x in matrix_input.split(',')]).reshape(2, 2)
        fig = plot_transformed_square(matrix_values)
        st.pyplot(fig)
    except:
        st.error("Invalid matrix format! Please enter 4 comma-separated values.")
