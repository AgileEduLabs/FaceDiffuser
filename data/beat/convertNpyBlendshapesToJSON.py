import numpy as np
import json
import os

def npy_to_json(npy_path, output_json_path):
    # Load the npy file
    data = np.load(npy_path)

    # Create the JSON structure
    anim_data = {
        "names": [
            "browDownLeft", "browDownRight", "browInnerUp", "browOuterUpLeft", "browOuterUpRight", "cheekPuff", 
            "cheekSquintLeft", "cheekSquintRight", "eyeBlinkLeft", "eyeBlinkRight", "eyeLookDownLeft", 
            "eyeLookDownRight", "eyeLookInLeft", "eyeLookInRight", "eyeLookOutLeft", "eyeLookOutRight", 
            "eyeLookUpLeft", "eyeLookUpRight", "eyeSquintLeft", "eyeSquintRight", "eyeWideLeft", "eyeWideRight", 
            "jawForward", "jawLeft", "jawOpen", "jawRight", "mouthClose", "mouthDimpleLeft", "mouthDimpleRight", 
            "mouthFrownLeft", "mouthFrownRight", "mouthFunnel", "mouthLeft", "mouthLowerDownLeft", 
            "mouthLowerDownRight", "mouthPressLeft", "mouthPressRight", "mouthPucker", "mouthRight", 
            "mouthRollLower", "mouthRollUpper", "mouthShrugLower", "mouthShrugUpper", "mouthSmileLeft", 
            "mouthSmileRight", "mouthStretchLeft", "mouthStretchRight", "mouthUpperUpLeft", "mouthUpperUpRight", 
            "noseSneerLeft", "noseSneerRight"
        ],
        "frames": []
    }

    # Recreate frames with weights
    for idx, frame in enumerate(data):
        frame_data = {
            "weights": frame.tolist(),
            "time": idx * (1/30),  # Assuming 30 FPS
            "rotation": []
        }
        anim_data["frames"].append(frame_data)

    # Save the JSON to the output path
    with open(output_json_path, 'w') as f:
        json.dump(anim_data, f, indent=4)

if __name__ == '__main__':
    npy_path = 'test_beat_1_condition_2.npy'
    output_json_path = 'output_json_file.json'

    npy_to_json(npy_path, output_json_path)