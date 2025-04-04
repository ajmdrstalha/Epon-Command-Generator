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
docker build -t epon-app .
docker run -p 8501:8501 epon-app
pip install -r requirements.txt
streamlit run epon_command_generate.py
EPON COMMAND GENERATOR/
│
├── .streamlit/
│   └── config.toml
├── .pages/
│   └── c_data_output.py
│   └── new_user_create.py
├── epon_command_generate.py
└── README.md
