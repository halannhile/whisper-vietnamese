import os
import pandas as pd

def generate_metadata_excel(folder_path, excel_filename):
    data = {'file_name': [], 'transcription': []}

    for filename in os.listdir(folder_path):
        if filename.endswith(".wav"):
            audio_file_path = os.path.join(folder_path, filename)
            transcription_file_path = os.path.join(folder_path, f"{os.path.splitext(filename)[0]}.txt")

            if os.path.exists(transcription_file_path):
                with open(transcription_file_path, 'r', encoding='utf-8') as transcription_file:
                    transcription = transcription_file.read()

                data['file_name'].append(filename)
                data['transcription'].append(transcription)
            else:
                print(f"Warning: No corresponding TXT file found for {filename}")

    df = pd.DataFrame(data)
    df.to_excel(excel_filename, index=False)

# Example usage for the train folder
train_folder_path = "./data/all/"
train_excel_filename = "./data/all/metadata.xlsx"
generate_metadata_excel(train_folder_path, train_excel_filename)
