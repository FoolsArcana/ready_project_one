"""
import pandas as pd
import matplotlib.pyplot as plotter
import csv
import re


import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

states = {
		'AK': 'Alaska',
		'AL': 'Alabama',
		'AR': 'Arkansas',
		'AS': 'American Samoa',
		'AZ': 'Arizona',
		'CA': 'California',
		'CO': 'Colorado',
		'CT': 'Connecticut',
		'DC': 'District of Columbia',
		'DE': 'Delaware',
		'FL': 'Florida',
		'GA': 'Georgia',
		'GU': 'Guam',
		'HI': 'Hawaii',
		'IA': 'Iowa',
		'ID': 'Idaho',
		'IL': 'Illinois',
		'IN': 'Indiana',
		'KS': 'Kansas',
		'KY': 'Kentucky',
		'LA': 'Louisiana',
		'MA': 'Massachusetts',
		'MD': 'Maryland',
		'ME': 'Maine',
		'MI': 'Michigan',
		'MN': 'Minnesota',
		'MO': 'Missouri',
		'MP': 'Northern Mariana Islands',
		'MS': 'Mississippi',
		'MT': 'Montana',
		'NA': 'National',
		'NC': 'North Carolina',
		'ND': 'North Dakota',
		'NE': 'Nebraska',
		'NH': 'New Hampshire',
		'NJ': 'New Jersey',
		'NM': 'New Mexico',
		'NV': 'Nevada',
		'NY': 'New York',
		'OH': 'Ohio',
		'OK': 'Oklahoma',
		'OR': 'Oregon',
		'PA': 'Pennsylvania',
		'PR': 'Puerto Rico',
		'RI': 'Rhode Island',
		'SC': 'South Carolina',
		'SD': 'South Dakota',
		'TN': 'Tennessee',
		'TX': 'Texas',
		'UT': 'Utah',
		'VA': 'Virginia',
		'VI': 'Virgin Islands',
		'VT': 'Vermont',
		'WA': 'Washington',
		'WI': 'Wisconsin',
		'WV': 'West Virginia',
		'WY': 'Wyoming'
}



food_atlas_data = pd.read_csv("Data/Food_Atlas2015/Food_Atlas2015.csv")


food_atlas_data.rename(columns = Name_Conversion,inplace = True)



county_food_atlas_groupdata = food_atlas_data.groupby(['State','County'])[['Population, tract total',"Low access, population at 1 mile for urban areas and 20 miles for rural areas, number"]].sum()
county_food_atlas_groupdata['ratio']=county_food_atlas_groupdata['Low access, population at 1 mile for urban areas and 20 miles for rural areas, number']/county_food_atlas_groupdata['Population, tract total']
county_food_atlas_groupdata.reset_index(inplace=True)
#county_food_atlas_groupdata.head()



code_lookups = pd.read_csv('Data/mapping_info/zip_codes_states.csv')
code_lookups.drop_duplicates(['state','county'],keep='last',inplace=True)
code_lookups['state_name'] = code_lookups.apply(lambda x: states.get(x['state'],None),axis=1)
#code_lookups.head()



county_food_atlas_loc_data = county_food_atlas_groupdata.merge(code_lookups, left_on = ['State','County'],right_on = ['state_name','county'],how='inner') 
#county_food_atlas_loc_data.head()


plotter.figure(figsize=(20,20))
plotter.scatter(county_food_atlas_loc_data['longitude'], county_food_atlas_loc_data['latitude'], c=county_food_atlas_loc_data['ratio']*100.0)
plotter.show()
"""



# The code for changing pages was derived from: http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk
from tkinter import ttk
from tkinter import *

