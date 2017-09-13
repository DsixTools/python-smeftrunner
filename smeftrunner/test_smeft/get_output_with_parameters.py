# -*- coding: utf-8 -*-


from smeftrunner import SMEFT
smeft = SMEFT()

smeft.scale_in = 1e4
smeft.scale_high = 1e4

with open('SMInput-CPV.dat', 'r') as f1:
  with open('WCsInput-CPV-SMEFT.dat', 'r') as f2:
    smeft.load_initial((f1, f2,))
    

C_out = smeft.rgevolve(scale_out=160)
C_out_approx = smeft.rgevolve_leadinglog(scale_out=160)

smeft.dump(C_out, open('my_output_file.dat', 'w'))
smeft.dump(C_out, open('my_output_file_approx.dat', 'w'))
