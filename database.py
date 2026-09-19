# ==============================================================================
# FUZE TECH HOLDINGS — RECOVERY & ANALYTICS DATA UTILITY HUB
# Simulated Multi-Tenant PostgreSQL Relational Schema
# ==============================================================================

# 👥 USER AUTHENTICATION & ACCESS REGISTRY TABLE
MOCK_CLIENTS_DB = [
    {
        "email": "lead@fuzetech.co.za",
        "password": "password123",
        "account_name": "Prospective Client (Lead-Tier Account)",
        "client_id": "CLIENT-000",
        "is_logtech_active": False,
        "is_gridtech_active": False
    },
    {
        "email": "operations@supergroup.co.za",
        "password": "superfleet2026",
        "account_name": "Super Group Logistics",
        "client_id": "CLIENT-881",
        "is_logtech_active": True,
        "is_gridtech_active": False
    },
    {
        "email": "director@imperial.co.za",
        "password": "enterpriseultra",
        "account_name": "Imperial Logistics Group",
        "client_id": "CLIENT-442",
        "is_logtech_active": True,
        "is_gridtech_active": True
    }
]

# 🚚 LOGTECH VEHICLE TELEMETRY TRANSACTION REGISTRY (Gated by client_id)
MOCK_FLEET_TELEMETRY = {
    "CLIENT-881": [
        {"Truck_ID": "LFL-001", "Driver": "Sipho M.", "Route": "JHB -> Gaborone", "Speed_KMH": 0.0, "Fuel_Liters": 280.5, "BURS_Clearance": "PROCEED TO BORDER"},
        {"Truck_ID": "LFL-002", "Driver": "Johan B.", "Route": "JHB -> Windhoek", "Speed_KMH": 80.0, "Fuel_Liters": 300.0, "BURS_Clearance": "HOLD AT STAGING"},
        {"Truck_ID": "LFL-003", "Driver": "Thabo N.", "Route": "JHB -> Lobatse", "Speed_KMH": 0.0, "Fuel_Liters": 195.0, "BURS_Clearance": "HOLD AT STAGING"}
    ],
    "CLIENT-442": [
        {"Truck_ID": "IMP-901", "Driver": "Blessing T.", "Route": "DBN -> Gaborone", "Speed_KMH": 65.0, "Fuel_Liters": 410.2, "BURS_Clearance": "PROCEED TO BORDER"},
        {"Truck_ID": "IMP-902", "Driver": "Musa Z.", "Route": "JHB -> Maseru", "Speed_KMH": 0.0, "Fuel_Liters": 380.0, "BURS_Clearance": "PROCEED TO BORDER"}
    ]
}

# ⚡ GRIDTECH SMART METER METRIC REGISTRY (Gated by client_id)
MOCK_GRID_TELEMETRY = {
    "CLIENT-442": [
        {"Meter_ID": "MTR-801", "Property_Fund": "Growthpoint Braamfontein", "Metered_Usage_kW": 4.2, "Substation_Line_Current_Amps": 18.5, "System_Status": "NORMAL"},
        {"Meter_ID": "MTR-802", "Property_Fund": "Redefine Parktown", "Metered_Usage_kW": 0.8, "Substation_Line_Current_Amps": 4.1, "System_Status": "NORMAL"},
        {"Meter_ID": "MTR-803", "Property_Fund": "Wits Student Housing", "Metered_Usage_kW": 0.0, "Substation_Line_Current_Amps": 45.2, "System_Status": "SUSPECTED BYPASS"}
    ]
}
