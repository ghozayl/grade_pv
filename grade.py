import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        crop_value = int(crop_var.get())
        land_area = int(land_area_entry.get())
        irrigation_value = int(irrigation_var.get())
        water_depth = int(water_depth_entry.get())
        workers = int(workers_entry.get())

        total_power = crop_value + land_area + irrigation_value + water_depth + workers
        cost = total_power * 10

        output_label.config(text=f'Total Power: {total_power}\nCost: {cost}')
    except ValueError:
        output_label.config(text="Please enter valid numeric values.")

# Create main window
root = tk.Tk()
root.title("PV Cost Calculator")

# Create input frame
input_frame = ttk.Frame(root, padding="20")
input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E))

# Crop dropdown
crop_label = ttk.Label(input_frame, text="Crop:")
crop_label.grid(row=0, column=0, sticky=tk.W)
crop_var = tk.StringVar(value="0")
crop_combobox = ttk.Combobox(input_frame, textvariable=crop_var, values=["None", "250 (Date)", "700 (Potato)", "1500 (Tomato)"])
crop_combobox.grid(row=0, column=1, sticky=tk.W)

# Land Area entry
land_area_label = ttk.Label(input_frame, text="Land Area:")
land_area_label.grid(row=1, column=0, sticky=tk.W)
land_area_entry = ttk.Entry(input_frame)
land_area_entry.grid(row=1, column=1, sticky=tk.W)

# Irrigation dropdown
irrigation_label = ttk.Label(input_frame, text="Irrigation:")
irrigation_label.grid(row=2, column=0, sticky=tk.W)
irrigation_var = tk.StringVar(value="0")
irrigation_combobox = ttk.Combobox(input_frame, textvariable=irrigation_var, values=["None", "172000 (Drip (>24h))", "57000 (Regulated (>6h))", "28000 (Sprinkler (>3h))"])
irrigation_combobox.grid(row=2, column=1, sticky=tk.W)

# Water Depth entry
water_depth_label = ttk.Label(input_frame, text="Depth of Water:")
water_depth_label.grid(row=3, column=0, sticky=tk.W)
water_depth_entry = ttk.Entry(input_frame)
water_depth_entry.grid(row=3, column=1, sticky=tk.W)

# Workers entry
workers_label = ttk.Label(input_frame, text="Workers:")
workers_label.grid(row=4, column=0, sticky=tk.W)
workers_entry = ttk.Entry(input_frame)
workers_entry.grid(row=4, column=1, sticky=tk.W)

# Calculate button
calculate_button = ttk.Button(input_frame, text="Calculate", command=calculate)
calculate_button.grid(row=5, columnspan=2)

# Output frame
output_frame = ttk.Frame(root, padding="20")
output_frame.grid(row=1, column=0, sticky=(tk.W, tk.E))

output_label = ttk.Label(output_frame, text="")
output_label.grid(row=0, column=0)

root.mainloop()
