import numpy as np

def PPCA(data, q, sigma_init = 1, EM = False):
    N = data.shape[0]  # N row, N t_i
    d = data.shape[1]  # d cột của data
    mean = np.mean(data.T, axis=1) # mean vector
    mean = np.array([mean]).T # chuyển vecto mean về vecto cột
    S = (data.T -  mean).dot((data.T -  mean).T) / N # hiệp phương sai sample S
    if EM == False:
      eig_vals, eig_vecs = np.linalg.eig(S) # hàm riêng và trị riêng của S
      # xếp các trị riêng hàm riêng tương ứng thành các tuple
      eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]
      # xếp lại theo thứ tự theo giá trị trị riêng
      eig_pairs.sort()
      eig_pairs.reverse()
      # tìm MLE cho lambda
      lambda_ = 0
      for i in range(q, d):
        lambda_ += eig_pairs[i][0]
      sigma_ML = 1/(d-q)*lambda_
      # tìm ma trận U_q
      U_q = eig_pairs[0][1]
      for i in range(1, q):
        U_q = np.vstack((U_q, eig_pairs[i][1]))
      U_q = U_q.T
      # tìm ma trận Delta_q
      eig_vals_for_delta = np.array(eig_pairs[0][0])
      for i in range(1, q):
        eig_vals_for_delta = np.append(eig_vals_for_delta, eig_pairs[i][0])
      Delta_q = np.diag((eig_vals_for_delta))
      # tính ma trận W với giả định R = I
      W = np.matrix.round( U_q.dot(  np.sqrt(Delta_q - sigma_ML*np.identity(q)) ), 2 )
    else:
        sigma = sigma_init
        W = np.random.rand(d, q)
        while True:
            M = W.T.dot(W) + sigma * np.identity(q)
            M_inv = np.linalg.inv(M)

            W_ml = S.dot(W).dot(np.linalg.inv(sigma*np.identity(q) + M_inv.dot(W.T).dot(S).dot(W)))
            sigma_ML = (1/d) * np.trace(S - S.dot(W).dot(M_inv).dot(W_ml.T))
            sigma_ML = np.absolute(sigma_ML)
            if abs((sigma - sigma_ML)) <= 0.000001:
                break
            W = W_ml
            sigma = sigma_ML
    return (W, sigma_ML, mean)
