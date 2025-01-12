# Diagonalization

If you have a Matrix A, where A = [
    [1, 1]
    [4, 1]
]

and its eigenvalues are λ₁ = 3 and λ₂ = -1
and its eigenvectors x₁ = [1, 2] and x₂ = [1, -2]

you can create the matrix S, which has the eigenvectors as its columns.  S =[
    [1, 1]
    [2, -2]
]

Now if you multiply AS, the resulting columns are a linear column of A and the respective eigenvector. AS = M.  Mⱼ = Axⱼ

so AS = [
    [3, -1]
    [6, 2]
]

For eigenvectors, Ax = λx.  so for each column, where Mⱼ= Axⱼ, Mⱼ= λxⱼ.  The resulting matrix Λ satisfies AS = SΛ. so A = SΛS^-1 and (S^-1)AS = Λ.

Knowing this, and that SS^1 === 𝟙, if you square A ... A^2 = SΛ(S^-1)SΛ(S^-1), the right side simplifies to S(Λ^2)S^-1

All of the vectors of A need to be indepenent for this to work.
