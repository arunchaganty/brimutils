#!/usr/bin/env Rscript

argv <- commandArgs(trailingOnly=TRUE)
outname <- 'plot'
if (length(argv) > 0) {
    outname <- argv[1]
}

d <- read.table('stdin')
if (ncol(d) == 1) {
    d <- cbind(1:nrow(d), d)
}
pdf(file=paste(outname, '.pdf', sep=''), title=outname)
plot(d, 'x', 'y', main=outname, type='o')
dev.off()
