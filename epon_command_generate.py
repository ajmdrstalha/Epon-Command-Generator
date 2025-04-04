import streamlit as st

st.set_page_config(page_title="EPON Command Generator", page_icon="💻")

# Sidebar for navigation
page = st.sidebar.radio

if page == "New User Create":
    st.switch_page("pages/new_user_create")

st.title("💻 EPON Command Generator")
st.write("Generate EPON commands by entering the OLT port and ONU ID numbers.")

# Input Form
with st.form(key="command_form"):
    user_input = st.text_input("Enter OLT Port and ONU ID (e.g., 2 14)", key="input")
    submit_button = st.form_submit_button("Generate Commands")

if submit_button and user_input:
    olt_port, onu_id = user_input.split()
    
    st.markdown("**Signal Check:**")
    combined_command = (
        f"enable\n"
        f"show ep optical-transceiver-diagnosis interface epon0/{olt_port}:{onu_id}\n"
        f"show epon interface epon0/{olt_port}:{onu_id} onu ctc optical-transceiver-diagnosis"
    )
    st.code(combined_command, language="bash")

    st.markdown("**Mac-Address:**")
    st.code(f"show mac address-table interface epon0/{olt_port}:{onu_id}", language="bash")

    st.markdown("**Port State:**")
    st.code(f"show epon interface epon0/{olt_port}:{onu_id} onu port 1 state", language="bash")

    st.markdown("**Reboot:**")
    st.code(f"epon reboot onu int ep 0/{olt_port}:{onu_id}", language="bash")

    st.markdown("**Inactive Onu Info. :**")
    st.code(f"show epon inactive-onu int epon0/{olt_port}", language="bash")

    st.markdown("**Running Config :**")
    st.code(f"show running-config int epon0/{olt_port}:{onu_id}", language="bash")

elif submit_button:
    st.warning("Please enter valid OLT Port and ONU ID!")

# Help Section
with st.expander("ℹ️ Help"):
    st.markdown(
        """
        **How to use:**
        - Enter two numbers separated by space in the input field.
        - First number: OLT port.
        - Second number: ONU ID.
        - Example: "2 14".
        - Click 'Generate Commands' or press Enter to create the EPON commands.
        """
    )
