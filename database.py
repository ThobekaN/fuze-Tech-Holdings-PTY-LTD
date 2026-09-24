# ==============================================================================
# FUZE TECH HOLDINGS — RECOVERY & ANALYTICS DATA UTILITY HUB
# Centralized Multi-Tenant Production Data Schema
# ==============================================================================

# 👥 USER AUTHENTICATION & ACCESS REGISTRY TABLE
MOCK_CLIENTS_DB = [
    {
        "email": "lead@fuzetech.co.za",
        "password": "password123",
        "account_name": "Prospective Client (Lead-Tier Account)",
        "client_id": "CLIENT-000",
        "is_logtech_active": True,
        "is_gridtech_active": False,
        "is_cybertech_active": False,
        "is_transittech_active": False,
        "is_healthtech_active": False
    },
    {
        "email": "operations@supergroup.co.za",
        "password": "superfleet2026",
        "account_name": "Super Group Logistics",
        "client_id": "CLIENT-881",
        "is_logtech_active": True,
        "is_gridtech_active": False,
        "is_cybertech_active": False,
        "is_transittech_active": False,
        "is_healthtech_active": False
    },
    {
        "email": "director@imperial.co.za",
        "password": "enterpriseultra",
        "account_name": "Imperial Group (Full Enterprise Suite)",
        "client_id": "CLIENT-442",
        "is_logtech_active": True,
        "is_gridtech_active": True,
        "is_cybertech_active": True,
        "is_transittech_active": True, # TransitTech Enabled
        "is_healthtech_active": True   # HealthTech Enabled
    }
]

