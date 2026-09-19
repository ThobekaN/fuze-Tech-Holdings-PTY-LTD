CREATE TABLE clients ( 
	client_id VARCHAR(50) PRIMARY KEY, 
	(Super Group) corporate_name VARCHAR(150) NOT NULL, 
	account_email VARCHAR(100) UNIQUE NOT NULL, 
	security_hash VARCHAR(255) NOT NULL, 
	is_logtech_active BOOLEAN DEFAULT FALSE, 	is_gridtech_active BOOLEAN DEFAULT FALSE, 	is_cybertech_active BOOLEAN DEFAULT FALSE, 	is_transittech_active BOOLEAN DEFAULT FALSE, 	is_healthtech_active BOOLEAN DEFAULT FALSE, 
	created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

ALTER TABLE clients ENABLE ROW LEVEL SECURITY;

CREATE TABLE vehicles ( 
	vehicle_id SERIAL PRIMARY KEY, 
	client_owner_id VARCHAR(50) REFERENCES clients(client_id) ON DELETE CASCADE, 
	truck_registration VARCHAR(20) NOT NULL, 
	assigned_driver VARCHAR(100), 
	active_route_corridor VARCHAR(150), 
	live_speed_kmh NUMERIC(5,2) DEFAULT 0.0, 
	fuel_volume_liters NUMERIC(6,2) NOT NULL, 
	burs_clearance_status VARCHAR(50) DEFAULT 'HOLD AT STAGING', 	
	last_telematics_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
); 
CREATE INDEX idx_vehicle_tenant_isolation ON vehicles(client_owner_id);

CREATE TABLE smart_meters ( 
	meter_node_id SERIAL PRIMARY KEY, 
	client_landlord_id VARCHAR(50) REFERENCES clients(client_id) ON DELETE CASCADE, 	
	physical_meter_serial VARCHAR(50) UNIQUE NOT NULL, 	
	facility_account_name VARCHAR(150) NOT NULL, 	
	metered_consumption_kw NUMERIC(6,2) DEFAULT 0.0, 	
	transformer_line_amps NUMERIC(6,2) NOT NULL, 	
	system_integrity_status VARCHAR(50) DEFAULT 'NORMAL', 	
	logged_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

CREATE INDEX idx_meter_tenant_isolation ON smart_meters(client_landlord_id);

CREATE TABLE api_checkouts ( 
	transaction_uuid VARCHAR(64) PRIMARY KEY, 
	client_app_id VARCHAR(50) REFERENCES clients(client_id) ON DELETE CASCADE, 
	user_alias VARCHAR(100) NOT NULL, 
	claimed_email VARCHAR(150) NOT NULL, 
	hardware_fingerprint_hash VARCHAR(64) NOT NULL, 
	-- Core anti-cloning immutable key 
	promo_code_applied VARCHAR(50), 
	spatial_latitude NUMERIC(9,6), 
	spatial_longitude NUMERIC(9,6), 
	evaluation_status VARCHAR(50) DEFAULT 'APPROVED', 	
	vetted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

CREATE INDEX idx_cyber_tenant_isolation ON api_checkouts(client_app_id);

CREATE INDEX idx_hardware_fingerprint ON api_checkouts(hardware_fingerprint_hash);

CREATE TABLE transit_scans ( 
	scan_id SERIAL PRIMARY KEY, 
	client_institution_id VARCHAR(50) REFERENCES clients(client_id) ON DELETE CASCADE, 	
	verified_identity_card_id VARCHAR(30) NOT NULL, 
	-- Student / Staff identity reference 
	vehicle_node_id VARCHAR(20) NOT NULL, 
	-- Shuttle bus hardware terminal ID 	
	current_transit_state VARCHAR(30) DEFAULT 'OUTSIDE_SYSTEM', 
	-- For Anti-Passback state tracking 
	token_age_seconds INT NOT NULL, 
	-- Cryptographic rotation age validation 
	gate_response_status VARCHAR(50) DEFAULT 'ACCESS APPROVED', 	
  	scanned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
);

CREATE INDEX idx_transit_tenant_isolation ON transit_scans(client_institution_id); 

CREATE INDEX idx_anti_passback_state ON transit_scans(verified_identity_card_id, current_transit_state);

CREATE TABLE cold_chain_probes ( 
	probe_id SERIAL PRIMARY KEY, 
	client_healthcare_id VARCHAR(50) REFERENCES clients(client_id) ON DELETE CASCADE, 
	physical_probe_serial VARCHAR(50) UNIQUE NOT NULL, 	
	clinical_facility_name VARCHAR(150) NOT NULL, 	
	current_temperature_celsius NUMERIC(4,2) NOT NULL, 	
	thermal_slope_derivative NUMERIC(4,2) NOT NULL,
	-- Trajectory calculation metric 
	inventory_security_status VARCHAR(50) DEFAULT 'NORMAL', 
	last_ping_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
); 

CREATE INDEX idx_health_tenant_isolation ON cold_chain_probes(client_healthcare_id);

