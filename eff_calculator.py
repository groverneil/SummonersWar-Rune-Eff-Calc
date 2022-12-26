# Contributors: Neil Grover, Ishaan Singh
# All rune stats are in the Rune_stats.txt file <-- only for 6 star runes

FILENAME = r"Rune_stats.txt"

def string_to_int_list(string_val):

    '''helper function for the transferring of the values from the text file into the dictionary'''

    return [int(x) for x in string_val.split(',')]

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

def certain_val_check(val):

    '''
     converts acc and res to their full form so that they can be called by the rune_vals dictionary.
    '''

    val_split = val.split(' +')
    print(val_split)
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

    '''
    Takes the rune rarity name and returns the color of the rune.
    '''

    match rarity.lower():
        case 'normal':
            return 'white'  
        case 'magic':
            return 'green'       
        case 'rare':
            return 'blue'      
        case 'hero':
            return 'purple'     
        case 'legend':
            return 'orange'

class Rune:

    '''
    This class contains all attributes of the rune as well as calc functions.
    '''


    def __init__(self, base_rarity = "", main_stat = "", innate_stat = "", stat_1 = "", stat_2 = "", stat_3 = "", stat_4 = "", pow_lvl = 0):
        # creating the dictionary with all the values
        self.rune_vals = dict()
        with open(FILENAME) as f1:
            for line in f1:
                # these two lines get the values from the text file and split them into the dictionary
                (key, val) = line.split()
                self.rune_vals[key] = val
        # converts the default string values extracted from the text file into ints so that
        # they can be used in calculations
        for x in self.rune_vals:
            self.rune_vals[x] = string_to_int_list(self.rune_vals[x])
        # IMPORTANT - The values in self.rune_vals are stored in this format {stat_name: [min, max]}
        # the important - and unchangeable stats
        self.rarity = base_rarity.lower() if base_rarity.lower() not in ['normal', 'magic', 'rare', 'hero', 'legend'] else color_check(base_rarity.lower())
        self.main = main_stat
        self.innate = certain_val_check(innate_stat.lower()) if innate_stat != '' else innate_stat
        # % efficiency of the innate stat if there is one
        self.innate_eff = 0         # calculated value

        # all four substats of the rune
        # it puts it throught a function that checks that all the terms will be registered by the dictionary 
        self.first = certain_val_check(stat_1.lower()) if stat_1 != '' else stat_1
        self.second = certain_val_check(stat_2.lower()) if stat_2 != '' else stat_2
        self.third = certain_val_check(stat_3.lower()) if stat_3 != '' else stat_3
        self.fourth = certain_val_check(stat_4.lower()) if stat_4 != '' else stat_4

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
        Rune Rarity         Number of Roles Possible (Not including Innate)

        White               5               
        Green               6
        Blue                7
        Purple              8
        Orange              9
        '''

    def base_efficiency(self):

        '''
        Returns the base efficiency value for the given rarity.
        Value is calculated with respect to orange runes.
        '''

        match self.rarity:
            case 'white': self.eff_coeff = 5/9
            case 'green': self.eff_coeff = 6/9
            case 'blue': self.eff_coeff = 7/9
            case 'purple': self.eff_coeff = 8/9
            case 'orange': self.eff_coeff = 1
        
        # This can store the efficiency based on the number of rolls

        # We would need another function that calculates efficiency based on actual values.

    def rel_eff(self):

        '''
        This function would calculate the relative efficiency of the rune.
        '''

        pass

        # This function does not account for self.eff_coeff

    def abs_eff(self):
        pass

        #This function accounts for self.eff_coeff
        #Can be calculated by using self.rel_eff and self.eff_coeff
    
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
            self.innate_eff = stat_parser(self.innate)[1] / self.rune_vals[stat_parser(self.innate)[0]][1]
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

        self.innate_eff = self.innate_efficiency()
        print('the rune_dict:')
        for k,j in self.rune_vals.items():
            print(f'{k} : {j}')
        print('innate efficiency: ', self.innate_eff)




if __name__ == '__main__':
    # testing the stat_parser function (planning to cal)

    # a = input().lower()
    # test_var = color_check(a)
    # print(test_var)

    rune = Rune("", "", 'hp +325')
    #rune.innate_efficiency()
    rune.printer()

    




