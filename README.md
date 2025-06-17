# Terneo / Welrok Thermostat

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)

A Home Assistant integration for Terneo and Welrok smart thermostats. This component provides local control of your thermostat devices through Home Assistant, supporting both Terneo and Welrok brands as they use the same hardware.

## Features

- Local network control of your thermostat
- Temperature control and monitoring
- Schedule management
- Operation mode control
- Energy consumption monitoring
- Real-time status updates

## Requirements

- Home Assistant 2025.5 or newer
- Device firmware version 2.3 or above
- Local network access to the thermostat
- Unblocked local network control (see Security section)

## Security Note

For firmware version 2.3 and above, local network control is blocked by default for security reasons. You need to unblock it:

- [Terneo Unblock Instructions](https://terneo-api.readthedocs.io/ru/latest/en/safety.html)
- [Welrok Unblock Instructions](https://welrok-local-api.readthedocs.io/en/latest/en/safety.html)

## Installation

### Option 1: Manual Installation
1. Download the `terneo` folder
2. Copy it to your Home Assistant `custom_components` directory
3. Restart Home Assistant

### Option 2: HACS Installation
1. Open HACS in your Home Assistant instance
2. Go to Integrations
3. Click the three dots (⋮) at the top right
4. Select "Custom repositories"
5. Add this repository URL
6. Select "Integration" as the category
7. Click "ADD"
8. Go to the Integrations tab
9. Find and install "Terneo Thermostat"

## Configuration

Add the following to your `configuration.yaml`:

```yaml
climate:
  - platform: terneo
    serial: 'DEVICE_SERIALNUMBER'
    host: 'DEVICE_IP'
```

### Finding Your Device Information

1. Open your web browser
2. Navigate to `http://{device_ip}/index.html`
3. Find your device's serial number on this page

## API Documentation

- [Terneo API Documentation](https://terneo-api.readthedocs.io/ru/latest/)
- [Welrok API Documentation](https://welrok-local-api.readthedocs.io/ru/latest/)