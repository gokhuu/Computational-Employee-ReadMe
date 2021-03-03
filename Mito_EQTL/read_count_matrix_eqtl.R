#import library
library(MatrixEQTL)

#set work directory
#setwd("C:/Users/khuub/One Drive/OneDrive/Desktop/Projects/projects/Mito_EQTL");

#files in use
allele = read.csv ="allele.csv";
count_expression= "count_expression.csv";
count_expression_edit = "count_expression_no_zero.csv";
count_epression_log_norm = "count_expression_log_norm.csv";
count_epression_standard_norm = "count_expression_standard_norm.csv";

co_var = "mito_covariates.csv";

#settings for engine
useModel = modelLINEAR

covariates_applied = co_var;

output_file_name = tempfile();

pvOutputThreshold = 1e-2;

errorCovariance = numeric();

cisDist = 1e6;

#Load data
#Genotype
snps = SlicedData$new();
snps$fileDelimiter = ",";
snps$fileOmitCharacters = "NA";
snps$fileSkipRows = 1;
snps$fileSkipColumns = 1;
snps$fileSliceSize = 2000;
snps$LoadFile(allele);

#Expression - Log Standardized
gene_log = SlicedData$new();
gene_log$fileDelimiter = ",";
gene_log$fileOmitCharacters = "NA";
gene_log$fileSkipRows = 1;
gene_log$fileSkipColumns = 1;
gene_log$fileSliceSize = 2000;
gene_log$LoadFile("count_expression_log_norm.csv");

#Expression - SK Learn StandardScaler
gene_stan = SlicedData$new();
gene_stan$fileDelimiter = ",";
gene_stan$fileOmitCharacters = "NA";
gene_stan$fileSkipRows = 1;
gene_stan$fileSkipColumns = 1;
gene_stan$fileSliceSize = 2000;
gene_stan$LoadFile("count_expression_standard_norm.csv");

#covariates
cvrt_applied = SlicedData$new();
cvrt_applied$fileDelimiter = ",";      
cvrt_applied$fileOmitCharacters = "NA"; 
cvrt_applied$fileSkipRows = 1;          
cvrt_applied$fileSkipColumns = 1;       
if(length(covariates_applied)>0) {
  cvrt$LoadFile(covariates_applied);}

#Analysis
#log normalized and covariates data
me_log_cv = Matrix_eQTL_engine(
  snps = snps,
  gene = gene_log,
  cvrt = cvrt_applied,
  output_file_name = output_file_name,
  pvOutputThreshold = pvOutputThreshold,
  useModel = useModel,
  errorCovariance = errorCovariance,
  verbose = TRUE,
  pvalue.hist = TRUE,
  min.pv.by.genesnp = FALSE,
  noFDRsaveMemory = FALSE
);

unlink(output_file_name)

#log normalized and covariates data
me_log_cv_qq = Matrix_eQTL_engine(
  snps = snps,
  gene = gene_log,
  cvrt = cvrt_applied,
  output_file_name = output_file_name,
  pvOutputThreshold = pvOutputThreshold,
  useModel = useModel,
  errorCovariance = errorCovariance,
  verbose = TRUE,
  pvalue.hist = "qqplot",
  min.pv.by.genesnp = FALSE,
  noFDRsaveMemory = FALSE
);

unlink(output_file_name)

#standardized and covariates data
me_stan_cv = Matrix_eQTL_engine(
  snps = snps,
  gene = gene_stan,
  cvrt = cvrt_applied,
  output_file_name = output_file_name,
  pvOutputThreshold = pvOutputThreshold,
  useModel = useModel,
  errorCovariance = errorCovariance,
  verbose = TRUE,
  pvalue.hist = TRUE,
  min.pv.by.genesnp = FALSE,
  noFDRsaveMemory = FALSE
);

unlink(output_file_name)

#standardized and covariates data
me_stan_cv_qq = Matrix_eQTL_engine(
  snps = snps,
  gene = gene_stan,
  cvrt = cvrt_applied,
  output_file_name = output_file_name,
  pvOutputThreshold = pvOutputThreshold,
  useModel = useModel,
  errorCovariance = errorCovariance,
  verbose = TRUE,
  pvalue.hist = "qqplot",
  min.pv.by.genesnp = FALSE,
  noFDRsaveMemory = FALSE
);

unlink(output_file_name)

#analysis
#log normalized data
cat('Analysis done in: ', me_log_cv$time.in.sec, ' seconds', '\n');
cat('Detected eQTLs:', '\n');
show(me_log$all$eqtls)

#standard noramlized data
cat('Analysis done in: ', me_stan_cv$time.in.sec, ' seconds', '\n');
cat('Detected eQTLs:', '\n');
show(me_stan$all$eqtls)

#log normlized data
plot(me_log_cv)
plot(me_log_cv_qq)

#standard normalized data
plot(me_stan_cv)
plot(me_stan_cv_qq)