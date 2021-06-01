#python3

import allel as al

x = al.read_vcf('ED1.Filtered.Variants.vcf', ['CHROM', 'POS', 'INFO'])
print(x)