con = Netmiko(host = '98.43.1.27',
              username = 'admin',
              password = 'admin',
              port = 22,
              device_type = 'cisco_xr',
              timeout = 160,
              verbose = False)

show_version  = con.send_command('show interface description')

results = parser.parse(show_version,"show interface description","nxos")

for key,value in results.items():
        for key1,value1 in value.items():
                for key2,value2 in value1.items():
                        if value2 == "down" or value2 == "admin-down":
                                print(f"{key1} interface is in down state.")
