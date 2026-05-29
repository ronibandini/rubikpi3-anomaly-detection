<img width="1118" height="788" alt="RubikPi" src="https://github.com/user-attachments/assets/1ca39476-0e59-4f1b-a226-d9a25bae058a" />

# RUBIK Pi 3 Anomaly Detection with Edge Impulse and n8n

![RubikPi](https://github.com/ronibandini/rubikpi3-anomaly-detection/blob/main/rubikpi.png)

Visual anomaly detection running on the **RUBIK Pi 3**, powered by **Edge Impulse** and integrated with **n8n** for automated logging, reporting, and workflow orchestration.

This project demonstrates how to deploy an Edge Impulse anomaly detection model on a RUBIK Pi 3, monitor objects through a USB camera, and automatically send anomaly scores to an n8n workflow whenever a configurable threshold is exceeded.

## Features

* Real-time visual anomaly detection
* Edge deployment using Edge Impulse Linux Runner
* USB camera image acquisition
* Automated anomaly reporting through n8n webhooks
* Historical anomaly logging
* Email notifications and graph generation
* Runs entirely on-device

## Architecture

```text
USB Camera
     │
     ▼
RUBIK Pi 3
     │
     ▼
Edge Impulse Model
     │
 Anomaly Score
     │
     ▼
Python Runner
     │
Webhook POST
     │
     ▼
n8n Workflow
     │
 ├── Data Storage
 ├── Graph Generation
 └── Email Reports
```

## Hardware Requirements

* RUBIK Pi 3
* USB Webcam
* Power Supply (3A recommended)
* Active Cooler (recommended for continuous operation)

## Software Requirements

* Ubuntu running on RUBIK Pi 3
* Python 3
* Edge Impulse Linux Runner
* n8n account or self-hosted instance

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ronibandini/rubikpi3-anomaly-detection.git
cd rubikpi3-anomaly-detection
```

### 2. Install dependencies

```bash
pip3 install requests
```

### 3. Install Edge Impulse Linux Runner

```bash
edge-impulse-linux-runner
```

Authenticate with your Edge Impulse account and select your anomaly detection project.

## Edge Impulse Setup

Create or clone an anomaly detection project in Edge Impulse.

A sample project used for testing is available here:

https://studio.edgeimpulse.com/studio/374008

Train and deploy the model using the Linux (AARCH64 with Qualcomm QNN) target.

## n8n Setup

### Create a Data Table

Create a table containing:

| Field |
| ----- |
| x     |
| y     |
| value |

### Import Workflow

Import the provided workflow:

```text
EI with Rubik Pi 3 upload.json
```

After importing:

1. Open the Webhook node.
2. Copy the Production URL.
3. Save the workflow.
4. Activate it.

## Configuration

Open `runner.py` and modify:

```python
WEBHOOK_URL = "YOUR_N8N_WEBHOOK"
CONFIDENCE_THRESHOLD = 85.0
```

### Threshold

The threshold determines when an anomaly is reported.

Example:

```python
CONFIDENCE_THRESHOLD = 85.0
```

Only anomaly scores above 85% will trigger a webhook request.

## Running

Start the detector:

```bash
python3 runner.py
```

Output example:

```text
Rubik Pi 3 Anomaly Detection with Edge Impulse and n8n

Stop with CTRL-C

Anomaly Score: 12.3
Anomaly Score: 15.8
Anomaly Score: 91.4
Webhook triggered
```

## How It Works

1. Edge Impulse performs inference on images captured from the USB camera.
2. The anomaly score is extracted from the runner output.
3. When the score exceeds the configured threshold:

   * A webhook request is sent to n8n.
   * The score is stored.
   * Reports can be generated automatically.
4. n8n can generate charts and email summaries of detected anomalies.

## Example Use Cases

* Manufacturing quality control
* Visual inspection systems
* Missing component detection
* Packaging verification
* Educational TinyML demonstrations
* Edge AI prototyping

## Files

| File                             | Description                   |
| -------------------------------- | ----------------------------- |
| `runner.py`                      | Main anomaly detection runner |
| `EI with Rubik Pi 3 upload.json` | n8n workflow                  |
| `README.md`                      | Documentation                 |

## Tutorial

Full step-by-step tutorial:

https://docs.edgeimpulse.com/projects/expert-network/anomaly-detection-n8n-rubik-pi

## Demonstration

Video:

https://www.youtube.com/shorts/6sRBoeaxIbk

## License

GPL-3.0

## Author

**Roni Bandini**

* GitHub: https://github.com/ronibandini
* LinkedIn: https://www.linkedin.com/in/ronibandini/

## Acknowledgments

* Edge Impulse
* Thundercomm RUBIK Pi Team
* n8n

Built for exploring practical Edge AI workflows combining machine learning inference, automation, and real-time anomaly reporting.

