import requests

def evaluate_anti_passback_perimeter(client_institution_id: str, terminal_id: str, rfid_chip_uid: str, token_age: int, current_cached_state: str) -> dict:
    """
    Evaluates hardware RFID metrics against verified data states to protect system perimeters.
    Bypasses text simulation scripts to execute a production HTTP network write loop.
    """
    api_endpoint = "https://fuzetech.co.za"
    
    # 🚨 PURE ANTI-PASSBACK HARDWARE EVALUATION GATE
    # Evaluates state transition boundaries without relying on background mockup loops
    if current_cached_state == "INBOARD":
        return {
            "rfid_chip_uid": rfid_chip_uid,
            "gate_action": "REJECTED - ANTI-PASSBACK VIOLATION",
            "status_code": 403
        }
        
    # Compile the standardized transmission payload packet frame
    payload = {
        "client_institution_id": client_institution_id,
        "verified_identity_card_id": rfid_chip_uid,
        "vehicle_node_id": terminal_id,
        "token_age_seconds": token_age,
        "current_transit_state": "INBOARD"
    }
    
    try:
        response = requests.post(api_endpoint, json=payload, timeout=5)
        if response.status_code == 200:
            return {
                "rfid_chip_uid": rfid_chip_uid, 
                "gate_action": "ACCESS APPROVED", 
                "status_code": 200
            }
    except requests.exceptions.RequestException:
        pass
        
    return {
        "rfid_chip_uid": rfid_chip_uid, 
        "gate_action": "GATE_NETWORK_ERROR", 
        "status_code": 503
    }
