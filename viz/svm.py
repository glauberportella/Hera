def show():
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 5, 0]
    y = [0, 5, 9, 12, 13, 12, 9, 5, 0, 1, 0, 7]
    X = list(map(lambda x: [x], X))

    import pylab

    pylab.scatter(X, y)

    import numpy as np
    from sklearn.kernel_ridge import KernelRidge
    from sklearn.svm import SVR
    from sklearn.neighbors import KNeighborsRegressor, RadiusNeighborsRegressor

    for regressor in [
        [KernelRidge(kernel="laplacian"), "laplacian"],
        [SVR(C=5), "svr_5"],
        [KNeighborsRegressor(n_neighbors=1), "knr"],
    ]:
        model = regressor[0]
        model.fit(X, y)

        print("")
        print(regressor[1])
        print(model.score(X, y))

        test_x = np.linspace(-1, 10, 100)
        test_y = []
        for x in test_x:
            test_y.append(model.predict([[x]])[0])

        pylab.plot(test_x, test_y, label=regressor[1])
    pylab.legend(loc="best")
    pylab.show()


show()
