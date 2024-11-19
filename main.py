# import sys
# sys.path.append("D:\\OneDrive\\Desktop\\DAA Project")
import sys
print("PYTHONPATH:", sys.path)
import streamlit as st
from algorithms.closest_pair import closest_pair
from algorithms.karatsuba import karatsuba
from utils.file_utils import load_points, load_numbers

st.title("Divide and Conquer Algorithms")

uploaded_file = st.file_uploader("Choose a file", type="txt")
if uploaded_file:
    option = st.selectbox("Select an Algorithm", ["Closest Pair of Points", "Integer Multiplication"])
    if st.button("Run Algorithm"):
        if option == "Closest Pair of Points":
            points = load_points(uploaded_file)
            result = closest_pair(points)
            st.write(f"The closest distance is: {result}")

        elif option == "Integer Multiplication":
            nums = load_numbers(uploaded_file)
            result = karatsuba(nums[0], nums[1])
            st.write(f"Result of Integer Multiplication: {result}")

