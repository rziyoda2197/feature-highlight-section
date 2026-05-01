import tkinter as tk
from tkinter import ttk

class FeatureHighlightSection:
    def __init__(self, root):
        self.root = root
        self.root.title("Feature Highlight Section")

        # Frame uchun yaratish
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Header uchun yaratish
        self.header = tk.Label(self.frame, text="Feature Highlight Section", font=("Arial", 18))
        self.header.pack(pady=10)

        # Iconlar uchun yaratish
        self.icons = [
            {"icon": "fa fa-star", "text": "Feature 1"},
            {"icon": "fa fa-bell", "text": "Feature 2"},
            {"icon": "fa fa-lock", "text": "Feature 3"},
            {"icon": "fa fa-user", "text": "Feature 4"},
            {"icon": "fa fa-cog", "text": "Feature 5"},
        ]

        # Iconlar uchun loop
        for icon in self.icons:
            # Icon uchun yaratish
            self.icon = tk.Label(self.frame, text=f"<i class='{icon['icon']}'></i>", font=("Arial", 24))
            self.icon.pack(side=tk.LEFT, padx=10)

            # Text uchun yaratish
            self.text = tk.Label(self.frame, text=icon["text"], font=("Arial", 14))
            self.text.pack(side=tk.LEFT, padx=10)

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = FeatureHighlightSection(root)
    root.mainloop()
