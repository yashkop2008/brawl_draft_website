import os
from tkinter import Tk, Label, StringVar, OptionMenu, Button, messagebox, Canvas
from PIL import Image, ImageTk
from tkinter import font

# Predefined list of maps with absolute file paths
MAPS = {
    "Canal Grande": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/canal_grande.png",
    "Hideout": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/hideout.png",
    "Shooting Star": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/shooting_star.png",
    "Snake Prairie": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/snake_prairie.png",
    "Center Stage": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/center_stage.png",
    "Pinball Dreams": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/pinball_dreams.png",
    "Sneaky Fields": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/sneaky_fields.png",
    "Triple Dribble": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/triple_dribble.png",
    "Double Swoosh": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/double_swoosh.png",
    "Hard Rock Mine": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/hard_rock_mine.png",
    "Last Stop": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/last_stop.png",
    "Under Mine": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/under_mine.png",
    "Bridge Too Far": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/bridge_too_far.png",
    "Hot Potato": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/hot_potato.png",
    "Kaboom Canyon": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/kaboom_canyon.png",
    "Safe Zone": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/safe_zone.png",
    "Dueling Beetles": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/dueling_beetles.png",
    "Open Business": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/open_business.png",
    "Parallel Plays": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/parallel_plays.png",
    "Ring of Fire": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/ring_of_fire.png",
    "Belles Rock": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/belles_rock.png",
    "Flaring Phoenix": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/flaring_phoenix.png",
    "Goldarm Gulch": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/goldarm_gulch.png",
    "Out in the Open": "C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/out_in_the_open.png"
}

# Variables to track win and loss counts
win_count = 0
loss_count = 0

def update_win_loss():
    """Update the win and loss count on the window."""
    win_label.config(text=f"Wins: {win_count}")
    loss_label.config(text=f"Losses: {loss_count}")
    win_rate = (win_count / (win_count + loss_count) * 100) if (win_count + loss_count) > 0 else 0
    win_rate_label.config(text=f"Win Rate: {win_rate:.2f}%")

def display_map_image(map_name, image_label):
    """Display the map image in the GUI."""
    if map_name in MAPS:
        map_image_path = MAPS[map_name]
        if os.path.exists(map_image_path):
            # Load and display the image
            img = Image.open(map_image_path)
            
            # Resize to fit within the screen dimensions (maintaining aspect ratio)
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            
            img.thumbnail((screen_width * 0.8, screen_height * 0.5))  # Resize to 80% width and 50% height
            
            img_tk = ImageTk.PhotoImage(img)
            image_label.config(image=img_tk)
            image_label.image = img_tk
        else:
            messagebox.showerror("Error", f"Image file not found: {map_image_path}")
    else:
        messagebox.showerror("Error", f"Map '{map_name}' not found. Please check the name.")

def increment_win():
    """Increment the win count and update the display."""
    global win_count
    win_count += 1
    update_win_loss()

def increment_loss():
    """Increment the loss count and update the display."""
    global loss_count
    loss_count += 1
    update_win_loss()

def reset_stats():
    """Reset the win and loss counts."""
    global win_count, loss_count
    win_count = 0
    loss_count = 0
    update_win_loss()

# Initialize the main window
root = Tk()
root.title("Brawl Stars Draft Guide")

# Set the window to full screen
root.attributes("-fullscreen", True)  # Set to fullscreen
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))  # Allow exiting fullscreen with Escape key

# Define the background color (from your provided image)
bg_color = "#61a6e1"  # A shade of blue that matches the uploaded screenshot

# Set the window background color
root.configure(bg=bg_color)

# Create a canvas for the background image
canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight(), bg=bg_color)
canvas.pack(fill="both", expand=True)

# Load the background image
background_image = Image.open("C:/Users/yashk/OneDrive/Desktop/brawl_draft_website/picsmaps/background.jpg")  # Replace with the correct image path
background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))  # Resize to fit window size
bg_image_tk = ImageTk.PhotoImage(background_image)

# Set the background image on the canvas
canvas.create_image(0, 0, image=bg_image_tk, anchor="nw")

# Load the Brawl Stars font
brawl_font = font.Font(family="Brawl Stars", size=24, weight="bold")  # Use the actual Brawl Stars font if available

# Light gray color for text background
light_gray = "#f0f0f0"

# Add a title label (no white background)
title_label = Label(root, text="Brawl Stars Draft Guide", font=brawl_font, fg="white", bg=bg_color)
title_label.place(relx=0.5, rely=0.05, anchor="n")  # Centered at the top

# Add a dropdown menu
selected_map = StringVar(root)
selected_map.set("Select a map")  # Default value

map_dropdown = OptionMenu(root, selected_map, *MAPS.keys())
map_dropdown.place(relx=0.5, rely=0.15, anchor="n")  # Centered below the title

# Add an image display area
image_label = Label(root, bg=bg_color)  # Label to display the map image, no white background
image_label.place(relx=0.5, rely=0.4, anchor="n")

# Add a button to display the map in the top-right corner
display_button = Button(
    root,
    text="Display Map",
    command=lambda: display_map_image(selected_map.get(), image_label),
    font=brawl_font,
    bg="blue",
    fg="white"
)
display_button.place(relx=0.95, rely=0.05, anchor="ne")  # Positioned at the top-right corner

# Win/Loss Tracking Label (Top Left)
win_label = Label(root, text=f"Wins: {win_count}", font=brawl_font, bg=light_gray, fg="black")
win_label.place(relx=0.05, rely=0.05, anchor="nw")

loss_label = Label(root, text=f"Losses: {loss_count}", font=brawl_font, bg=light_gray, fg="black")
loss_label.place(relx=0.05, rely=0.1, anchor="nw")

# Win Rate Label
win_rate_label = Label(root, text="Win Rate: 0%", font=brawl_font, bg=light_gray, fg="black")
win_rate_label.place(relx=0.05, rely=0.15, anchor="nw")

# Win and Loss Buttons
win_button = Button(root, text="Win", command=increment_win, font=brawl_font, bg="green", fg="white")
win_button.place(relx=0.05, rely=0.25, anchor="nw")

loss_button = Button(root, text="Loss", command=increment_loss, font=brawl_font, bg="red", fg="white")
loss_button.place(relx=0.05, rely=0.35, anchor="nw")

# Reset Button
reset_button = Button(root, text="Reset", command=reset_stats, font=brawl_font, bg="gray", fg="white")
reset_button.place(relx=0.05, rely=0.45, anchor="nw")

# Run the GUI event loop
root.mainloop()
