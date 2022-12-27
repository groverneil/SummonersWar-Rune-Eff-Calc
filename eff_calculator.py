"""Contributors: Neil Grover, Ishaan Singh"""
# All rune stats are in the Rune_stats.txt file <-- only for 6 star runes
filename = r"Rune_stats.txt"
# helper function for the transferring of the values from the text file into the dictionary
#def string_to_int_list(string_val):
#    return [int(x) for x in string_val.split(',')]


def stat_parser(stat):

    '''
    splits the input into the stat and the value (i know the code is ver weird but ignore that.
    '''


    if stat.split(' +')[0].lower() in ['acc', 'res', 'accuracy', 'resistance']:
        return [stat.split(' +')[0].lower(), int(stat.split(' +')[1])] if stat[-1] != '%' else [stat.split(' +')[0].lower(), int(stat.replace('%','').split(' +')[1])]
    else:
        return [stat.split(' +')[0].lower(), int(stat.split(' +')[1])] if stat[-1] != '%' else [stat.split(' +')[0].lower()+'%', int(stat.replace('%','').split(' +')[1])]

    # This seems redundant.
    # We can consider Acc and Res to be % values by default.

    # 

def certain_val_check(val):

    '''
     converts acc and res to their full form so that they can be called by the rune_vals dictionary.
    '''

    val_split = val.split(' +')
    #print(val_split)
    # this blocks checks for irregularities in the val types

    if val_split[0] == 'acc':
        val_split[0] = 'accuracy' 
    elif val_split[0] == 'res':
        val_split[0] = 'resistance'       
    elif val_split[0][0] == 'c':

        # this cancerous line joins crit rate and crit dmg the correct way in case people don't >:(
        val_split[0] = val_split[0].split()[0] + '_' + val_split[0].split()[1]

    return ' +'.join(val_split)        

def color_check(rarity):
    val_dict = {
        'normal': 'white',
        'magic': 'green',
        'rare': 'blue',
        'hero': 'purple',
        'legend': 'orange'
    }
    return val_dict.get(rarity.lower(), 'fuck off')

