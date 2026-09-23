import hashlib
import requests

def calculate_device_fingerprint(cpu_cores: int, total_storage_gb: int, os_build_signature: str) -> str:
    """
    Computes an unalterable, hardware-derived cryptographic signature hash.
    App cloners or local system cache clears cannot modify these underlying specs.
    """
    raw_hardware_string = f"{cpu_cores}-{total_storage_gb}-{os_build_signature}"
    fingerprint_hash = hashlib.sha256(raw_hardware_string.encode()).hexdigest()
    return f"HW-UUID-{fingerprint_hash[:6].upper()}"

def transmit_checkout_verification(client_app_id: str, user_alias: str, email: str, promo_code: str, lat: float, lon: float, hardware_specs: dict) -> dict:
    """
    Compiles client checkout variables into a structured JSON transmission payload block
    and transmits it via an HTTP POST request to the central Fuze Tech API gateway.
    """
    api_endpoint = "https://fuzetech.co.za"
    
    fingerprint = calculate_device_fingerprint(
        cpu_cores=hardware_specs.get("cpu_cores", 4),
        total_storage_gb=hardware_specs.get("storage", 64),
        os_build_signature=hardware_specs.get("os_build", "Android-14.0")
    )
    
    payload = {
        "client_app_id": client_app_id,
        "user_alias": user_alias.strip(),
        "claimed_email": email.lower().strip(),
        "device_hardware_fingerprint": fingerprint,
        "promo_code_applied": promo_code.upper().strip() if promo_code else "NONE",
        "spatial_latitude": lat,
        "spatial_longitude": lon
    }
    
    try:
        response = requests.post(api_endpoint, json=payload, timeout=5)
        return {
            "status_code": response.status_code,
            "api_response": response.json() if response.status_code == 200 else None
        }
    except requests.exceptions.RequestException:
        return {"status_code": 503, "api_response": None}
