import pandas as pd
import ipaddress

def cidr_to_ip_range(cidr):
    try:
        network = ipaddress.ip_network(cidr)
        if network.version == 4:
            from_ip = str(network.network_address)
            to_ip = str(network.broadcast_address)
        elif network.version == 6:
            from_ip = str(network.network_address.exploded)
            to_ip = str(network.broadcast_address.exploded)
        else:
            return None, None
        return from_ip, to_ip
    except ValueError:
        return None, None

# Read the Excel file
excel_file_path = r'C:\Users\nayan.tank\Downloads\AzureIPs.xlsx'
df = pd.read_excel(excel_file_path)

# Apply cidr_to_ip_range function to calculate from_ip and to_ip
df[['FromIP', 'ToIP']] = df['CIDR'].apply(lambda x: pd.Series(cidr_to_ip_range(x)))

# Write the modified DataFrame back to the Excel file
df.to_excel(excel_file_path, index=False)
