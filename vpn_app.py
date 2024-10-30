import os
import tkinter as tk
from tkinter import messagebox
import subprocess

# Define paths for OpenVPN executable and config files
OPENVPN_PATH = r"C:\Users\sid\Downloads\openvpn\bin\openvpn.exe"  # Change this path as needed
REGION_CONFIGS = {
    "US": r"C:\Users\sid\Downloads\vpn\USA_104.28.195.232_udp.ovpn",  # Change this path as needed
    # Add more regions here as needed
    # "UK": r"C:\Path\To\UK.ovpn",
    # "Canada": r"C:\Path\To\Canada.ovpn",
}

class VPNApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Personal VPN")
        self.master.geometry("400x300")
        self.master.configure(bg='black')

        self.label = tk.Label(master, text="Select VPN Region", bg='black', fg='white', font=('Helvetica', 16))
        self.label.pack(pady=20)

        self.region_var = tk.StringVar(value='')

        self.region_menu = tk.OptionMenu(master, self.region_var, *REGION_CONFIGS.keys())
        self.region_menu.pack(pady=10)

        self.connect_button = tk.Button(master, text="Connect", command=self.connect_vpn, bg='green', fg='white', font=('Helvetica', 12))
        self.connect_button.pack(pady=20)

        self.disconnect_button = tk.Button(master, text="Disconnect", command=self.disconnect_vpn, bg='red', fg='white', font=('Helvetica', 12))
        self.disconnect_button.pack(pady=5)

    def connect_vpn(self):
        region = self.region_var.get()
        if region:
            config_file = REGION_CONFIGS[region]
            print(f"Looking for config file: {config_file}")  # Debug line
            if os.path.exists(config_file):
                subprocess.Popen([OPENVPN_PATH, config_file])  # Run OpenVPN
                messagebox.showinfo("Connection Status", f"Connecting to {region}...")
            else:
                messagebox.showerror("Error", f"Configuration file for {region} not found.")
        else:
            messagebox.showwarning("Warning", "Please select a region.")

    def disconnect_vpn(self):
        subprocess.Popen(["taskkill", "/F", "/IM", "openvpn.exe"])  # Kill OpenVPN process
        messagebox.showinfo("Connection Status", "Disconnected from VPN.")

if __name__ == "__main__":
    root = tk.Tk()
    app = VPNApp(root)
    root.mainloop()
