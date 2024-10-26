from pyulog import ULog
import pandas as pd

# Load the ULog file
ulog = ULog('log_9_2024-10-14-15-00-06.ulg')

# Extract and save each message type
with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer:
    # Extract each message type and save it as a sheet
    for msg in ulog.data_list:
        df = pd.DataFrame(msg.data)
        # Write each DataFrame to a separate sheet
        df.to_excel(writer, sheet_name=msg.name[:31], index=False)  # Excel sheet names are limited to 31 characters
