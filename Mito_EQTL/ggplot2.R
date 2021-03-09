library(ggplot2)

data = read.csv('fpkm_log2_pvalues.csv')

plt = ggplot(data,aes(x=fpkm_log2_pvalues))+geom_histogram(binwidth = 0.01, fill="#69b3a2", color="#e9ecef")

plt