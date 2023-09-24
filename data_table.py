from prettytable import PrettyTable

Table = PrettyTable(["Name", "Password", "Age", "Created", ])

Table.add_row(["Admin", "Admin123", "Undfined", "24.09.2023",])
Table.add_row(["Kali", "Kali#1731", "Undfined", "24.09.2023",])
Table.add_row(["vvl", "wdfihb#208", "Undfined", "24.09.2023",])
Table.add_row(["critick", "heartattack$bash", "Undfined", "24.09.2023",])

print(Table)
