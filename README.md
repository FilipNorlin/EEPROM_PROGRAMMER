# EEPROM_PROGRAMMER

## Diagram

```mermaid
flowchart TD
    BAT(Battery) --> V_REG(Voltage Regulator)
    V_REG --> Protection(Input Protection)
    USB(USB C) --> Protection
    Protection --> MCU{MCU}
    MCU --> LCD(LCD Display)
    MCU --> Input(Input Controls)
    MCU --> SD(SD Card Reader)
    MCU --> Logic(Logic)
    Logic --> LED(Data LEDs)
    Logic --> EEPROM(EEPROM)