# 🚚 LOGTECH VEHICLE TELEMETRY TRANSACTION REGISTRY (Gated by client_id)
MOCK_FLEET_TELEMETRY = {
    "CLIENT-000": [
        {"Truck_ID": "PC-01", "Driver": "Samkelo M.", "Route": "DBN -> Windhoek", "Speed_KMH": 0.0, "Fuel_Liters": 250.5, "BURS_Clearance": "PROCEED TO BORDER"},
        {"Truck_ID": "PC-02", "Driver": "Falakhe M.", "Route": "DBN -> Windhoek", "Speed_KMH": 60.0, "Fuel_Liters": 300.0, "BURS_Clearance": "HOLD AT STAGING"}
    ]
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

# 🛡️ CYBERTECH PROMO TRANSACTION REGISTRY (Gated by client_id)
MOCK_CYBER_TELEMETRY = {
    "CLIENT-442": [
        {"Transaction_ID": "TXN-901", "User_Alias": "new_user_jhb", "Claimed_Email": "thabo.m@gmail.com", "Device_Hardware_Fingerprint": "HW-UUID-4401", "Promo_Code": "FIRST100", "Evaluation_Status": "APPROVED"},
        {"Transaction_ID": "TXN-902", "User_Alias": "kfc_lover_22", "Claimed_Email": "lindiwe.k@outlook.com", "Device_Hardware_Fingerprint": "HW-UUID-8892", "Promo_Code": "EATSNEW50", "Evaluation_Status": "APPROVED"},
        {"Transaction_ID": "TXN-903", "User_Alias": "disposable_acc_7", "Claimed_Email": "x7291@tempmail.io", "Device_Hardware_Fingerprint": "HW-UUID-1105", "Promo_Code": "FIRST100", "Evaluation_Status": "TRIGGERED COORD CLUSTER"}
    ]
}

# 🚌 TRANSITTECH ENTRY/EXIT SHUTTLE GATEWAY REGISTRY (Gated by client_id)
MOCK_TRANSIT_TELEMETRY = {
    "CLIENT-442": [
        {"Scan_ID": "SCN-701", "Student_Staff_ID": "WITS-10024", "Transit_Route": "Braamfontein -> Education", "Card_State": "DEBOARDED", "Token_Age_Sec": 12, "Gate_Action": "ACCESS APPROVED"},
        {"Scan_ID": "SCN-702", "Student_Staff_ID": "WITS-20491", "Transit_Route": "Main Campus -> Junction", "Card_State": "OUTSIDE_SYSTEM", "Token_Age_Sec": 8, "Gate_Action": "ACCESS APPROVED"},
        {"Scan_ID": "SCN-703", "Student_Staff_ID": "WITS-10024", "Transit_Route": "Braamfontein -> Education", "Card_State": "IN_TRANSIT", "Token_Age_Sec": 4, "Gate_Action": "REJECTED - ANTI-PASSBACK"}
    ]
}

# 🏥 HEALTHTECH COLD STORAGE THERMAL LOG MATRIX (Gated by client_id)
MOCK_HEALTH_TELEMETRY = {
    "CLIENT-442": [
        {"Fridge_ID": "FRG-501", "Clinical_Facility": "Braamfontein Clinic", "Current_Temp_C": 4.2, "Safety_Range": "2°C - 8°C", "Thermal_Status": "NORMAL"},
        {"Fridge_ID": "FRG-502", "Clinical_Facility": "Hillbrow Health Hub", "Current_Temp_C": 5.1, "Safety_Range": "2°C - 8°C", "Thermal_Status": "NORMAL"},
        {"Fridge_ID": "FRG-503", "Clinical_Facility": "Parktown Pharmacy", "Current_Temp_C": 14.8, "Safety_Range": "2°C - 8°C", "Thermal_Status": "CRITICAL SPIKE"}
    ]
}
# ==============================================================================
# EXTERNAL TELEMATICS PROVIDER CLOUD SERVERS (Simulating Third-Party Tracking APIs)
# ==============================================================================
REMOTE_TRACKING_SERVERS_JSON = {
    "cartrack_oauth2_token_000": [
        {"Truck_ID": "PC-01", "Driver": "Samkelo M.", "Route": "DBN -> Windhoek", "Speed_KMH": 0.0, "Fuel_Liters": 250.5, "BURS_Clearance": "PROCEED TO BORDER"},
        {"Truck_ID": "PC-02", "Driver": "Falakhe M.", "Route": "DBN -> Windhoek", "Speed_KMH": 60.0, "Fuel_Liters": 300.0, "BURS_Clearance": "HOLD AT STAGING"}
    ]
    "cartrack_oauth2_token_881": [
        {"Truck_ID": "ND-882-901", "Driver": "Sipho Khumalo", "Route": "JHB -> Gaborone", "Speed_KMH": 0.0, "Fuel_Liters": 280.5, "BURS_Clearance": "PROCEED TO BORDER"},
        {"Truck_ID": "ND-104-552", "Driver": "Johan Burger", "Route": "JHB -> Windhoek", "Speed_KMH": 82.0, "Fuel_Liters": 310.0, "BURS_Clearance": "HOLD AT STAGING"},
        {"Truck_ID": "ND-773-441", "Driver": "Thabo Ncube", "Route": "JHB -> Lobatse", "Speed_KMH": 0.0, "Fuel_Liters": 195.0, "BURS_Clearance": "HOLD AT STAGING"}
    ],
    "ctrack_secure_key_442": [
        {"Truck_ID": "NC-551-209", "Driver": "Blessing Tau", "Route": "DBN -> Gaborone", "Speed_KMH": 65.0, "Fuel_Liters": 410.2, "BURS_Clearance": "PROCEED TO BORDER"},
        {"Truck_ID": "NC-992-881", "Driver": "Musa Zwane", "Route": "JHB -> Maseru", "Speed_KMH": 0.0, "Fuel_Liters": 380.0, "BURS_Clearance": "PROCEED TO BORDER"}
    ]
}

REMOTE_MUNICIPAL_GRID_JSON = {
    "city_power_grid_key_442": [
        {"Meter_ID": "MTR-991", "Property_Fund": "Growthpoint Braamfontein", "Metered_Usage_kW": 4.2, "Substation_Line_Current_Amps": 18.5, "System_Status": "NORMAL"},
        {"Meter_ID": "MTR-992", "Property_Fund": "Redefine Parktown", "Metered_Usage_kW": 0.8, "Substation_Line_Current_Amps": 4.1, "System_Status": "NORMAL"},
        {"Meter_ID": "MTR-993", "Property_Fund": "Wits Student Housing", "Metered_Usage_kW": 0.0, "Substation_Line_Current_Amps": 45.2, "System_Status": "SUSPECTED BYPASS"}
    ]
}
