import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import json
import os

class ImageExcelConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image and Excel Converter")
        
        # Create and place widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Button to select and process images
        self.image_button = tk.Button(self.root, text="Select Images", command=self.select_images)
        self.image_button.pack(pady=10)
        
        # Option to save extensions or not
        self.ext_var = tk.IntVar(value=1)
        self.ext_check = tk.Checkbutton(self.root, text="Include file extensions", variable=self.ext_var)
        self.ext_check.pack(pady=5)
        
        # Button to select and process Excel to JSON
        self.excel_to_json_button = tk.Button(self.root, text="Excel to JSON", command=self.select_excel_to_json)
        self.excel_to_json_button.pack(pady=10)
        
        # Button to select and process JSON to Excel
        self.json_to_excel_button = tk.Button(self.root, text="JSON to Excel", command=self.select_json_to_excel)
        self.json_to_excel_button.pack(pady=10)
        
        # Text widget to display log
        self.log_text = tk.Text(self.root, height=10, width=50)
        self.log_text.pack(pady=10)
    
    def select_images(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.gif")])
        if file_paths:
            self.process_images(file_paths)
    
    def process_images(self, file_paths):
        save_ext = self.ext_var.get() == 1
        log_entries = []
        for path in file_paths:
            file_name = os.path.basename(path)
            if not save_ext:
                file_name = os.path.splitext(file_name)[0]
            log_entries.append(file_name)
        
        # Save names to a text file
        with open("image_names.txt", "w") as file:
            for entry in log_entries:
                file.write(entry + "\n")
        
        self.log_text.insert(tk.END, "Image names saved to image_names.txt\n")
    
    def select_excel_to_json(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx"), ("Excel Files", "*.xls")])
        if file_path:
            self.convert_excel_to_json(file_path)
    
    def convert_excel_to_json(self, file_path):
        output_file = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if output_file:
            # Load Excel file
            df = pd.read_excel(file_path)
            df.to_json(output_file, orient="records", lines=True)
            self.log_text.insert(tk.END, f"Excel file converted to JSON: {output_file}\n")
    
    def select_json_to_excel(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if file_path:
            self.convert_json_to_excel(file_path)
    
    def convert_json_to_excel(self, file_path):
        output_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        if output_file:
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    # Handle possible extra data in JSON
                    json_objects = []
                    while content:
                        try:
                            data, index = self.extract_json(content)
                            json_objects.append(data)
                            content = content[index:].strip()
                        except json.JSONDecodeError:
                            break
                
                # Flatten the list of JSON objects if necessary
                if len(json_objects) == 1:
                    data = json_objects[0]
                else:
                    data = [item for sublist in json_objects for item in (sublist if isinstance(sublist, list) else [sublist])]

                # Create DataFrame and save to Excel
                if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                    df = pd.DataFrame(data)
                    df.to_excel(output_file, index=False)
                    self.log_text.insert(tk.END, f"JSON file converted to Excel: {output_file}\n")
                else:
                    messagebox.showerror("Error", "JSON file format is invalid. Expected a list of dictionaries.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
    
    def extract_json(self, content):
        try:
            data, index = json.JSONDecoder().raw_decode(content)
            return data, index
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Unable to decode JSON from content", content, 0)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageExcelConverterApp(root)
    root.mainloop()
