import tkinter as tk
from tkinter import filedialog, Label
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import webbrowser

def get_exif_data(image_path):
    image = Image.open(image_path)
    exif_data = {}
    info = image._getexif()
    if info:
        for tag, value in info.items():
            tag_name = TAGS.get(tag, tag)
            if tag_name == "GPSInfo":
                gps_data = {}
                for key in value:
                    sub_tag = GPSTAGS.get(key, key)
                    gps_data[sub_tag] = value[key]
                exif_data[tag_name] = gps_data
            else:
                exif_data[tag_name] = value
    return exif_data

def get_lat_lon(exif_data):
    if "GPSInfo" in exif_data:
        gps_info = exif_data["GPSInfo"]
        gps_latitude = gps_info.get("GPSLatitude")
        gps_latitude_ref = gps_info.get("GPSLatitudeRef")
        gps_longitude = gps_info.get("GPSLongitude")
        gps_longitude_ref = gps_info.get("GPSLongitudeRef")

        if gps_latitude and gps_longitude and gps_latitude_ref and gps_longitude_ref:
            lat = convert_to_degrees(gps_latitude)
            if gps_latitude_ref != "N":
                lat = 0 - lat

            lon = convert_to_degrees(gps_longitude)
            if gps_longitude_ref != "E":
                lon = 0 - lon

            return lat, lon
    return None, None

def convert_to_degrees(value):
    d = float(value[0])
    m = float(value[1])
    s = float(value[2])
    return d + (m / 60.0) + (s / 3600.0)

def upload_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        exif_data = get_exif_data(file_path)
        exif_text.delete('1.0', tk.END)
        exif_text.insert(tk.END, str(exif_data))
        lat, lon = get_lat_lon(exif_data)
        if lat and lon:
            location = f"{lat}, {lon}"
            location_label.config(text=location)
            copy_button.config(state=tk.NORMAL)
            open_map_button.config(state=tk.NORMAL)
        else:
            location_label.config(text="No GPS data found")
            copy_button.config(state=tk.DISABLED)
            open_map_button.config(state=tk.DISABLED)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(location_label.cget("text"))
    root.update()  # Keeps the clipboard content after the window is closed

def open_in_maps():
    location = location_label.cget("text")
    if location:
        webbrowser.open(f"https://www.google.com/maps?q={location}")

# GUI setup
root = tk.Tk()
root.title("GPS Data Extractor")
root.geometry("600x400")

upload_button = tk.Button(root, text="Upload Image", command=upload_file)
upload_button.pack(pady=20)

location_label = Label(root, text="")
location_label.pack(pady=10)

copy_button = tk.Button(root, text="Copy Location", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack(pady=10)

open_map_button = tk.Button(root, text="Open in Google Maps", command=open_in_maps, state=tk.DISABLED)
open_map_button.pack(pady=10)

exif_text = tk.Text(root, height=10, width=70)
exif_text.pack(pady=20)

root.mainloop()
