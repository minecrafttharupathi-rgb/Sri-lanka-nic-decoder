# Sri Lanka NIC Decoder

A simple Python GUI application built with Tkinter that decodes Sri Lankan National Identity Card (NIC) numbers and displays:

* NIC Type (Old/New)
* Date of Birth (DOB)
* Gender
* Current Age
* NIC Validation Status

## Features

* Supports both Old NIC format (e.g., `991234567V`)
* Supports New NIC format (e.g., `199912345678`)
* Automatically calculates age using the current system date
* Detects gender from the NIC day code
* Simple graphical user interface (GUI)
* Error handling for invalid NIC numbers

## Requirements

* Python 3.x
* Tkinter (included with most Python installations)

## Installation

Install python

## Prerequisites

Install Python 3 from:

https://www.python.org/downloads/

Verify the installation:

```bash
python --version
```

or

```bash
python3 --version
```
Clone the repository:

```bash
git clone https://github.com/minecrafttharupathi-rgb/Sri-lanka-nic-decoder.git
cd Sri-lanka-nic-decoder
```

Run the application:

```bash
python sri_lanka_nic_card_reader_1.6.py
```

## How It Works

### Old NIC Format

Example:

```text
991234567V
```

* First 2 digits = Birth year
* Next 3 digits = Day of year
* Last character = V or X

### New NIC Format

Example:

```text
199912345678
```

* First 4 digits = Birth year
* Next 3 digits = Day of year

### Gender Detection

| Day Code  | Gender |
| --------- | ------ |
| 001 - 366 | Male   |
| 501 - 866 | Female |

For female NIC numbers, 500 is subtracted from the day code before calculating the birth date.

## Project Structure

```text
Sri-lanka-nic-decoder/
│
├── sri_lanka_nic_card_reader_1.6.py
├── README.md
└── screenshot.png
```

## Fonts

This project uses the following fonts:

* Ink Free
* Arial
* Consolas
* Fixedsys

If Ink Free is not installed on the system, the operating system may substitute another font automatically.

## Disclaimer

This tool is intended for educational and informational purposes only. It does not verify NIC numbers against official government databases.

## Author

Tharupathi

GitHub: https://github.com/minecrafttharupathi-rgb

Email: mailto:minecraft.tharupathi@gmail.com

## License

This project is licensed under the MIT License.
