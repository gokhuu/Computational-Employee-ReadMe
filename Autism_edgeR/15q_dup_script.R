#load working directory and library
setwd("C:/Users/khuub/One Drive/OneDrive/Desktop/Projects/projects/Autism_edgeR/")
library(edgeR)

#Import data
counts <- read.csv("15q_dup_fpkm_avg_threshold_no_index.csv",header=TRUE)
m <- as.matrix(counts)
group <- as.factor(rep(c("Control","Case"),c(12,4)))
co <- read.csv('15qdup_pc1.csv',header=FALSE)

#Create DGE List Obj
d <- DGEList(counts = m, group=group)

#Clean Data
keep <- filterByExpr(d,group=group)
d <- d[keep,,keep.lib.sizes=FALSE]


#Normalize Data
d <- calcNormFactors(d, method = "TMM")


#Create design Matrix, apply covariates
design <- model.matrix(~group+0,co)


#Test
d <- estimateDisp(d,design)
de.com <- exactTest(d,pair = c("Case","Control"))

#Results
topTags(de.com)
hist(de.com$table$PValue,prob=TRUE)
