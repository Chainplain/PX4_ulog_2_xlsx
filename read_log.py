from matplotlib import pyplot as plt
import pandas as pd
from pyulog import ULog
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide the root window
Tk().withdraw()

# Open file dialog to select the .ulg file
file_path = askopenfilename(title='Select a .ulg file', filetypes=[('ULG files', '*.ulg')])

if file_path:  # Check if a file was selected
    ulog = ULog(file_path)
    output_file = file_path.replace('.ulg', '.xlsx')
    
    import os
    from tkinter import messagebox

    if os.path.exists(output_file):
        is_willing_to_overwirte = messagebox.askyesno("File Exists", f"'{output_file}' already exists. Do you want to overwrite it?")
        if is_willing_to_overwirte:       
            with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            # Extract each message type and save it as a sheet
                for msg in ulog.data_list:
                    df = pd.DataFrame(msg.data)
                    # Write each DataFrame to a separate sheet
                    df.to_excel(writer, sheet_name=msg.name[:31], index=False)  # Excel sheet names are limited to 31 characters
            print("Overwitten..")
    else:
        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            # Extract each message type and save it as a sheet
                for msg in ulog.data_list:
                    df = pd.DataFrame(msg.data)
                    # Write each DataFrame to a separate sheet
                    df.to_excel(writer, sheet_name=msg.name[:31], index=False)  # Excel sheet names are limited to 31 characters
        print("Create new file..")
else:
    print("No file selected.")
    
df = pd.read_excel(output_file, sheet_name='vehicle_attitude')
timestamps = df['timestamp'].values / 1e6  # Convert from microseconds to seconds

fig, ax = plt.subplots(4, 1, figsize=(12, 12), sharex=True)
fig.canvas.set_window_title('vehicle_attitude')
# fig, ax = plt.subplots(4, 1, figsize=(12, 12), sharex=True)
ax[0].plot(timestamps, df['q[0]'].values)
ax[1].plot(timestamps, df['q[1]'].values)
ax[2].plot(timestamps, df['q[2]'].values)
ax[3].plot(timestamps, df['q[3]'].values)
ax[0].set_title('q[0]')
ax[1].set_title('q[1]')
ax[2].set_title('q[2]')
ax[3].set_title('q[3]')
ax[-1].set_xlabel('time(s)')


df_accel = pd.read_excel(output_file, sheet_name='vehicle_acceleration')
timestamps_accel = df_accel['timestamp'].values / 1e6  # Convert from microseconds to seconds

fig_accel, ax_accel = plt.subplots(3, 1, figsize=(12, 9), sharex=True)
fig_accel.canvas.set_window_title('vehicle_acceleration')
ax_accel[0].plot(timestamps_accel, df_accel['xyz[0]'].values)
ax_accel[1].plot(timestamps_accel, df_accel['xyz[1]'].values)
ax_accel[2].plot(timestamps_accel, df_accel['xyz[2]'].values)
ax_accel[0].set_title('xyz[0]')
ax_accel[1].set_title('xyz[1]')
ax_accel[2].set_title('xyz[2]')
ax_accel[-1].set_xlabel('time(s)')

df_angular_velocity = pd.read_excel(output_file, sheet_name='vehicle_angular_velocity')
timestamps_angular_velocity = df_angular_velocity['timestamp'].values / 1e6  # Convert from microseconds to seconds

fig_angular_velocity, ax_angular_velocity = plt.subplots(3, 1, figsize=(12, 9), sharex=True)
fig_angular_velocity.canvas.set_window_title('vehicle_angular_velocity')
ax_angular_velocity[0].plot(timestamps_angular_velocity, df_angular_velocity['xyz[0]'].values)
ax_angular_velocity[1].plot(timestamps_angular_velocity, df_angular_velocity['xyz[1]'].values)
ax_angular_velocity[2].plot(timestamps_angular_velocity, df_angular_velocity['xyz[2]'].values)
ax_angular_velocity[0].set_title('xyz[0]')
ax_angular_velocity[1].set_title('xyz[1]')
ax_angular_velocity[2].set_title('xyz[2]')
ax_angular_velocity[-1].set_xlabel('time(s)')

plt.tight_layout()
plt.show()

    


