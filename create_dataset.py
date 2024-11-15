import os
import shutil

# Paths
original_data_path = "AtoZ_3.1"
target_data_path = "data"

# Mapping from letter to class
class_mapping = {
    'A': 0, 'E': 0, 'M': 0, 'N': 0, 'S': 0, 'T': 0,
    'B': 1, 'D': 1, 'F': 1, 'I': 1, 'U': 1, 'V': 1, 'K': 1, 'R': 1, 'W': 1,
    'C': 2, 'O': 2,
    'G': 3, 'H': 3,
    'L': 4,
    'P': 5, 'Q': 5, 'Z': 5,
    'X': 6,
    'Y': 7, 'J': 7
}

for i in range(8):
    os.makedirs(os.path.join(target_data_path, str(i)), exist_ok=True)

# Moving images to the corresponding class folder with unique names
for letter, class_id in class_mapping.items():
    letter_folder = os.path.join(original_data_path, letter)
    target_folder = os.path.join(target_data_path, str(class_id))

    if os.path.exists(letter_folder):
        for img_file in os.listdir(letter_folder):
            source_path = os.path.join(letter_folder, img_file)

            # Generating a new unique filename
            new_filename = f"{letter}_{img_file}"
            target_path = os.path.join(target_folder, new_filename)
            shutil.copy(source_path, target_path)

print("Dataset organized successfully.")
