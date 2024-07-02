import my_tkinter_app as tk
from my_tkinter_app import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageEnhance


class ImageProcessor:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Viewer")
        self.original_image_label = tk.Label(self.root, text="Original Image")
        self.original_image_label.pack()

        self.original_image = None  # Initialize original_image attribute

        self.selected_effect = tk.StringVar()
        self.selected_effect.set("No Effect")

        effect_menu = tk.OptionMenu(self.root, self.selected_effect, "No Effect", "Grayscale", "Blur", "Drop Shadow")
        effect_menu.pack()

        apply_button = tk.Button(self.root, text="Apply Effect", command=self.apply_and_display_effect)
        apply_button.pack()

    def open_image_and_apply_effect(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])

        if file_path:
            self.original_image = Image.open(file_path)
            self.display_image(self.original_image)

    def display_image(self, image):
        image_tk = ImageTk.PhotoImage(image)
        self.original_image_label.configure(image=image_tk)
        self.original_image_label.image = image_tk

    def apply_effect(self, image, effect):
        if effect == "Grayscale":
            return image.convert("L")
        elif effect == "Blur":
            return image.filter(ImageFilter.BLUR)
        elif effect == "Drop Shadow":
            return self.apply_drop_shadow(image)
        else:
            return image  # Default: No effect

    def apply_drop_shadow(self, image, distance=5, blur_radius=8, transparency=0.7):
        if image is None:
            return None  # Return None if the image is not available

        shadow = Image.new("RGBA", image.size, (0, 0, 0, 0))
        shadow.paste(image, (distance, distance))
        shadow_blur = shadow.filter(ImageFilter.GaussianBlur(blur_radius))
        result = Image.alpha_composite(image.convert("RGBA"), shadow_blur)
        enhancer = ImageEnhance.Brightness(result)
        result = enhancer.enhance(transparency)
        return result

    def apply_and_display_effect(self):
        selected_effect_value = self.selected_effect.get()
        modified_image = self.apply_effect(self.original_image, selected_effect_value)
        self.display_image(modified_image)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessor(root)

    open_button = tk.Button(root, text="Open Image", command=app.open_image_and_apply_effect)
    open_button.pack()

    root.mainloop()
