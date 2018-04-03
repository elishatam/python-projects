import numpy as np
import matplotlib.pyplot as plt
import requests
from scipy.optimize import minimize

def get_white_point(X, Y, Z, sf):
    Xw = np.sum(X)
    Yw = np.sum([y*s for (y,s) in zip(Y, sf)])
    Zw = np.sum(Z)
    xw = Xw/(Xw + Yw + Zw)
    yw = Yw/(Xw + Yw + Zw)

    return xw, yw

def get_xy_obj(X, Y, Z, sf, xt, yt):
    [x, y] = get_white_point(X, Y, Z, sf)
    d = (x - xt) ** 2 + (y - yt) ** 2
    return d

def correct_white_point(D, xt, yt):
    X = []
    Y = []
    Z = []
    for i in range(1, 4):
        X.append(D[i][0] / D[i][2] * D[i][1])
        Y.append(D[i][0])
        Z.append(D[i][0] / D[i][2] * (1 - D[i][1] - D[i][2]))

    f = plt.figure()
    ax = f.add_subplot(111)
    plot_locus_CIE1932(ax)
    ax.scatter([xt], [yt], marker='x')

    sf0 = [1, 1, 1]
    [xw0, yw0] = get_white_point(X, Y, Z, sf0)

    ax.scatter(xw0, yw0, marker='o')

    def objective_function(sf):     
        return get_xy_obj(X, Y, Z, sf, xt, yt)

    opt_res = minimize(objective_function, np.array(sf0), method='COBYLA')
    sf_opt = opt_res.x
    sf_opt[sf_opt > 1] = 1
    [xw_opt, yw_opt] = get_white_point(X, Y, Z, sf_opt)
    ax.scatter(xw_opt, yw_opt, marker='v')

    plt.legend(['locus', 'planck', 'target', 'original', 'optimized'])
    # formatting cie plot size
    # ax.set_xlim(0, 0.8)
    # ax.set_ylim(0, 0.85)

    print('Best: ({:.2f}, {:.2f}, {:.2f})\t{}, {}\n'.format(sf_opt[0], sf_opt[1], sf_opt[2], xw_opt, yw_opt))

    return sf_opt, (xw_opt, yw_opt)

def plot_locus_CIE1932(plt_ax):
    x = [0.175596, 0.172787, 0.170806, 0.170085, 0.160343, 0.146958, 0.139149,
         0.133536, 0.126688, 0.115830, 0.109616, 0.099146, 0.091310, 0.078130,
         0.068717, 0.054675, 0.040763, 0.027497, 0.016270, 0.008169, 0.004876,
         0.003983, 0.003859, 0.004646, 0.007988, 0.013870, 0.022244, 0.027273,
         0.032820, 0.038851, 0.045327, 0.052175, 0.059323, 0.066713, 0.074299,
         0.089937, 0.114155, 0.138695, 0.154714, 0.192865, 0.229607, 0.265760,
         0.301588, 0.337346, 0.373083, 0.408717, 0.444043, 0.478755, 0.512467,
         0.544767, 0.575132, 0.602914, 0.627018, 0.648215, 0.665746, 0.680061,
         0.691487, 0.700589, 0.707901, 0.714015, 0.719017, 0.723016, 0.734674,
         0.175596]

    y = [0.005295, 0.004800, 0.005472, 0.005976, 0.014496, 0.026643, 0.035211,
         0.042704, 0.053441, 0.073601, 0.086866, 0.112037, 0.132737, 0.170464,
         0.200773, 0.254155, 0.317049, 0.387997, 0.463035, 0.538504, 0.587196,
         0.610526, 0.654897, 0.675970, 0.715407, 0.750246, 0.779682, 0.792153,
         0.802971, 0.812059, 0.819430, 0.825200, 0.829460, 0.832306, 0.833833,
         0.833316, 0.826231, 0.814796, 0.805884, 0.781648, 0.754347, 0.724342,
         0.692326, 0.658867, 0.624470, 0.589626, 0.554734, 0.520222, 0.486611,
         0.454454, 0.424252, 0.396516, 0.372510, 0.351413, 0.334028, 0.319765,
         0.308359, 0.299317, 0.292044, 0.285945, 0.280951, 0.276964, 0.265326,
         0.005295]

    plt_ax.plot(x, y, 'k-', linewidth=2)
    plot_planckian_locus(plt_ax)
    plt.axis('equal')


def plot_planckian_locus(ax_plt):
    T = np.linspace(1667, 25000, 100)
    xp = np.zeros((100,))
    yp = np.zeros((100,))
    mask = np.where(T < 4000)[0]
    xp[mask] = -0.2661239 * 10**9 / (T[mask]**3) - 0.2343580 * 10**6 / (T[mask]**2) + 0.8776956 * 10**3 / T[mask] + 0.179910
    mask = np.where(T >= 4000)[0]
    xp[mask] = -3.0258469 * 10**9 / (T[mask]**3) + 2.1070379 * 10**6 / (T[mask]**2) + 0.2226347 * 10**3 / T[mask] + 0.240390
    
    mask = np.where(T < 2222)[0]
    yp[mask] = -1.1063814 * xp[mask]**3 - 1.34811020 * xp[mask]**2 + 2.18555832 * xp[mask] - 0.20219683
    mask = np.where(np.logical_and(T >= 2222, T <= 4000))[0]
    yp[mask] = -0.9549476 * xp[mask]**3 - 1.37418593 * xp[mask]**2 + 2.09137015 * xp[mask] - 0.16748867
    mask = np.where(T > 4000)[0]
    yp[mask] = 3.0817580 * xp[mask]**3 - 5.87338670 * xp[mask]**2 + 3.75112997 * xp[mask] - 0.37001483

    ax_plt.plot(xp, yp, 'k--', linewidth=1)

def set_display_color(url, col):
    requests.post(url + "/" + col)
