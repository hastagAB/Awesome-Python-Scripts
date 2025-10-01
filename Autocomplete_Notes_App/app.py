import tkinter as tk
from tkinter import filedialog, messagebox

class AutocompleteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Autocomplete Notes App")

        # Load words from wordlist.txt
        self.autocomplete_list = self.load_wordlist("wordlist.txt")

        self.create_widgets()

    def load_wordlist(self, filename):
        """Load words from a specified file."""
        try:
            with open(filename, 'r') as file:
                words = [line.strip() for line in file.readlines() if line.strip()]
            return words
        except FileNotFoundError:
            messagebox.showerror("Error", f"File '{filename}' not found.")
            return []  

    def create_widgets(self):
        self.large_entry = tk.Text(self.root, wrap=tk.WORD) 
        self.large_entry.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.suggestion_entry = tk.Entry(self.root, width=60, state='readonly') 
        self.suggestion_entry.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.save_button = tk.Button(self.root, text="Save Notes", command=self.save_notes)
        self.save_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.root.grid_rowconfigure(0, weight=1)  
        self.root.grid_columnconfigure(0, weight=1)

        self.large_entry.bind("<KeyRelease>", self.update_suggestion)
        self.large_entry.bind("<Tab>", self.insert_complete_word)

    def update_suggestion(self, event):
        """Update the suggestion based on the current input."""
        current_input = self.get_last_word()
        suggestion = ""

        if current_input: 
            matches = [word for word in self.autocomplete_list if word.startswith(current_input)]
            if matches:
                suggestion = matches[0]  

        self.suggestion_entry.config(state='normal')
        self.suggestion_entry.delete(0, tk.END)  
        self.suggestion_entry.insert(0, suggestion)  
        self.suggestion_entry.config(state='readonly')  

    def get_last_word(self):
        """Get the last word from the current line of the large entry."""
        cursor_index = self.large_entry.index(tk.INSERT)
        line_number = cursor_index.split('.')[0]  
        line_text = self.large_entry.get(f"{line_number}.0", f"{line_number}.end").strip()  # Get the current line text
        words = line_text.split()  
        return words[-1] if words else "" 

    def insert_complete_word(self, event):
        """Insert the complete word into the large entry when Tab is pressed."""
        complete_word = self.suggestion_entry.get()
        if complete_word: 
            cursor_index = self.large_entry.index(tk.INSERT)
            line_number = cursor_index.split('.')[0]  
            line_text = self.large_entry.get(f"{line_number}.0", f"{line_number}.end").strip() 
            words = line_text.split() 
            if words:
                words[-1] = complete_word  
                self.large_entry.delete(f"{line_number}.0", f"{line_number}.end")
                self.large_entry.insert(f"{line_number}.0", ' '.join(words)) 

        return "break"  

    def save_notes(self):
        """Save the notes to a file."""
        notes = self.large_entry.get("1.0", tk.END).strip()
        if notes:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                                       filetypes=[("Text files", "*.txt"), 
                                                                  ("All files", "*.*")])
            if file_path:  
                with open(file_path, 'w') as file:
                    file.write(notes)
                messagebox.showinfo("Success", "Notes saved successfully!")
        else:
            messagebox.showwarning("Warning", "No notes to save!")

if __name__ == "__main__":
    root = tk.Tk()
    app = AutocompleteApp(root)
    root.mainloop()
