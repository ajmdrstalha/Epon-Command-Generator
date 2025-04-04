import streamlit as st

# Set page config
st.set_page_config(page_title="EPON Command Generator", page_icon="💻")

# Sidebar for navigation
page = st.sidebar.radio

# Page 1: Home - Generate Commands
st.title("💻 EPON Command Generator")
st.write("Enter the ONT ID to generate commands for EPON diagnostics.")

# ONT ID input
user_input = st.text_input("Enter the ONT ID (e.g., 2 45)", key="ont_input")

# Button to generate the commands
generate_button = st.button("Generate Commands")

# Check if either button is pressed or 'Enter' key is used
if generate_button or user_input:
    if user_input:
        try:
            olt_port, onu_id = map(int, user_input.split())
            st.markdown("### Generated Commands:")

            # Command 1: Optical Information
            command_1 = f"enable\nconfig\ninterface epon 0/0\nshow ont optical-info {olt_port} {onu_id}\nshow port ddm-info {olt_port} detail"
            st.code(command_1, language="bash")
        except ValueError:
            st.warning("⚠️ Please enter two valid numbers separated by a space!")
    else:
        st.warning("⚠️ Please enter ONT ID values.")

# Help Section
with st.expander("ℹ️ Help"):
    st.markdown(
        """
        **How to use:**
        - Enter two numbers separated by space in the input field.
        - First number: OLT port.
        - Second number: ONU ID.
        - Example: "2 45".
        - Click 'Generate Commands' to create the EPON commands or press Enter after entering the values.
        """
    )
