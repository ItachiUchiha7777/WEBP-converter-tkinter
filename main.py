import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image
from PIL.ExifTags import TAGS


def convert_images():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    compression_quality = compression_quality_slider.get()

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    metadata_dict = {}

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.webp')

            try:
                with Image.open(input_path) as img:
                    # Extract EXIF data
                    exif_data = get_exif_data(input_path)
                    date_taken = exif_data.get("DateTimeOriginal", "Unknown Date") if exif_data else "Unknown Date"
                    
                    # Save the image as WebP
                    img.save(output_path, 'webp', quality=int(compression_quality))

                    # Store metadata
                    metadata_dict[os.path.splitext(filename)[0]] = {
                        "date_taken": date_taken
                    }
            except Exception as e:
                messagebox.showerror("Error", f"Failed to convert {filename}: {e}")

    # Save metadata to a JSON file
    metadata_file = os.path.join(output_folder, "metadata.json")
    with open(metadata_file, 'w') as f:
        json.dump(metadata_dict, f, indent=4)

    messagebox.showinfo("Conversion Complete", "Images have been converted to WebP format. Metadata saved.")

# Function to select input folder
def select_input_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        input_folder_entry.delete(0, tk.END)
        input_folder_entry.insert(0, folder_path)

# Function to select output folder
def select_output_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        output_folder_entry.delete(0, tk.END)
        output_folder_entry.insert(0, folder_path)

# Function to update the compression quality label
def update_quality_label(value):
    quality_label.config(text=f"Compression Quality: {int(value)}")

# Function to get the exif data from an image file
def get_exif_data(image_path):
    try:
        with Image.open(image_path) as img:
            exif_data = img._getexif()
            if exif_data:
                return {TAGS.get(tag, tag): value for tag, value in exif_data.items() if tag in TAGS}
            return {}
    except Exception as e:
        print(f"Error getting EXIF data: {e}")
        return {}

# Create the main window
root = tk.Tk()
root.title("Image Converter")
root.geometry("600x500")  # Updated window size for better appearance

# Change the background color
root.configure(bg="#f5f5f5")

# Create a frame to center the content
center_frame = tk.Frame(root, bg="#ffffff", padx=20, pady=20)
center_frame.pack(expand=True, fill="both")

# Input folder entry
input_label = ttk.Label(center_frame, text="Input Folder:", background="#ffffff", font=("Arial", 12))
input_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
input_folder_entry = ttk.Entry(center_frame, width=40)
input_folder_entry.grid(row=0, column=1, padx=5, pady=5)
input_button = ttk.Button(center_frame, text="Browse", command=select_input_folder)
input_button.grid(row=0, column=2, padx=5, pady=5)

# Output folder entry
output_label = ttk.Label(center_frame, text="Output Folder:", background="#ffffff", font=("Arial", 12))
output_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
output_folder_entry = ttk.Entry(center_frame, width=40)
output_folder_entry.grid(row=1, column=1, padx=5, pady=5)
output_button = ttk.Button(center_frame, text="Browse", command=select_output_folder)
output_button.grid(row=1, column=2, padx=5, pady=5)

# Compression quality slider
compression_quality_label = ttk.Label(center_frame, text="Compression Quality:", background="#ffffff", font=("Arial", 12))
compression_quality_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
compression_quality_slider = ttk.Scale(center_frame, from_=0, to=100, orient=tk.HORIZONTAL)
compression_quality_slider.set(80)  # Default compression quality
compression_quality_slider.grid(row=2, column=1, padx=5, pady=5, columnspan=2)
quality_label = ttk.Label(center_frame, text="Compression Quality: 80", background="#ffffff", font=("Arial", 12))
quality_label.grid(row=3, column=1, padx=5, pady=5, columnspan=2)

# Bind the update_quality_label function to the slider
compression_quality_slider.bind("<Motion>", lambda event: update_quality_label(compression_quality_slider.get()))
compression_quality_slider.bind("<ButtonRelease-1>",
                                lambda event: update_quality_label(compression_quality_slider.get()))

# Convert button
convert_button = ttk.Button(center_frame, text="Convert", command=convert_images, style='TButton')
convert_button.grid(row=4, column=1, padx=5, pady=20, columnspan=2)

# Center the frame in the window
center_frame.place(in_=root, anchor="c", relx=0.5, rely=0.5)

# Styling for ttk Button
style = ttk.Style()
style.configure('TButton', font=("Arial", 12))

root.mainloop()
