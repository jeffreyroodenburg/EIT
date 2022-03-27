from tkinter import *
from tkinter import ttk
import time




class EIT:
	def __init__(self):
		##// Window Config \\##
		self.bg_color = "#393d49"
		self.fg_color = "white"
		self.root = Tk()
		self.root.config(bg=self.bg_color)
		self.root.geometry("600x500")
		self.root.attributes("-fullscreen", True)
		self.root.title("Griftland Iteam")

		##// Afstand Input Box \\##
		self.afstand_entry = Entry(self.root, font=("Helvetica", 30))
		self.afstand_entry.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

		##// Afstand Label \\##
		self.afstand_label = Label(self.root, font=("Helvetica", 30), text="Afstand in km:", bg=self.bg_color, fg=self.fg_color)
		self.afstand_label.grid(row=0, column=0, padx=5, pady=5)

		##// Submit Knop \\##
		self.submit_knop = Button(self.root, font=("Helvetica", 30), text="Submit", bg=self.bg_color, fg=self.fg_color, command=self.submit)
		self.submit_knop.grid(row=1, column=2,padx=5, pady=5)

		##// Info Labels \\##
		self.gereden_afstand_label = Label(self.root, font=("Helvetica", 20), text=f"Gereden afstand: ", bg=self.bg_color, fg=self.fg_color)
		self.gereden_afstand_label.grid(row=3, column=0, padx=0, pady=5)


		self.co2_uitstoot_label = Label(self.root, font=("Helvetica", 20), text=f"CO2 uitstoot: ", bg=self.bg_color, fg=self.fg_color)
		self.co2_uitstoot_label.grid(row=4, column=0, padx=0, pady=5)

		self.co2_in_hout_label = Label(self.root, font=("Helvetica", 20), text=f"CO2 in hout: ", bg=self.bg_color, fg=self.fg_color)
		self.co2_in_hout_label.grid(row=5, column=0, padx=0, pady=5)

		self.benzine_verbruik_label = Label(self.root, font=("Helvetica", 20), text=f"Benzine verbruik: ", bg=self.bg_color, fg=self.fg_color)
		self.benzine_verbruik_label.grid(row=6, column=0, padx=0, pady=5)

		self.benzine_kosten_label = Label(self.root, font=("Helvetica", 20), text=f"Benzine kosten: ", bg=self.bg_color, fg=self.fg_color)
		self.benzine_kosten_label.grid(row=7, column=0, padx=0, pady=5)

		self.root.mainloop()



	##// Functions \\##
	def submit(self):
		##// Afstand \\##
		self.gereden_afstand = self.afstand_entry.get()
		self.gereden_afstand = str(self.gereden_afstand)
		self.gereden_afstand_label["text"] = f"gereden_afstand: {self.gereden_afstand} km"

		##// CO2 Uitstoot \\##
		self.co2_uitstoot = float(self.gereden_afstand) * 119
		self.co2_in_hout = self.co2_uitstoot * 0.5
		self.co2_uitstoot = str(self.co2_uitstoot)
		self.co2_uitstoot.split(".")
		self.co2_uitstoot_label["text"] = f"CO2 uitstoot: {self.co2_uitstoot[:6]} gram"

		##// CO2 In Hout \\##
		self.co2_in_hout = str(self.co2_in_hout)
		self.co2_in_hout_label["text"] = f"CO2 in hout: {self.co2_in_hout[:3]} kilo"



		##// Benzine Verbruik \\##
		self.benzine_verbruik = float(self.gereden_afstand) / 14
		self.benzine_kosten = self.benzine_verbruik * 1.2
		self.benzine_verbruik = str(self.benzine_verbruik)
		self.benzine_verbruik_label["text"] = f"Benzine verbruik: {self.benzine_verbruik[:3]} L"

		##// benzine kosten \\##
		self.benzine_kosten = str(self.benzine_kosten)
		self.benzine_kosten_label["text"] = f"Benzine kosten: €{self.benzine_kosten[:3]}"

		


EIT()
