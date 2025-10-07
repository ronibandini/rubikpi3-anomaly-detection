# Anomaly Detection with Edge Impulse, n8n and RUBIK Pi 3 
# Roni Bandini @RoniBandini 
# October 2025
# GPL-3.0 license 

import subprocess
import time
import requests
import json

# Runner output file
output_file = open('output.txt', 'w')

print("Rubik Pi 3 Anomaly Detection with Edge Impulse and n8n")
print("Roni Bandini, Oct 2025, Argentina, @RoniBandini")
print("")
print("Stop with CTRL-C")

# Threshold for triggering webhook
CONFIDENCE_THRESHOLD = 85.0

# Edit n8n webhook URL
WEBHOOK_URL = ""

# Launch Impulse Runner with parameters using subprocess, output to file
subprocess.Popen(["edge-impulse-linux-runner"], stdout=output_file)

with open("output.txt", "r") as f:
    lines_seen = set()
    while True:
        line = f.readline()
        if not line:
            time.sleep(1)
            continue

        if "[]" in line:
            print("No detection")

        if "height" in line and "anomaly" in line and line not in lines_seen:

            # Find JSON array start
            json_start = line.find("[")
            if json_start != -1:
                json_str = line[json_start:].strip()
                try:
                    anomalies = json.loads(json_str)   # Parse as list
                    for anomaly in anomalies:
                        confidence = anomaly["value"]
                        x, y = anomaly["x"], anomaly["y"]

                        print("Confidence:", confidence)
                        print(" At X:", x, "Y:", y)

                        # Check threshold
                        if confidence >= CONFIDENCE_THRESHOLD:
                            print("⚡ Triggering webhook (confidence above threshold)")
                            try:
                                payload = {
                                    "label": anomaly["label"],
                                    "confidence": confidence,
                                    "x": x,
                                    "y": y,
                                    "width": anomaly["width"],
                                    "height": anomaly["height"]
                                }
                                r = requests.post(WEBHOOK_URL, json=payload, timeout=5)
                                print("Webhook response:", r.status_code, r.text)
                            except Exception as e:
                                print("Webhook error:", e)

                except json.JSONDecodeError as e:
                    print("JSON decode error:", e)

            lines_seen.add(line)

