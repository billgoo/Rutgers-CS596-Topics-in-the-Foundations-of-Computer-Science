import numpy as np

def get_matrix():
    A = np.random.random((20, 3))
    while np.linalg.matrix_rank(A) < 3:
        A = np.random.random((20, 3))

    B = np.random.random((3, 5))
    while np.linalg.matrix_rank(B) < 3:
        B = np.random.random((20, 3))
    
    origin_matrix = np.dot(A, B)
    if np.linalg.matrix_rank(origin_matrix) == 3:
        return origin_matrix

    else:
        print("error")
    # test
    '''
    origin_matrix = np.array([[1,0,0,0,2],
                            [0,0,3,0,0],
                            [0,0,0,0,0],
                            [0,2,0,0,0]])

    '''
    return origin_matrix


def svd_factor(M):
    # SVD
    U, S, Vh = np.linalg.svd(M)
    # print(U.shape, S.shape, Vh.shape)
    # print(U,"\n",S,"\n",Vh)

    # construct matrix sigma
    # sigma = np.zeros([U.shape[1], Vh.shape[0]])
    sigma = np.zeros([U.shape[1], Vh.shape[0]])
    for i in range(S.shape[0]):
        sigma[i, i] = S[i]

    A = np.dot(np.dot(U, sigma), Vh)

    return np.linalg.matrix_rank(A)


def reconstruct_matrix(M, k):
    # SVD
    U, S, Vh = np.linalg.svd(M)
    # print(U.shape, S.shape, Vh.shape)
    # print(U,"\n",S,"\n",Vh)

    # construct matrix sigma
    # sigma = np.zeros([U.shape[1], Vh.shape[0]])
    sigma = np.zeros([U.shape[1], Vh.shape[0]])
    for i in range(S.shape[0]):
        sigma[i, i] = S[i]

    A = np.dot(np.dot(U[:, :k], sigma[:k, :k]), Vh[:k, :])

    return A


if __name__ == "__main__":
    x = np.random.randint(0, 20, size=5)
    y = np.random.randint(0, 5, size=5)
    print(x, y)

    max_rank = [0, 0, 0, 0, 0, 0]
    max_svd_rank = [0, 0, 0, 0, 0, 0]
    min_rank = [0, 0, 3, 3, 3, 3]
    min_svd_rank = [0, 0, 3, 3, 3, 3]

    dist_list = [0, 0, 0, 0, 0, 0]

    for _ in range(10000000):
        A = get_matrix()

        temp = np.array(A)
        temp[x[0], y[0]] = 0

        for i in range(1, 5):
            temp[x[i], y[i]] = 0

            rank = np.linalg.matrix_rank(temp)
            rank_svd = svd_factor(temp)

            if rank != rank_svd:
                print(_, i)
            if rank < 3:
                print("rank", _, i)
            if rank_svd < 3:
                print("rank_svd", _, i)

            max_rank[i+1] = max(rank, max_rank[i+1])
            max_svd_rank[i+1] = max(rank_svd, max_svd_rank[i+1])
            min_rank[i+1] = min(rank, min_rank[i+1])
            min_svd_rank[i+1] = min(rank_svd, max_svd_rank[i+1])

            # reconstruct
            recons = reconstruct_matrix(temp, 3)
            dist = np.linalg.norm(A - recons)
            dist_list[i+1] += dist


    print(max_rank)
    print(max_svd_rank)
    print(min_rank)
    print(min_svd_rank)
    print(np.array(dist_list) / 10000000)

    '''
    A = np.zeros([20, 5])
    A[0,0],A[0,1],A[1,2],A[1,3],A[2,4] = 1,1,1,1,1
    print(np.linalg.matrix_rank(A))
    A[1,2],A[1,3],A[2,4] = 0,0,0
    print(np.linalg.matrix_rank(A))
    '''
