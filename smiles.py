
import pandas as pd
from rdkit import Chem

input_file = "peptide.csv"
output_file = "peptide_smiles.csv"

records = []

df = pd.read_csv(input_file)

for sequence in df["SEQUENCE"]:

    mol = Chem.MolFromFASTA(sequence)

    if mol is not None:

        smiles = Chem.MolToSmiles(
            mol,
            canonical=True,
            isomericSmiles=True
        )

        status = "Success"

    else:
        smiles = None
        status = "Conversion Failed"

    records.append({
        "Sequence": sequence,
        "SMILES": smiles,
        "Status": status
    })

output_df = pd.DataFrame(records)

output_df.to_csv(output_file, index=False)

print("Conversion completed!")
print(output_df.head())
