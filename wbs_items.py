wbs_structure = {
    "T.A.I.L.S": {
        "Management": {
            "Documentation": {
                "Project Plan": {
                    "Set up repositories and AGILE board": {},
                    "Project Approval": {},
                },
                "Technical Specifications": {
                    "Hardware Specs": {},
                    "Software Architecture": {},
                    "Communication Protocols": {},
                },
            },
            "Deliverables": {
                "Timeline": {
                    "Initial Draft": "By Jan 10, 2025",
                    "Final Submission": "By Feb 24, 2025",
                    "Interim Updates": {},
                    "Final Demo": {},
                },
                "Milestones": {
                    "Midterm Presentation": "Feb 14, 2025",
                    "Final Presentation": "Apr 1, 2025",
                },
                "Final Report": {
                    "Midterm Draft": "Due Feb 10, 2025",
                    "Final Draft": "Due Apr 1, 2025",
                },
            },
            "Funding": {
                "Budget Allocation": {
                    "Cost Estimation": {},
                    "Resource Cost Breakdown": {},
                },
                "Grant Applications": {
                    "Identify Funding Sources": {},
                    "Prepare Application Documents": {},
                    "EEF Application": {},
                },
                "Resource Procurement": {
                    "Component Sourcing": {
                        "Drone Hardware": {},
                        "Raspberry Pi and Sensors": {},
                        "Ground Station Components": {},
                        "Cloud infrastructure": {},
                    },
                },
            },
        },
        "Design": {
            "On Board Inference System": {
                "Object Detection Setup": {
                    "Evaluate Object Detection Libraries": {},
                    "Benchmark Inference Performance": {},
                    "Optimize Model for Real-Time Processing": {},
                },
                "Communication Protocols": {
                    "Design LoRa Communication Scheme (915 MHz)": {},
                    "Implement Offline Data Transmission": {},
                },
                "Power Management": {
                    "Battery Pack Integration": {},
                    "Power Distribution Design": {},
                    "Thermal Management Considerations": {},
                },
            },
            "Ground Station Design": {
                "Arduino Hardware Layout": {
                    "Circuit Design": {},
                    "Component Placement": {},
                },
                "Radio Transceiver Integration": {
                    "915 MHz Radio Setup": {},
                    "BLE Module Configuration": {},
                },
                "Power Supply and Enclosure": {
                    "Power Management Design": {},
                    "Enclosure and Environmental Protection": {},
                },
                "Prototype Development": {
                    "Initial Breadboarding": {},
                    "Iterative Design Improvements": {},
                },
            },
        },
        "Development": {
            "Software": {
                "Frontend": {
                    "Map Interface": {
                        "Design Real-Time Map Display": {},
                        "Offline Map Caching": {},
                    },
                    "Object Location Visualization": {
                        "Integrate GPS Data Overlay": {},
                        "Dynamic POI Highlighting": {},
                    },
                    "User Controls and Settings": {
                        "Search Subject Selection": {},
                        "Flight Path Configuration": {},
                        "Offline Mode Toggle": {},
                    },
                    "User Login and Authentication": {
                        "Implement Secure Login": {},
                        "Session Management": {},
                    },
                    "UI/UX Design": {
                        "User Journey Mapping": {},
                        "Prototype Wireframes": {},
                        "User Testing and Iteration": {},
                    },
                },
                "Backend": {
                    "Database Integration": {
                        "Design Data Models for GPS and Detection": {},
                        "Implement Offline Data Storage Mechanism": {},
                        "Database Sync Strategy": {},
                    },
                    "GPS Data Processing": {
                        "Develop Flask API Endpoints": {},
                        "Implement Data Validation": {},
                        "Real-Time Processing of Incoming Data": {},
                    },
                    "Object Detection Pipeline": {
                        "Integrate Camera Feed with Detection Model": {},
                        "Buffer and Process Inference Data": {},
                        "Handle Detection Anomalies": {},
                    },
                },
                "AI System": {
                    "Select an Object Detection Model": {
                        "Evaluate YOLO vs MobileNet": {},
                        "Benchmark on Raspberry Pi Zero": {},
                    },
                    "Integrate the AI Model into the Drone's Camera Feed Analysis System": {
                        "Develop Inference Pipeline": {},
                        "Optimize for Low-Power Operation": {},
                    },
                    "Record GPS Location of Drone to Backend When POI Is Detected": {
                        "Synchronize Inference and GPS Data": {},
                        "Implement Data Timestamping": {},
                    },
                },
            },
            "Hardware": {
                "Drone Assembly": {
                    "Mounting": {
                        "Design Custom Mount": {},
                        "Test Vibration Dampening": {},
                    },
                },
                "Raspberry Pi Setup": {
                    "OS Configuration": {
                        "Install and Configure Raspberry Pi OS": {},
                        "Set Up Auto-Start Services": {},
                    },
                    "Peripheral Connections": {
                        "Connect Camera, GPS, and LoRa Modules": {},
                        "Verify Driver Integrations": {},
                    },
                },
                "Hardware Setup": {
                    "Write Unit Tests for Hardware Interfaces": {},
                    "Validate GPS Accuracy and POI Mapping": {},
                    "Test Object Detection System Independent of Drone": {},
                    "Test Drone Capabilities in Controlled Environments": {},
                    "Conduct Field Tests in Real-World Conditions": {},
                },
                "Drone Procurement": {
                    "Choose drone": {},
                    "Purchase Drone": {},
                    "Obtain Drone License and Regulatory Approvals": {},
                },
                "Ground Station Assembly": {
                    "Arduino Integration": {
                        "Develop Firmware for Data Reception": {},
                        "Implement BLE Communication": {},
                    },
                    "Radio and BLE Module Setup": {
                        "Configure 915 MHz Radio": {},
                        "Test BLE Connectivity": {},
                    },
                    "Power Supply Setup": {
                        "Design Power Circuit for Arduino": {},
                        "Test Battery Life and Reliability": {},
                    },
                    "Enclosure Assembly": {
                        "Design Protective Enclosure": {},
                        "Prototype and Iterate Design": {},
                    },
                },
            },
        },
        "Integration": {
            "Drone and Raspberry Pi": {
                "Latency Analysis": {
                    "Measure Communication Delay": {},
                    "Optimize Data Transmission": {},
                },
                "Error Handling Implementation": {
                    "Develop Failover Protocols": {},
                    "Simulate Connection Interruptions": {},
                },
                "AI Model and Camera Feed": {
                    "Synchronize Data Streams": {},
                    "Implement Buffering Mechanisms": {},
                },
            },
            "End-to-End System": {
                "Object Detection Validation": {
                    "Cross-Verify AI Output with Manual Annotations": {},
                    "Calibrate Detection Sensitivity": {},
                },
                "GPS Location Accuracy Testing": {
                    "Compare Drone GPS Data with Baseline Measurements": {},
                    "Test in Varied Environmental Conditions": {},
                },
                "Database and Frontend Sync": {
                    "Test Data Sync Post-Offline Mode": {},
                    "Validate Data Integrity During Transfer": {},
                },
            },
        },
        "Testing": {
            "Software Testing": {
                "Frontend Testing": {
                    "UI Responsiveness": {
                        "Cross-Device Testing": {},
                        "Offline Mode Verification": {},
                    },
                    "Interactive Map Accuracy": {
                        "Real-Time Update Testing": {},
                        "Error Simulation Scenarios": {},
                    },
                },
                "Backend Testing": {
                    "Data Storage Reliability": {
                        "Stress Test Database Operations": {},
                        "Simulate Offline Data Accumulation": {},
                    },
                    "GPS Data Validation": {
                        "Edge Case Data Inputs": {},
                        "Automated Data Verification Scripts": {},
                    },
                    "Object Detection Results": {
                        "Benchmark Against Ground Truth": {},
                        "Analyze False Positives/Negatives": {},
                    },
                },
            },
            "Hardware Testing": {
                "Drone Flight Testing": {
                    "Stability and Control": {
                        "Test in Windy Conditions": {},
                        "Maneuverability Assessments": {},
                    },
                    "GPS Signal Quality": {
                        "Test Signal Under Flight Conditions": {},
                        "Measure Signal Dropouts": {},
                    },
                },
                "System Performance": {
                    "Power Consumption": {
                        "Monitor Battery Life": {},
                        "Test Under Load Conditions": {},
                    },
                    "Communication Robustness": {
                        "Test LoRa Range and Reliability": {},
                        "Simulate RF Interference": {},
                    },
                },
                "Ground Station Testing": {
                    "Arduino Communication Test": {
                        "Verify Data Reception": {},
                        "Test BLE Signal Strength": {},
                    },
                    "Enclosure and Environmental Testing": {
                        "Assess Durability": {},
                        "Temperature and Humidity Testing": {},
                    },
                },
            },
        },
    }
}
