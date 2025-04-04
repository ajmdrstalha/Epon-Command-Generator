```markdown
# EPON Command Generator

The **EPON Command Generator** is a simple **Streamlit**-based web application that helps users generate common EPON (Ethernet Passive Optical Network) commands. Users can generate commands for **OLT ports**, **ONU IDs**, **VLAN tags**, and more, making network management and troubleshooting easier and faster.

## Features

- **Generate EPON commands** based on OLT port and ONU ID.
- Includes commands for **signal check**, **MAC address**, **port state**, **reboot**, **inactive ONU info**, and **running config**.
- **New User Create** section to generate configuration commands for setting up new users.
- **EPON ONU diagnostics** and more!

## Prerequisites

To run this app locally, you will need:

- **Docker** installed on your machine
- **Git** for version control
- **Python 3.10+** (for local development, optional if using Docker)

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/epon-command-generator.git
cd epon-command-generator
```

### 2. Run the application using Docker:

#### Build the Docker image:

```bash
docker build -t epon-app .
```

#### Run the Docker container:

```bash
docker run -p 8501:8501 epon-app
```

This will run the app at `http://localhost:8501`.

### 3. Run Locally (Optional)

If you prefer running the app locally (without Docker):

1. Install Python dependencies:

```bash
pip install -r requirements.txt
```

2. Run the Streamlit app:

```bash
streamlit run epon_command_generate.py
```

This will start the app on `http://localhost:8501`.

## Usage

1. **New User Create:**
   - Enter OLT port, ONU ID, VLAN tag, and description to generate commands for setting up a new user.

2. **EPON Diagnostics:**
   - Enter OLT port and ONU ID to generate various EPON diagnostic commands like signal check, port state, and more.

## Help Section

A comprehensive guide is provided within the app. Use the "ℹ️ Help" section for detailed instructions on how to use the app.

## Project Structure

```
EPON COMMAND GENERATOR/
│
├── .streamlit/
│   └── config.toml
├── .pages/
│   └── c_data_output.py
│   └── new_user_create.py
├── epon_command_generate.py
└── README.md
```

## Contributing

Feel free to open issues or pull requests if you find any bugs or want to add features. 

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

---

### Notes:
- **Replace** `YOUR-USERNAME` with your GitHub username.
- If you want to include instructions for local setup, it’s included in the **Installation** section.
- You can also add a **License** section if you plan to distribute your project.

Let me know if you want to include any specific information or examples!
