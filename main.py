import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import json
import os

class ConvertidorDeArchivosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertidor de Archivos")

        # Crear y colocar widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Botón para seleccionar y procesar Excel a JSON
        self.excel_to_json_button = tk.Button(self.root, text="Excel a JSON", command=self.select_excel_to_json)
        self.excel_to_json_button.pack(pady=10)
        
        # Botón para seleccionar y procesar JSON a Excel
        self.json_to_excel_button = tk.Button(self.root, text="JSON a Excel", command=self.select_json_to_excel)
        self.json_to_excel_button.pack(pady=10)
        
        # Botón para seleccionar y procesar CSV a Excel
        self.csv_to_excel_button = tk.Button(self.root, text="CSV a Excel", command=self.select_csv_to_excel)
        self.csv_to_excel_button.pack(pady=10)
        
        # Botón para seleccionar y procesar Excel a CSV
        self.excel_to_csv_button = tk.Button(self.root, text="Excel a CSV", command=self.select_excel_to_csv)
        self.excel_to_csv_button.pack(pady=10)
        
        # Botón para seleccionar y procesar CSV a JSON
        self.csv_to_json_button = tk.Button(self.root, text="CSV a JSON", command=self.select_csv_to_json)
        self.csv_to_json_button.pack(pady=10)
        
        # Botón para seleccionar y procesar JSON a CSV
        self.json_to_csv_button = tk.Button(self.root, text="JSON a CSV", command=self.select_json_to_csv)
        self.json_to_csv_button.pack(pady=10)
        
        # Widget de texto para mostrar el registro
        self.log_text = tk.Text(self.root, height=15, width=50)
        self.log_text.pack(pady=10)
    
    def select_excel_to_json(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx;*.xls")])
        if file_path:
            self.convert_excel_to_json(file_path)
    
    def convert_excel_to_json(self, file_path):
        output_file = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivos JSON", "*.json")])
        if output_file:
            try:
                # Cargar archivo Excel
                df = pd.read_excel(file_path)
                df.to_json(output_file, orient="records", lines=True)
                self.log_text.insert(tk.END, f"Archivo Excel convertido a JSON: {output_file}\n")
            except Exception as e:
                messagebox.showerror("Error", str(e))
    
    def select_json_to_excel(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.json")])
        if file_path:
            self.convert_json_to_excel(file_path)
    
    def convert_json_to_excel(self, file_path):
        output_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Archivos Excel", "*.xlsx")])
        if output_file:
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    # Manejar datos adicionales en JSON
                    json_objects = []
                    while content:
                        try:
                            data, index = self.extract_json(content)
                            json_objects.append(data)
                            content = content[index:].strip()
                        except json.JSONDecodeError:
                            break

                # Aplanar la lista de objetos JSON si es necesario
                if len(json_objects) == 1:
                    data = json_objects[0]
                else:
                    data = [item for sublist in json_objects for item in (sublist if isinstance(sublist, list) else [sublist])]

                # Crear DataFrame y guardar en Excel
                if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                    df = pd.DataFrame(data)
                    df.to_excel(output_file, index=False)
                    self.log_text.insert(tk.END, f"Archivo JSON convertido a Excel: {output_file}\n")
                else:
                    messagebox.showerror("Error", "Formato de archivo JSON inválido. Se esperaba una lista de diccionarios.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
    
    def extract_json(self, content):
        try:
            data, index = json.JSONDecoder().raw_decode(content)
            return data, index
        except json.JSONDecodeError:
            raise json.JSONDecodeError("No se pudo decodificar JSON del contenido", content, 0)

    def select_csv_to_excel(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
        if file_path:
            self.convert_csv_to_excel(file_path)
    
    def convert_csv_to_excel(self, file_path):
        output_file = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Archivos Excel", "*.xlsx")])
        if output_file:
            try:
                df = pd.read_csv(file_path)
                df.to_excel(output_file, index=False)
                self.log_text.insert(tk.END, f"Archivo CSV convertido a Excel: {output_file}\n")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def select_excel_to_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx;*.xls")])
        if file_path:
            self.convert_excel_to_csv(file_path)
    
    def convert_excel_to_csv(self, file_path):
        output_file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Archivos CSV", "*.csv")])
        if output_file:
            try:
                df = pd.read_excel(file_path)
                df.to_csv(output_file, index=False)
                self.log_text.insert(tk.END, f"Archivo Excel convertido a CSV: {output_file}\n")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def select_csv_to_json(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos CSV", "*.csv")])
        if file_path:
            self.convert_csv_to_json(file_path)
    
    def convert_csv_to_json(self, file_path):
        output_file = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("Archivos JSON", "*.json")])
        if output_file:
            try:
                df = pd.read_csv(file_path)
                df.to_json(output_file, orient="records", lines=True)
                self.log_text.insert(tk.END, f"Archivo CSV convertido a JSON: {output_file}\n")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def select_json_to_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.json")])
        if file_path:
            self.convert_json_to_csv(file_path)
    
    def convert_json_to_csv(self, file_path):
        output_file = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Archivos CSV", "*.csv")])
        if output_file:
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    # Manejar datos adicionales en JSON
                    json_objects = []
                    while content:
                        try:
                            data, index = self.extract_json(content)
                            json_objects.append(data)
                            content = content[index:].strip()
                        except json.JSONDecodeError:
                            break

                if len(json_objects) == 1:
                    data = json_objects[0]
                else:
                    data = [item for sublist in json_objects for item in (sublist if isinstance(sublist, list) else [sublist])]

                # Crear DataFrame y guardar en CSV
                if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                    df = pd.DataFrame(data)
                    df.to_csv(output_file, index=False)
                    self.log_text.insert(tk.END, f"Archivo JSON convertido a CSV: {output_file}\n")
                else:
                    messagebox.showerror("Error", "Formato de archivo JSON inválido. Se esperaba una lista de diccionarios.")
            except Exception as e:
                messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = ConvertidorDeArchivosApp(root)
    root.mainloop()
