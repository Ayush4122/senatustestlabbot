import streamlit as st
from fpdf import FPDF

# Streamlit App Title
st.title("Test Request Form Generator")

# Form Fields
st.subheader("Form Details")

# General Information
st.write("### General Information")
job_id = st.text_input("Job ID No.")
date = st.date_input("Date")
customer_name = st.text_input("Name and Address of Customer")
submitted_by = st.text_input("Name of Submitted")
contractor_name = st.text_input("Name of Contractor")
site_address = st.text_area("Site Address / Project Name")

# Testing Requirements
st.write("### Testing Requirements")
soil_rock = st.text_input("Soil/Rock Quantity")
design_mix = st.text_input("Design Mix")
aggregate = st.text_input("Aggregate/Sand/M-Sand Quantity")
cement = st.text_input("Cement (OPC/PPC/Fly Ash)")
brick = st.text_input("Brick/Fly Ash Bricks")
cube = st.text_input("Cube/Core/ACC Block/Paver Block")
water = st.text_input("Water")
ndt_upv = st.text_input("NDT/UPV")
bitumen = st.text_input("Bitumen Division/Wooden")

# Review Section
st.write("### Review of Test Request (By Laboratory)")
test_requirements = st.text_input("Requirements of test method defined and understood")
capability = st.text_input("Capability and Resources available")
sample_condition = st.radio("Condition of Sample Received", ["Sealed", "Open"])
discussion = st.text_input("Discussion with Customer, if any")
statement_conformity = st.radio("Requirement of Statement of Conformity", ["Yes", "No"])

# Placeholder for signatures
st.write("### Signatures")
customer_signature = st.text_input("Customer's Representative Signature (Enter Name)")
technical_manager_signature = st.text_input("Technical Manager Signature (Enter Name)")

# Generate PDF
if st.button("Generate PDF"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Header
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, txt="Test Request Form", ln=True, align="C")
    pdf.set_font("Arial", size=12)

    # General Information
    pdf.cell(200, 10, txt=f"Job ID No.: {job_id}", ln=True)
    pdf.cell(200, 10, txt=f"Date: {date}", ln=True)
    pdf.cell(200, 10, txt=f"Customer Name and Address: {customer_name}", ln=True)
    pdf.cell(200, 10, txt=f"Submitted By: {submitted_by}", ln=True)
    pdf.cell(200, 10, txt=f"Contractor Name: {contractor_name}", ln=True)
    pdf.multi_cell(200, 10, txt=f"Site Address / Project Name: {site_address}")

    # Testing Requirements
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(200, 10, txt="Testing Requirements", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Soil/Rock: {soil_rock}", ln=True)
    pdf.cell(200, 10, txt=f"Design Mix: {design_mix}", ln=True)
    pdf.cell(200, 10, txt=f"Aggregate/Sand/M-Sand: {aggregate}", ln=True)
    pdf.cell(200, 10, txt=f"Cement: {cement}", ln=True)
    pdf.cell(200, 10, txt=f"Brick: {brick}", ln=True)
    pdf.cell(200, 10, txt=f"Cube/Core/ACC Block/Paver Block: {cube}", ln=True)
    pdf.cell(200, 10, txt=f"Water: {water}", ln=True)
    pdf.cell(200, 10, txt=f"NDT/UPV: {ndt_upv}", ln=True)
    pdf.cell(200, 10, txt=f"Bitumen Division/Wooden: {bitumen}", ln=True)

    # Review Section
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(200, 10, txt="Review of Test Request (By Laboratory)", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Test Requirements: {test_requirements}", ln=True)
    pdf.cell(200, 10, txt=f"Capability: {capability}", ln=True)
    pdf.cell(200, 10, txt=f"Condition of Sample: {sample_condition}", ln=True)
    pdf.cell(200, 10, txt=f"Discussion with Customer: {discussion}", ln=True)
    pdf.cell(200, 10, txt=f"Statement of Conformity: {statement_conformity}", ln=True)

    # Signatures
    pdf.cell(200, 10, txt="Signatures:", ln=True)
    pdf.cell(200, 10, txt=f"Customer's Representative: {customer_signature}", ln=True)
    pdf.cell(200, 10, txt=f"Technical Manager: {technical_manager_signature}", ln=True)

    # Save PDF
    pdf_path = "C:\Users\DELL\Downloads\Test_Request_Form.pdf"
    pdf.output(pdf_path)

    # Provide Download Link
    with open(pdf_path, "rb") as pdf_file:
        st.download_button(
            label="Download PDF",
            data=pdf_file,
            file_name="Test_Request_Form.pdf",
            mime="application/pdf",
        )
