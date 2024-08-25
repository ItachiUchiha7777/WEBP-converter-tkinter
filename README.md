# Image Converter

**Image Converter** is a graphical tool built with Tkinter and Pillow that converts image files to WebP format. The application supports various image formats and allows you to adjust the compression quality. Additionally, it extracts and saves EXIF metadata from the images.

## Features

- Convert images to WebP format.
- Adjustable compression quality via a slider.
- Extract and save EXIF metadata to a JSON file.
- User-friendly interface for folder selection.

## Requirements

- Python 3.x
- Pillow (`PIL` fork)
- Tkinter (usually included with Python standard library)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ItachiUchiha7777/WEBP-converter-tkinter.git
    cd WEBP-converter-tkinter
    ```

2. **Install the required libraries**:
    ```bash
    pip install pillow
    ```

## Usage

1. **Run the application**:
    ```bash
    python main.py
    ```

2. **Select the input folder**: Click "Browse" next to the "Input Folder" field and choose the folder containing the images you want to convert.

3. **Select the output folder**: Click "Browse" next to the "Output Folder" field and choose the folder where you want the converted images to be saved.

4. **Adjust compression quality**: Use the slider to set the desired quality (0 to 100).

5. **Convert images**: Click the "Convert" button to start the conversion process. Converted images will be saved in the WebP format in the output folder, and metadata will be saved in `metadata.json`.

## Example

1. Select an input folder with image files.
2. Choose an output folder.
3. Adjust the compression quality as desired.
4. Click "Convert" to process the images.

## Troubleshooting

- **Error converting image**: Ensure that the input folder contains supported image formats (JPG, JPEG, PNG, BMP, TIFF).
- **Missing libraries**: Install required libraries using `pip install pillow`.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a Pull Request.

## Contact

For any questions or issues, please contact [Your Name](mailto:rohitgusain792@gmail.com).

