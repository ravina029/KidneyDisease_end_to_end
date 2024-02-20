import shutil   #Copy model.h5 from artifacts/training to model folder
import os

# Paths
source_path = 'artifacts/training/model.h5'
destination_folder = 'model'
destination_path = os.path.join(destination_folder, 'model.h5')

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Copy the file
shutil.copy(source_path, destination_path)

print(f"File copied from {source_path} to {destination_path}")
