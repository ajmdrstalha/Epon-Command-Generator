import streamlit as st

st.set_page_config(page_title="EPON Command Generator", page_icon="💻")

# Sidebar for navigation
page = st.sidebar.radio

if page == "New User Create":
    st.switch_page("pages/new_user_create")

st.title("💻 EPON Command Generator")
st.write("Generate EPON commands by entering the OLT port, ONU ID, VLAN tag, and a description.")

# Show the `show epon onu-information dynamic` command before input
epon_info_dynamic_command = "enable\nshow epon onu-information dynamic"
st.markdown("### **EPON ONU Information Dynamic Command:**")
st.code(epon_info_dynamic_command, language="bash")

# Function to generate EPON commands
def generate_commands():
    user_input = st.session_state.input
    vlan_input = st.session_state.vlan
    description_input = st.session_state.description
    
    if user_input and vlan_input and description_input:
        olt_port, onu_id = user_input.split()
        
        # Show the confirm-onu line in a copyable code block
        st.markdown("**Confirm/Configure ONU Command:**")
        st.code(f"epon confirm-onu int epon0/{olt_port}:{onu_id}", language="bash")
        st.code(f"epon conform-onu int epon0/{olt_port}:{onu_id}", language="bash")
        
        # Command Block
        config_commands = (
            f"config\n"
            f"int epon0/{olt_port}:{onu_id}\n"
            f"epon onu all-port ctc vlan mode tag {vlan_input}\n"
            f"description {description_input}\n"
            f"exit\n"
            f"write all\n"
            f"exit"
        )
        
        st.code(config_commands, language="bash")
    else:
        st.warning("Please fill in all the fields: EPON interface, VLAN tag, and description!")

# Input fields for OLT Port, ONU ID, VLAN tag, and Description
with st.form(key="command_form"):
    st.text_input("Enter EPON interface", key="input")
    st.text_input("Enter VLAN tag", key="vlan")
    st.text_input("Enter Description", key="description")
    submit_button = st.form_submit_button("Generate Commands")

# Triggering generate_commands() when the Enter key is pressed or the button is clicked
if submit_button or st.session_state.get('input'):
    generate_commands()

# Help Section
with st.expander("ℹ️ Help"):
    st.markdown(
        """
        **How to use:**
        - Enter EPON interface in 'x y' format (e.g., "1 14").
        - Enter VLAN tag (e.g., "13").
        - Enter a description (e.g., "talha").
        - Click 'Generate Command' or press the keyboard Enter button.
        """
    )
