import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt
from rdkit.Chem import AllChem as Chem
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import PandasTools
from rdkit.Chem import Draw
from rdkit import DataStructs
import matplotlib
import matplotlib.pyplot as plt
import os
if __name__ == "__main__":
    os.system('export DISPLAY=:0.0')
    x = [0,1]
    plt.plot(x)
    print('test matplot')
matplotlib.use('TkAgg')
data = pd.read_csv('molecules.csv', sep = ',')
print(data.head())
len(data.index)
print(data.dtypes)
PandasTools.AddMoleculeColumnToFrame(data,'SMILES_parent','Molecule',includeFingerprints=True)
print([str(x) for x in  data.columns])
print(data.dtypes)
print(data.head())
cols = list(data.columns.values)
data = data[['Mol_ID',
 'Molecule',
 'SMILES_parent',
 'Name']]
print(data.head())
PandasTools.FrameToGridImage(data,column= 'Molecule', molsPerRow=4,subImgSize=(150,150),legendsCol="Mol_ID")
fplist = [] #fplist
for mol in data['Molecule']:
    fp = Chem.GetMorganFingerprintAsBitVect( mol,2,2048 )
    fplist.append(fp)
data['mfp2']=fplist
data.head(3)
fp1=data.at[0,'mfp2']
fp2=data.at[1,'mfp2']
from rdkit import DataStructs
DataStructs.DiceSimilarity(fp1,fp2)
for r in data.index:
#r =0
    fp1 = data.at[r,'mfp2']
    colname = data.at[r,'Mol_ID']
    simlist = [] #fplist
    for mol in data['Molecule']:
        fp = Chem.GetMorganFingerprintAsBitVect( mol,2 )
        sim =DataStructs.DiceSimilarity(fp1,fp)
        simlist.append(sim)
    data[colname]=simlist
data.head(1)
#difficult to view dataframe so remove fingerprint column and others
newdata = data.drop(['mfp2','SMILES_parent',"Name"], axis=1)
newdata
print(newdata)
import seaborn as sns
cm = sns.light_palette("red", as_cmap=True)
s = newdata.style.background_gradient(cmap=cm)
plt.show()


