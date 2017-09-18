import unittest
import pylha
import pkgutil


"""get datas as a dictionary"""
def BLOCKdict(streams):
    d = {}
    for stream in streams:
        s = pylha.load(stream)
        if 'BLOCK' not in s:
            raise ValueError("No BLOCK found")
        d.update(s['BLOCK'])
    return d


#exact values
with open('data/my_output_file.dat', 'r') as f:
    results = BLOCKdict((f,))

#approx values
with open('data/my_output_file_approx.dat', 'r') as f:
    results_approx = BLOCKdict((f,))


"""test"""    
class TestValues(unittest.TestCase):
    def test_values(self):
        #test blocks
        self.assertEqual(list(results.keys()), list(results_approx.keys()))
        #test values
        for block in list(results.keys()):
            dim=len(results[block]['values'][0])-1
            for value in results[block]['values']:
                for value_approx in results_approx[block]['values']:
                    if list(value[:dim]) == list(value_approx[:dim]):
                        try:
                            value[dim]/value_approx[dim]
                            #check: print (block, value[:dim], value[dim], value_approx[dim])
                            self.assertAlmostEqual(value[dim]/value_approx[dim], 1, places=10)
                        except:
                            self.assertAlmostEqual(value[dim], 0, places=10)
                            self.assertAlmostEqual(value_approx[dim], 0, places=10)
                            
        
if __name__ == '__main__':
    unittest.main()