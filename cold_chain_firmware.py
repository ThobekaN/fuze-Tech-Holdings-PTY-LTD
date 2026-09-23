import requests

def transmit_thermal_telemetry(client_healthcare_id: str, probe_serial: str, clinical_facility_name: str, current_temperature_celsius: float, thermal_slope_derivative: float) -> dict:
    """
    Executes a clean production HTTP POST network request to transmit ambient environmental 
    parameters straight up the internet pipeline into the central PostgreSQL database.
    """
    api_endpoint = "https://fuzetech.co.za"
    
    payload = {
        "client_healthcare_id": client_healthcare_id,
        "physical_probe_serial": probe_serial,
        "clinical_facility_name": clinical_facility_name,
        "current_temperature_celsius": current_temperature_celsius,
        "thermal_slope_derivative": thermal_slope_derivative,
        "inventory_security_status": "NORMAL" if current_temperature_celsius <= 8.0 else "EMERGENCY SPIKE"
    }
    
    try:
        response = requests.post(api_endpoint, json=payload, timeout=5)
        return {
            "status_code": response.status_code,
            "success": response.status_code == 200
        }
    except requests.exceptions.RequestException:
        return {
            "status_code": 503,
            "success": False
        }
