# Linear Algebra Project Report: Topic PPCA
* This report is about the studies of PPCA. The report file is "Report_Linear- PPCA.pdf". There also is a application code file in this repository

### Group nembers:
* Trần Trung Việt
* Lê Hoài Nam
* Huỳnh Hữu Nhật
* Huỳnh Hoàng Trung Nghĩa

### Instructor
* Dr. Nguyễn Phúc Sơn


## Introduction 
Principal component analysis (PCA) (Jolliffe 1986) is an extremely popular technique to reduce dimension in multivariate analysis. The most common definition of PCA, introduced by Hotelling (1933),  for a set of observed $d$-dimensional data vectors <img src="https://render.githubusercontent.com/render/math?math=\{\textbf{t}_n\}, n \in \{1...N\}">, the <img src="https://render.githubusercontent.com/render/math?math=q"> principal axes <img src="https://render.githubusercontent.com/render/math?math=\textbf{w}_j , j \in \{1...q\}"> , are those orthonormal axes onto which the retained variance under projection is maximal. One limiting disadvantage of these definitions of PCA is the absence of an associated probability density or generative model. Deriving PCA from the perspective of density estimation would offer a number of important advantages including the following:

* The corresponding likelihood would permit comparison with other density-estimation techniques and facilitate statistical testing.
* Bayesian inference methods could be applied by combining the likelihood with a prior.
* In classification, PCA could be used to model class-conditional densities, thereby allowing the posterior probabilities of class membership to be computed.
* The value of the probability density function could be used as a measure of the ‘degree of novelty’ of a new data point.
* The probability model would offer a methodology for obtaining a principal component projection when data values are missing.
* The single PCA model could be extended to a mixture of such models.

M.E Tipping and C.M Bishop introduces a probability formula of PCA from the Gaussian latent variable model that is closely related to statistical factor analysis and is discussed in Section 2. The PPCA model is described in detail in Section 3, the principal axes emerge as maximum likelihood parameter estimates which may be computed by the usual eigen-decomposition of the sample covariance matrix and subsequently incorporated in the model. Alternatively, the latent variable formulation leads naturally to an iterative, and computationally efficient, expectation–maximization (EM) algorithm for effecting PCA are presented in Section 3.5.
