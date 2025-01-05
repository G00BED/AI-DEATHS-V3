import random
import tkinter as tk
import tkinter.simpledialog
import random
import AiGeneration

#CORE GAME FUNCTIONS
class BattleRoyaleGame:
  
    def __init__(self, master):
        self.master = master
        master.title("AI DEATH GENERATOR                                              v1.3")
        master.geometry("700x800")
        master.configure(bg="#782D2D") #BEHIND ENTER NAMES COLOR 
      
        # Create a custom font
        self.custom_font = ("Impact", 14)

        # Create a text widget to display the output
        self.text_widget = tk.Text(master, font=self.custom_font, bg="#ff6b6b", fg="#ffffff", borderwidth=30, relief="sunken") #SCREEN COLOR
        self.text_widget.pack(fill="both", expand=True)

        # Create a label widget to display the names entered
        self.names_label = tk.Label(master, text="", font=self.custom_font, bg="#782D2D", fg="#ffffff")
        self.names_label.pack()#BEHIND NAMES COLOR
      
        # Load the image
        self.icon_image = tk.PhotoImage(file="Skull_Icon.png")

        # Create a start button to begin the game
        self.start_button = tk.Button(master, image=self.icon_image, font=self.custom_font, bg="black", fg="#f7f7ff", command=self.start_game) #BUTTON COLOR
        self.start_button.pack(pady=5)
  
    # Select a pair of adjacent names from the list
    def start_game(self):
        # Clear all text in the text widget
        self.text_widget.delete("1.0", "end")
    
        # Open the file containing the list of strings
        with open('deaths.txt') as f:
            strings = f.readlines()
    
        # Strip newline characters from the end of each string
        strings = [s.strip() for s in strings]
    
        # Prompt the user for a list of names
        names = []
        while True:
            name = tk.simpledialog.askstring("Enter a Name", "Enter Names, TYPE DONE When Completed:")
            if name in ["done", "Done", "DONE", "dOne", "doNe", "donE", "DOne"]:
                self.text_widget.insert("end", "Starting...\n\n")
                self.text_widget.see("end")
                break
            names.append(name.upper())  # convert name to uppercase and append to names list
    
            # Update the label with the names entered
            self.names_label.configure(text=" ".join(names))
    
        # Remove any leading or trailing whitespace from each name
        names = [n.strip() for n in names]
    
        # Keep looping until there is only one name left in the list
        while len(names) > 1:
            # Select a random string from the list of strings
            selected_string = random.choice(strings)
    
            # Select a pair of adjacent names from the list
            name_pair = AiGeneration.random_pair(names)
    
            # Insert the selected string between the pair of names
            output_string = f'\U0001F480{name_pair[0]} {selected_string} {name_pair[1]}'
    
            # Schedule the insertion of the output string and a line break with some spacing around it
            self.master.after(10000, self.text_widget.insert, "end", output_string + "\n\n")
            self.master.after(10000, self.text_widget.see, "end")
    
            # Generate AI response
            ai_response = AiGeneration.AiGeneration()
  
          # Schedule the insertion of the response below the current line in the text widget with some spacing around it
            self.master.after(10000, self.text_widget.insert, "end", f"{name_pair[1]} says: {ai_response}\n\n")
            self.master.after(10000, self.text_widget.see, "end")
  
          # Delete the first name in the pair from the list
            names.pop(0)
  
      # Schedule the insertion of the final name and the AI response with some spacing around it
        self.master.after(10000, self.text_widget.insert, "end", f"\U0001F451{names[0]}\U0001F451 IS THE LAST ALIVE!\n\n")
        self.master.after(10000, self.text_widget.see, "end")
        self.master.after(10000, self.text_widget.insert, "end", f"{AiGeneration.AiGenerationWinner()}\n\n")
        self.master.after(10000, self.text_widget.see, "end")
  