LARGE_FONT= ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

	def __init__(self, *args, **kwargs):
		
		tk.Tk.__init__(self, *args, **kwargs)

		#tk.Tk.iconbitmap(self, default="clienticon.ico")
		tk.Tk.wm_title(self, "Sea of BTC client")
		
		
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand = True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		self.frames = {}

		for F in (StartPage, PageOne, PageTwo, PageThree):

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()

		
class StartPage(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		label = tk.Label(self, text="Start Page", font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		button = ttk.Button(self, text="Visit Page 1",
							command=lambda: controller.show_frame(PageOne))
		button.pack()

		button2 = ttk.Button(self, text="Visit Page 2",
							command=lambda: controller.show_frame(PageTwo))
		button2.pack()

		button3 = ttk.Button(self, text="Graph Page",
							command=lambda: controller.show_frame(PageThree))
		button3.pack()


class PageOne(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		button1 = ttk.Button(self, text="Back to Home",
							command=lambda: controller.show_frame(StartPage))
		button1.pack()

		button2 = ttk.Button(self, text="Page Two",
							command=lambda: controller.show_frame(PageTwo))
		button2.pack()


class PageTwo(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
		label.pack(pady=10,padx=10)

		button1 = ttk.Button(self, text="Back to Home",
							command=lambda: controller.show_frame(StartPage))
		button1.pack()

		button2 = ttk.Button(self, text="Page One",
							command=lambda: controller.show_frame(PageOne))
		button2.pack()


class PageThree(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
		label.pack(pady=10,padx=10)
		tkvar = StringVar()
		#button1 = ttk.Button(self, text="Back to Home",
		#					command=lambda: controller.show_frame(StartPage))
		#button1.pack()
		import pandas as pd
		import matplotlib.pyplot as plotter
		import csv
		import re


		import matplotlib
		matplotlib.use("TkAgg")
		from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
		from matplotlib.figure import Figure

		states = {
				'AK': 'Alaska',
				'AL': 'Alabama',
				'AR': 'Arkansas',
				'AS': 'American Samoa',
				'AZ': 'Arizona',
				'CA': 'California',
				'CO': 'Colorado',
				'CT': 'Connecticut',
				'DC': 'District of Columbia',
				'DE': 'Delaware',
				'FL': 'Florida',
				'GA': 'Georgia',
				'GU': 'Guam',
				'HI': 'Hawaii',
				'IA': 'Iowa',
				'ID': 'Idaho',
				'IL': 'Illinois',
				'IN': 'Indiana',
				'KS': 'Kansas',
				'KY': 'Kentucky',
				'LA': 'Louisiana',
				'MA': 'Massachusetts',
				'MD': 'Maryland',
				'ME': 'Maine',
				'MI': 'Michigan',
				'MN': 'Minnesota',
				'MO': 'Missouri',
				'MP': 'Northern Mariana Islands',
				'MS': 'Mississippi',
				'MT': 'Montana',
				'NA': 'National',
				'NC': 'North Carolina',
				'ND': 'North Dakota',
				'NE': 'Nebraska',
				'NH': 'New Hampshire',
				'NJ': 'New Jersey',
				'NM': 'New Mexico',
				'NV': 'Nevada',
				'NY': 'New York',
				'OH': 'Ohio',
				'OK': 'Oklahoma',
				'OR': 'Oregon',
				'PA': 'Pennsylvania',
				'PR': 'Puerto Rico',
				'RI': 'Rhode Island',
				'SC': 'South Carolina',
				'SD': 'South Dakota',
				'TN': 'Tennessee',
				'TX': 'Texas',
				'UT': 'Utah',
				'VA': 'Virginia',
				'VI': 'Virgin Islands',
				'VT': 'Vermont',
				'WA': 'Washington',
				'WI': 'Wisconsin',
				'WV': 'West Virginia',
				'WY': 'Wyoming'
		}

		Name_Conversion = {}
		with open("Data/Food_Atlas2015/Long Names.txt") as longFile:
			with open("Data/Food_Atlas2015/Short Names.txt") as shortFile:
				longReader = longFile.readlines()
				shortReader = shortFile.readlines()
				longReader = [x.strip() for x in longReader]
				shortReader = [y.strip() for y in shortReader]
				Name_Conversion = dict(zip(shortReader,longReader))

		food_atlas_data = pd.read_csv("Data/Food_Atlas2015/Food_Atlas2015.csv")


		food_atlas_data.rename(columns = Name_Conversion,inplace = True)

		# Create a Tkinter variable
		#tkvar = StringVar(root)
		# Dictionary with options
		choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}
		choices = list(food_atlas_data)
		tkvar.set('Population, tract total') # set the default option
		
		
		
		popupMenu = OptionMenu(self, tkvar, *choices)
		#Label(mainframe, text="Choose a dish").grid(row = 1, column = 1)
		popupMenu.pack()#.grid(row = 2, column =1)
		
		triggered = False
		
		#f = Figure(figsize=(2,2), dpi=100)
		#f.clear()
		#a = f.add_subplot(111)
		#a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
		#a.scatter(county_food_atlas_loc_data['longitude'], county_food_atlas_loc_data['latitude'], c=county_food_atlas_loc_data['ratio']*100.0)
		
		#canvas = FigureCanvasTkAgg(f, self)
		#canvas.show()
		
		#canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
		
		# on change dropdown value
		def change_dropdown(*args):
			#global triggered
			
			#uncomment for further work, will
			#global canvas
			####DO NOT DO THIS
			#canvas.pack_forget()

			county_food_atlas_groupdata = food_atlas_data.groupby(['State','County'])[['Population, tract total',tkvar.get()]].sum()
			county_food_atlas_groupdata['ratio']=county_food_atlas_groupdata[tkvar.get()]/county_food_atlas_groupdata['Population, tract total']
			county_food_atlas_groupdata.reset_index(inplace=True)
			#county_food_atlas_groupdata.head()



			code_lookups = pd.read_csv('Data/mapping_info/zip_codes_states.csv')
			code_lookups.drop_duplicates(['state','county'],keep='last',inplace=True)
			code_lookups['state_name'] = code_lookups.apply(lambda x: states.get(x['state'],None),axis=1)
			#code_lookups.head()



			county_food_atlas_loc_data = county_food_atlas_groupdata.merge(code_lookups, left_on = ['State','County'],right_on = ['state_name','county'],how='inner') 
			#county_food_atlas_loc_data.head()


			#plotter.figure(figsize=(20,20))
			#plotter.scatter(county_food_atlas_loc_data['longitude'], county_food_atlas_loc_data['latitude'], c=county_food_atlas_loc_data['ratio']*100.0)
			#plotter.show()


			
			#f = canvas.gcf()
			f = Figure(figsize=(8,4), dpi=100)
			f.clf()
			a = f.add_subplot(111)
			#a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
			a.scatter(county_food_atlas_loc_data['longitude'], county_food_atlas_loc_data['latitude'], c=county_food_atlas_loc_data['ratio']*100.0)
			
			canvas = FigureCanvasTkAgg(f, self)
			canvas.show()
			canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

			#toolbar = NavigationToolbar2TkAgg(canvas, self)
			#toolbar.update()
			#if not triggered:
			#	canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
			#	triggered = True
			
			
			

		# link function to change dropdown
		tkvar.trace('w', change_dropdown)
		
		########################PLOT
		

		'''
		# Create a Tkinter variable
		tkvar = StringVar(root)
		 
		# Dictionary with options
		choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}
		tkvar.set('Pizza') # set the default option
		 
		popupMenu = OptionMenu(mainframe, tkvar, *choices)
		Label(mainframe, text="Choose a dish").grid(row = 1, column = 1)
		popupMenu.grid(row = 2, column =1)
		 
		# on change dropdown value
		def change_dropdown(*args):
			print( tkvar.get() )
		 
		# link function to change dropdown
		tkvar.trace('w', change_dropdown)
		'''

		

app = SeaofBTCapp()
app.mainloop()