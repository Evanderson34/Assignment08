#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with Classes and Objects
# Change Log: (Who, When, What)
# Evan Anderson, 2021-December-08, created file
#------------------------------------------#

import os

# -- DATA -- #
strFileName = 'CDInventory.txt' # data storage file
lstOfCDObjects = [] # list of objects to hold data
objFile = None  # file object

# -- PROCESSING -- #
class CD(): 
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    def __init__(self, ID, Title, Artist): # Constructor
        # -- Attributes -- #
        self.cd_id = ID
        self.cd_title = Title
        self.cd_artist = Artist

    def __str__(self):
        return '{}, {}, {}'.format(self.cd_id,self.cd_title,self.cd_artist)

# -- PROCESSING -- #
class FileIO():
    """Processes data to and from file"""
    
    def save_inventory(file_name, lst_Inventory):
        """Function to save data to file
        
        Writes the data in string format from 2D table (list of objects) to file identified by file_name

        Args:
            file_name (string): name of file used to write the data to
            table (list of objects): 2D data structure that holds the data during runtime

        Returns:
            None.
        """
        objFile = open(file_name, 'w')
        for row in lst_Inventory:
            objFile.write(row.__str__() + '\n')
        objFile.close()
        
    def load_inventory(file_name, table):
        """Function to convert data from file to list of objects

        Reads the data from file identified by file_name into a 2D table (list of objects)

        Args:
            file_name (string): name of file used to read the data from
            table (list of objects): 2D data structure that holds the data during runtime

        Returns:
            None.
        """
        
        table.clear() # this clears existing data and allows to load data from fil
        try:
            objFile = open(file_name, 'r')
        except FileNotFoundError:
            objFile = open(file_name, 'w')
            print('Source file not found! New text document \'CDInventory.txt\' created.\n')
            objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            ObjectName = CD(data[0],data[1],data[2])
            table.append(ObjectName)
        objFile.close()                

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""
    
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
    
        print('Menu\n\n[l] Load Inventory from File\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] Exit')
    
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        
        choice = ' '
        while True:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
            OneOfMenuOptions = choice in ['l', 'a', 'i', 's', 'x']
            if OneOfMenuOptions:
                break
            try:
                if not OneOfMenuOptions:
                    raise Exception('\nInvalid Option!')
            except Exception as e:
                    print (e)     
        return choice
    
    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of objects): 2D data structure that holds the data during runtime.

        Returns:
            None.

        """   
        print('\n======= The Current Inventory: =======')
        print('ID, CD Title, Artist')
        for row in table:
            print(row) #returns data as string using the __str__ method
        print('======================================\n')
    
    @staticmethod
    def input_cd():
        """Function to ask user for input and appends input to 2D table data

        Args:
            strID (string): identifier obtained from user, converted to integer
            strTitle (string): name of CD title
            stArtist (string): name of CD artist

        Returns:
            None.            
        """
        try: 
            value1 = int(input('Enter ID: ').strip()) # Converts ID input to integer
            value2 = input('What is the CD\'s title? ').strip()
            value3 = input('What is the Artist\'s name? ').strip()
            return value1,value2,value3
        except ValueError:
              print('\nINVALID INPUT DATA\nID MUST BE A NUMBER')           
        
    def add_CD(value1,value2,value3):
        """Function to save newly created object with input data to table
    
        Args:
            Value1: the CD ID number as provided by the user
            Value2: the CD title as provided by the user
            Value3: the CD artist as provided by the user
        
        Returns:
            None.
        """    
        NewCD = CD(value1,value2,value3) # Creates new object
        lstOfCDObjects.append(NewCD) # Appends object to list of objects

# -- Main Body of Script -- #

# 1. When program starts, read in the currently saved Inventory. If no inventory exists, a new file is created.
FileIO.load_inventory(strFileName,lstOfCDObjects)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    # 3. Process menu selection
    strChoice = IO.menu_choice()
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the inventory will be reloaded from file.')
        strYesNo = input('Type \'yes\' to continue and reload from file. Otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('\nReloading...')
            if os.stat(strFileName).st_size == 0:
                print('\nSource file is empty!')
                lstOfCDObjects= []
            FileIO.load_inventory(strFileName,lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top. 
    # 3.3 process add a CD
    elif strChoice == 'a':
        try:
            cd_id, cd_title, cd_artist = IO.input_cd()
            IO.add_CD(cd_id, cd_title, cd_artist)
        except TypeError:    
            pass
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.5 process save inventory to file
    elif strChoice == 's':
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName,lstOfCDObjects)   
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.

