import pandas as pd

x= ['Control.PGP1','Control.PGP1','Control.PGP1','Control.GM23716','Control.GM23716','Control.GM23716','Control.GM23720','Control.GM23720','Control.GM23720','Control.GM25256','Control.GM25256','Control.GM25256','Control.BXS0110','Control.BXS0110','Control.BXS0110','Control.BXS0111','Control.BXS0111','Control.BXS0111','Control.BYS0112','Control.BYS0112','Control.BYS0112','Control.BXS0114','Control.BXS0114','Control.BXS0114','Control.BXS0115','Control.BXS0115','Control.BXS0115','Control.BXS0116','Control.BXS0116','Control.BXS0116','Control.BXS0117','Control.BXS0117','Control.BXS0117','Control.902','Control.902','Control.902','Case.1601-1','Case.1601-2','Case.1601-3','Case.1401-1','Case.1401-2','Case.1401-3','Case.1001-1','Case.1001-2','Case.1001-3','Case.901-1','Case.901-2','Case.901-3']

df = pd.DataFrame(x)
df.to_csv(r'workspace.csv')