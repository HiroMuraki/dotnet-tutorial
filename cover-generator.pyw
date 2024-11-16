from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
from dataclasses import dataclass
from typing import Tuple
from typing import List


@dataclass
class BackgroundOptions:
    width: int
    height: int
    background_color: str


@dataclass
class TextOptions:
    text: str
    font_family: str
    font_color: str
    font_size: int
    position: Tuple[int, int]


class ImageGenerator:
    @staticmethod
    def generate_cover(
            texts: List[TextOptions],
            background: BackgroundOptions,
            save_to: str) -> None:
        image = Image.new("RGB", (background.width, background.height), background.background_color)  # noqa
        draw = ImageDraw.Draw(image)

        for text in texts:
            try:
                font = ImageFont.truetype(text.font_family, text.font_size)
            except IOError:
                print("Font not found. Falling back to default font.")
                font = ImageFont.load_default()
            # Draw the title text
            draw.text(text.position, text.text, font=font, fill=text.font_color)  # noqa

        # Save the image to the specified path
        image.save(save_to)


def generate_cover(subtitle_text: str):
    subtitle_text = subtitle_text.removeprefix("【.NET C#基础】")

    background = BackgroundOptions(
        width=1280,
        height=720,
        background_color="#2E2E2E",
    )

    title = TextOptions(
        text=".NET C#基础",
        position=(205, 190),
        font_family="C:\\Windows\\Fonts\\msyhbd.ttc",
        font_color="#FFFFFF",
        font_size=79,
    )

    subtitle = TextOptions(
        text=subtitle_text,
        position=(220, 335),
        font_family="C:\\Windows\\Fonts\\msyhbd.ttc",
        font_color="#F25454",
        font_size=110,
    )

    ImageGenerator.generate_cover(
        texts=[title, subtitle],
        background=background,
        save_to=f"【.NET C#基础】{subtitle_text}.png"
    )


def main():
    # Create the main window
    root = tk.Tk()
    root.title("Cover generator")

    # Set window dimensions
    window_width, window_height = 400, 200

    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate x and y coordinates for the window to be centered
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Set the geometry of the window
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Subtitle label
    subtitle_label = tk.Label(root, text="Subtitle:")
    subtitle_label.pack(pady=10)

    # Subtitle entry field
    subtitle_entry = tk.Entry(root, width=50)
    subtitle_entry.pack(pady=10)

    # Button to trigger foo function
    def on_button_click():
        subtitle = subtitle_entry.get()  # Get the text from the entry field
        generate_cover(subtitle)  # Call the foo function with the entered text

    generate_button = tk.Button(
        root, text="Click to Generate", command=on_button_click)
    generate_button.pack(pady=20)

    # Run the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        input()
    finally:
        pass