class Rune:

    '''
    This class contains all attributes of the rune as well as calc functions.
    '''


    def __init__(self, base_rarity = "", main_stat = "", innate_stat = "", stat_1 = "", stat_2 = "", stat_3 = "", stat_4 = "", pow_lvl = 0):
        # creating the dictionary with all the values
        self.rune_vals = dict()

        with open(filename, encoding = "utf8") as stat_chart:
            for line in stat_chart:
                # these two lines get the values from the text file and split them into the dictionary
                (key, val) = line.split()
                self.rune_vals[key] = int(val)
        # converts the default string values extracted from the text file into ints so that
        # they can be used in calculations

        # IMPORTANT - The values in self.rune_vals are stored in this format {stat_name: max}
        # the important - and unchangeable stats
        self.rarity = base_rarity.lower() if base_rarity.lower() not in ['normal', 'magic', 'rare', 'hero', 'legend'] else color_check(base_rarity.lower())
        self.main = main_stat
        self.innate = certain_val_check(innate_stat.lower()) if innate_stat != '' else innate_stat

        # % efficiency of the innate stat if there is one
        self.innate_eff = 0         # calculated value

        # all four substats of the rune
        # it puts it throught a function that checks that all the terms will be registered by the dictionary 

        # I'm making this simpler by just having a list that has all these...would reduce my headache significantly
        self.stat_list = [0] * 4 
        # don't pay attention to these theyll make your brain hurt unecessarily....just accept that they work and move on
        self.stat_list[0] = stat_parser(certain_val_check(stat_1.lower())) if stat_1 != '' else 0 # first stat
        self.stat_list[1] = stat_parser(certain_val_check(stat_2.lower())) if stat_2 != '' else 0 # second stat
        self.stat_list[2] = stat_parser(certain_val_check(stat_3.lower())) if stat_3 != '' else 0 # third stat
        self.stat_list[3] = stat_parser(certain_val_check(stat_4.lower())) if stat_4 != '' else 0 # fourth stat

        # removes the redundant zeroes from the self.stat_list
        if 0 in self.stat_list:
            for _ in self.stat_list: self.stat_list.remove(0)

        self.stat_rolls = [] # place to fill up how many rolls per stat ranging from 1 - 4
        self.power_level = pow_lvl // 3 if pow_lvl < 15 else 4   # made sure this always rounds down and if its 15 then its the same as 12

        # relative efficiency measures how efficient a rune is relative to its base type (i.e. blue and purple runes can technically have 100% efficiency)
        self.rel_eff = 0
        # absolute efficiency measures how good a rune is overall in the game, so runes that are higher base grade and have innate will
        # always have a higher potential efficiency
        self.abs_eff = 0
        # efficiency coefficient to determine maximum efficiency for a rune of a different grade
        self.eff_coeff = 0

        # Let us break down the math for the function below:

        '''
        Rune Rarity         Number of Roles Possible (Not including Innate) These rolls include the base rolls, hence
        Legend rune = 4 base rolls + 4 power-up rolls = 8 rolls

        White               4               
        Green               5
        Blue                6
        Purple              7
        Orange              8
        '''

    # to calculate the 
    def base_rarity_efficiency(self):
        match self.rarity:
            case 'white': self.eff_coeff = 4/8
            case 'green': self.eff_coeff = 5/8
            case 'blue': self.eff_coeff = 6/8
            case 'purple': self.eff_coeff = 7/8
            case 'orange': self.eff_coeff = 1
        
        # This can store the efficiency based on the number of rolls

        # We would need another function that calculates efficiency based on actual values.

    # Ishaan <- spent a solid 5 minutes figuring out what in the goddamn fuck this function was.....really need to work on my naming skills D:
    def roll_calc(self):
        # this is probably gonna piss me off no end, but now i try and make this shit (Ishaan)
        # basically this function calculates how many rolls the rune had...and from there determines its actually efficiency? sounds like that could be fun
        print("HELLO!")
        for roll in self.stat_list:
            self.stat_rolls.append(roll[1]/self.rune_vals[roll[0]])

        # as I thought, the function itself was pretty simple, but the number of edits I've had to make because of it are making me mad
        # also since i dont return anything, self.stat_rolls itself is modified when this shit is called, so uh just remember that

        

    def rel_eff(self):

        '''
        This function would calculate the relative efficiency of the rune. (basically a flat efficiency value not considering the rune's base rarity)
        '''

        pass

        # This function does not account for self.eff_coeff

    def abs_eff(self):
        '''
        And here we give a fuck about the base rarity
        '''
        pass

        #This function accounts for self.eff_coeff
        #Can be calculated by using self.rel_eff and self.eff_coeff

    #@staticmethod  <-- THIS SHIT DIDNT HELP NEIL HAAAALPPPPPPPP
    def innate_efficiency(self):

        '''
        returns efficiency of the innate stat
        '''

        # if there is no innate or the innate is incorrect, then return -1 which should let the calculation functionn
        # know that the innate should not be considered
        if self.innate == "" or stat_parser(self.innate)[0] not in self.rune_vals.keys(): 
            self.innate_eff = -1
        elif stat_parser(self.innate)[0] in self.rune_vals:
            # calculates the innate val efficiency by dividing the innate value by its max
            self.innate_eff = stat_parser(self.innate)[1] / self.rune_vals[stat_parser(self.innate)[0]]
        return self.innate_eff

    def total_efficiency(self):

        pass
        #returns overall efficiency of rune
        #Accounts for both innate and base stat efficiency.
        # return value to absolute efficiency
    
    def printer(self):

        '''
        test function to print values
        '''

        '''self.innate_eff = self.innate_efficiency()
        print('the rune_dict:')
        for k,j in self.rune_vals.items():
            print(f'{k} : {j}')
        print('innate efficiency: ', self.innate_eff)'''

        print("The stats of each rune as they are saved:")
        for x in range(len(self.stat_list)):
            print(f"stat no. {x+1}: {self.stat_list[x]}")
        
        print("The stat_list: ", self.stat_list)
        print(f"The rarity of the rune: {self.rarity}")
        self.roll_calc()
        print(f"The total rolls and roll values: {self.stat_rolls}")




if __name__ == '__main__':
    # testing the stat_parser function (planning to cal)

    # a = input().lower()
    # test_var = color_check(a)
    # print(test_var)

    rune = Rune("Rare", "", 'hp +325', "hp +8%", "spd +30", "atk% +6", "res +8")
    #rune.innate_efficiency()
    rune.printer()

    

    




