import unittest
from collections import OrderedDict, defaultdict
import pylha
from smeftrunner import SMEFT


"""get the python output file"""
smeft = SMEFT()

smeft.scale_in = 1e4
smeft.scale_high = 1e4

with open('data/SMInput-CPV.dat', 'r') as f1:
  with open('data/WCsInput-CPV-SMEFT.dat', 'r') as f2:
    smeft.load_initial((f1, f2,))
    

C_out = smeft.rgevolve(scale_out=160)
C_out_approx = smeft.rgevolve_leadinglog(scale_out=160)

smeft.dump(C_out, open('data/my_output_file.dat', 'w'))
smeft.dump(C_out, open('data/my_output_file_approx.dat', 'w'))



"""get datas as a dictionary"""
def BLOCKdict(streams):
    d = {}
    for stream in streams:
        s = pylha.load(stream)
        if 'BLOCK' not in s:
            raise ValueError("No BLOCK found")
        d.update(s['BLOCK'])
    return d

#from python
with open('data/my_output_file.dat', 'r') as f:
    py_results = BLOCKdict((f,))

#from mathematica
with open('data/Output_SMEFTrunner.dat', 'r') as f:
    ma_results = BLOCKdict((f,))



  
"""check the keys of blocks"""
if set(py_results.keys()) is set(ma_results.keys()):
    print ("Blocks equal")
else:
    print ("Blocks not equal!")
    #unique blocks from python
    diffpy = set(py_results.keys())-set(ma_results.keys())
    if len(diffpy) == 0:
        print ("no unique block from python!")
    else:
        print ("unique blocks from python: %s" %diffpy)
    #unique blocks from mathematica
    diffma = set(ma_results.keys())-set(py_results.keys())
    if len(diffma) == 0:
        print ("no unique block from mathematica!")
    else:
        print ("unique blocks from mathematica: %s" %diffma)    #why is there 'WCLLPHIPHI'?
    #we also want to know the differences
    blocks = OrderedDict()
    for i in range(len(list(diffma))):
        blocks[list(diffma)[i]]=ma_results[list(diffma)[i]]
    pylha.dump({'BLOCK': blocks}, 'lha', open('blocks_diffences_ma.dat', 'w'))
    print ("The differences were written in a file 'blocks_diffences_ma.dat'")            

    


"""check the values of the common blocks"""
blocks_co = set(py_results.keys()) & set(ma_results.keys())
print ("common blocks: %s" %blocks_co)
print ("check values:")
class TestValues(unittest.TestCase):
    def test_values(self):
        defaultblocks = defaultdict(list)
        for block in blocks_co:
            #check dimension
            self.assertEqual(len(py_results[block]['values'][0]), len(ma_results[block]['values'][0])) 
            #check values
            dim=len(py_results[block]['values'][0])-1
            for py_value in py_results[block]['values']:
                for ma_value in ma_results[block]['values']:
                    if list(py_value[:dim]) == list(ma_value[:dim]):
                        try:
                            try:
                                self.assertAlmostEqual(abs(py_value[dim]), 0, places=5)
                                self.assertAlmostEqual(abs(ma_value[dim]), 0, places=5)
                            except:
                                py_value[dim]/ma_value[dim]
                                #check: print (block, value[:dim], value[dim], value_approx[dim])
                                self.assertAlmostEqual(py_value[dim]/ma_value[dim], 1, places=0)                                    
                        except:
                            #we want to know the default values
                            default = [py_value[dim], ma_value[dim]]
                            try:
                                py_value[dim]/ma_value[dim]
                                default.append(py_value[dim]/ma_value[dim])
                            except:
                                default.append('NA')
                            if block not in defaultblocks.keys():
                                defaultblocks[block]=defaultdict(list)
                                defaultblocks[block]['values']=[]
                            defaultblocks[block]['values'].append(py_value[:dim]+default)
        defaultblocks = OrderedDict(sorted(defaultblocks.items()))
        pylha.dump({'BLOCK': defaultblocks}, 'lha', open('defaultblocks_py_ma_quotient.dat', 'w'))
        print ("The different values were written in a file 'defaultblocks_py_ma_quotient.dat'")                 
                            
if __name__ == '__main__':
    unittest.main()        