![CIEI](../images/ciei.jpg)
# Software Installation and Setup:

## Shim Main Driving Code Installation:

Before starting the installation and setup, make sure you are logged into your Raspberry Pi. The driving code for the Hack-A-Thon will already be located in a folder labeled with your team name.

### Step 1: Navigate to Your Team's Directory

Navigate to your team's directory, where the driving code is located. Replace `Your_Team_Name` with the name of your team (ie. `team1`):

```bash
cd /path/to/Your_Team_Name
```

### Step 2: Install Python Dependencies

Next, install the Python dependencies required to run the application. These dependencies are listed in a file called `requirements.txt` in your team's directory `lora` directory. We will use `pip3`, the Python package manager, to install these dependencies:

```bash
sudo pip3 install -r requirements.txt
```

### Step 3: Verify Node Keys

The last step is to check that the correct keys for your specific node have been entered. You will be given a set of keys assigned to your device. These keys need to be checked inside the `keys.py` file, located in the `lora` directory within your team's directory. Your teams specific keys should already be included but it will be good to familarize yourself with them.

You can edit this file using a text editor such as `nano`:

```bash
nano keys.py
```

Once you have finished, press `Ctrl + X` to exit `nano`, press `Y` to save the changes, and then press `Enter` to confirm the filename.

Remember, it's important to keep these keys secret, as they are used to secure the communication between your device and the network.

### After these steps, your Raspberry Pi and the main driving code are now set up and ready to be used in the Hack-A-Thon!


<div style="display: flex; justify-content: space-between;">
  <img src="../images/stemx.png" width="30%" height="10%" />
  <img src="../images/PoweredByPITON.png" width="30%" height="10%"/> 
</div>

