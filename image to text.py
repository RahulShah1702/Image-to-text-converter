import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import pytesseract
import os

# Configure Tesseract path if necessary
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class ImageToTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Text Generator")
        self.root.geometry("800x700")
        self.root.config(bg="#f4f4f4")

        # Initial theme state
        self.current_theme = "light"

        # Initialize ttk style
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 12), padding=10, relief="flat")

        # Main Title
        self.title_label = ttk.Label(root, text="Image to Text Generator", font=("Arial", 20, "bold"))
        self.title_label.pack(pady=10)

        # Image Display Area
        self.image_frame = tk.Frame(root, bg="#f4f4f4", relief=tk.RIDGE, bd=2)
        self.image_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=False)
        self.image_label = tk.Label(self.image_frame, bg="#ddd", width=50, height=20, text="Drag & Drop an Image Here", anchor="center")
        self.image_label.pack(fill=tk.BOTH, expand=True)

        # Button Frame
        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(pady=20)

        # Separate each button with grid layout with padding
        self.open_button = ttk.Button(self.button_frame, text="Open Image", command=self.open_image)
        self.open_button.grid(row=0, column=0, padx=10, pady=5)

        self.extract_button = ttk.Button(self.button_frame, text="Extract Text", command=self.extract_text)
        self.extract_button.grid(row=0, column=1, padx=10, pady=5)

        self.copy_button = ttk.Button(self.button_frame, text="Copy", command=self.copy_text)
        self.copy_button.grid(row=0, column=2, padx=10, pady=5)

        self.clear_button = ttk.Button(self.button_frame, text="Clear", command=self.clear_text)
        self.clear_button.grid(row=0, column=3, padx=10, pady=5)

        self.save_button = ttk.Button(self.button_frame, text="Save to File", command=self.save_to_file)
        self.save_button.grid(row=0, column=4, padx=10, pady=5)

        self.mode_button = ttk.Button(self.button_frame, text="Toggle Theme", command=self.toggle_theme)
        self.mode_button.grid(row=0, column=5, padx=10, pady=5)

        # Text Output Area
        self.text_output = tk.Text(root, wrap=tk.WORD, height=15, font=("Arial", 12), padx=10, pady=10)
        self.text_output.pack(pady=10, fill=tk.BOTH, expand=True)
        self.text_output.bind("<<Modified>>", self.update_char_count)

        # Character Count
        self.char_count_label = ttk.Label(root, text="Character Count: 0", font=("Arial", 12))
        self.char_count_label.pack(pady=5)

        # Apply initial theme styling
        self.apply_theme_styles()

    def open_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
        if not file_path:
            return
        self.load_image(file_path)

    def load_image(self, file_path):
        try:
            img = Image.open(file_path)
            img.thumbnail((400, 400))
            img_tk = ImageTk.PhotoImage(img)
            self.image_label.config(image=img_tk, text="")
            self.image_label.image = img_tk
            self.image_label.file_path = file_path
        except Exception as e:
            messagebox.showerror("Error", f"Could not open image: {e}")

    def extract_text(self):
        if not hasattr(self.image_label, "file_path"):
            messagebox.showwarning("No Image", "Please select an image first!")
            return
        try:
            extracted_text = pytesseract.image_to_string(Image.open(self.image_label.file_path))
            self.text_output.delete("1.0", tk.END)
            self.text_output.insert(tk.END, extracted_text)
        except Exception as e:
            messagebox.showerror("Error", f"Could not extract text: {e}")

    def copy_text(self):
        text = self.text_output.get("1.0", tk.END).strip()
        if text:
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            self.root.update()
            messagebox.showinfo("Copied", "Text copied to clipboard!")
        else:
            messagebox.showwarning("No Text", "No text to copy!")

    def clear_text(self):
        self.text_output.delete("1.0", tk.END)
        self.char_count_label.config(text="Character Count: 0")

    def save_to_file(self):
        text = self.text_output.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("No Text", "No text to save!")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if not file_path:
            return
        try:
            with open(file_path, "w") as file:
                file.write(text)
            messagebox.showinfo("Saved", f"Text saved to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save text: {e}")

    def toggle_theme(self):
        if self.current_theme == "light":
            self.current_theme = "dark"
        elif self.current_theme == "dark":
            self.current_theme = "dark_blue"
        elif self.current_theme == "dark_blue":
            self.current_theme = "dark_red"
        elif self.current_theme == "dark_red":
            self.current_theme = "dark_green"
        elif self.current_theme == "dark_green":
            self.current_theme = "dark_grey"
        else:
            self.current_theme = "light"
        self.apply_theme_styles()

    def apply_theme_styles(self):
        if self.current_theme == "light":
            bg_color = "#f4f4f4"
            fg_color = "#000"
            button_bg_color = "#007acc"
            button_fg_color = "#000"
            text_bg_color = "#fff"
            text_fg_color = "#000"
        elif self.current_theme == "dark":
            bg_color = "#121212"
            fg_color = "#fff"
            button_bg_color = "#444"
            button_fg_color = "#000"
            text_bg_color = "#333"
            text_fg_color = "#fff"
        elif self.current_theme == "dark_blue":
            bg_color = "#001f3d"
            fg_color = "#fff"
            button_bg_color = "#003f6b"
            button_fg_color = "#000"
            text_bg_color = "#001f3d"
            text_fg_color = "#fff"
        elif self.current_theme == "dark_red":
            bg_color = "#2a0000"
            fg_color = "#fff"
            button_bg_color = "#5c0000"
            button_fg_color = "#000"
            text_bg_color = "#2a0000"
            text_fg_color = "#fff"
        elif self.current_theme == "dark_green":
            bg_color = "#0a2a2a"
            fg_color = "#fff"
            button_bg_color = "#0f4f4f"
            button_fg_color = "#000"
            text_bg_color = "#0a2a2a"
            text_fg_color = "#fff"
        elif self.current_theme == "dark_grey":
            bg_color = "#3d3d3d"
            fg_color = "#fff"
            button_bg_color = "#595959"
            button_fg_color = "#000"
            text_bg_color = "#3d3d3d"
            text_fg_color = "#fff"

        # Update the background and foreground colors for each widget
        self.root.config(bg=bg_color)
        self.title_label.config(background=bg_color, foreground=fg_color)
        self.image_frame.config(bg=bg_color)
        self.char_count_label.config(background=bg_color, foreground=fg_color)
        self.text_output.config(bg=text_bg_color, fg=text_fg_color)

        # Update button styles (background and text color) based on the theme
        self.style.configure("TButton",
                             background=button_bg_color,
                             foreground=button_fg_color,
                             relief="flat")
        self.open_button.config(style="TButton")
        self.extract_button.config(style="TButton")
        self.copy_button.config(style="TButton")
        self.clear_button.config(style="TButton")
        self.save_button.config(style="TButton")
        self.mode_button.config(style="TButton")

    def update_char_count(self, event=None):
        text = self.text_output.get("1.0", tk.END).strip()
        self.char_count_label.config(text=f"Character Count: {len(text)}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToTextApp(root)
    root.mainloop()
