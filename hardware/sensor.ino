const float shunt_resistor = 10.0;  // 10Ω resistor
const float v_ref = 5.0;            // Reference voltage
const int adc_max = 1023;           // 10-bit ADC resolution
unsigned long last_time = 0;        // Time tracking
float total_energy_joules = 0.0;    // Energy in joules

void setup() {
    Serial.begin(9600);
    last_time = millis();  // Initialize time tracking
}

void loop() {
    // Read voltages
    float v0 = analogRead(A0) * (v_ref / adc_max);  
    float v1 = analogRead(A1) * (v_ref / adc_max);  
    float v_drop = v0 - v1; 
    float current = v_drop / shunt_resistor;  
    float power = v0 * current;  

    // Time calculations
    unsigned long current_time = millis();
    float delta_time = (current_time - last_time) / 1000.0; // Convert ms to seconds
    last_time = current_time;

    // Energy accumulation
    total_energy_joules += power * delta_time; // E = P × t

    // Convert to mWh
    float energy_mWh = total_energy_joules * 1000.0 / 3600.0;  

    // Serial output
    // Serial.print("Power: ");
    // Serial.print(power * 1000, 2); // mW
    // Serial.print(" mW | Energy: ");
    Serial.print(energy_mWh, 4); // mWh
    // Serial.println(" mWh");

    delay(1000);
}
