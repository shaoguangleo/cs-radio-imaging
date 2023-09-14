import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 输入因变量

y1 = [0.10328447913966561, 0.03694517481024262, 0.05973352394081078, 0.07494466655080423, 0.08005347830555609, 0.08123809982070965]
# y2 = [96.81996833694228, 270.67134074644076, 167.41018008428364, 133.431776539043, 124.91649596824517, 123.09495202460099]
# y3 = [2.7640645681100144, 4.8402260539494, 9.507928595854944,14.873118545907015, 19.600989169628228, 20.275848895492736]

# y1 = [0.07729219886539293, 0.08117809333449758, 0.08181049573384902, 0.0820723210775889, 0.08219637667761205, 0.08219637667761205]
# y2 = [129.37916305648582, 123.18594326667171, 122.23370498245873, 121.84375766034785, 121.65986390399755, 121.65986390399755]
# y3 = [16.625862255125202, 22.903535916786602, 24.7617798594012,26.02869499928156, 26.78982312976979, 26.78982312976979]

y2 = [105.84648457186086, 146.80578010063223, 170.0968215094016, 194.69126137722338, 198.86539642563923, 206.83322383298406,194.91217543206514,175.9157073689354,154.7755103721758,140.6482204021047,131.6482204021047,118.22452317097205,108,105.33]
y3 = [16.566407916910535, 19.49575673900615, 21.074936373404462,21.96986181655856, 22.54416110092999, 22.997629207772356,23.40011383945066,24.266668681461297,25.433917835630247,26.192591907949808,26.692591907949808,27.07885132103806,27.09,27.12885]

# y2 = [50.54500736130311, 51.630719085354, 52.83116571943757, 53.954277988389926, 55.018400515358394, 56.205936795550876,60.58306270302328,97.32582810902026,146.03209510374626,140.6482204021047,127.58741115872111,94.49820948633418, 105.60054041846824, 149.55213813389273]
# y3 = [1.6569777067371985, 1.7772083862970391, 1.8990048140843554,2.021497614805043, 2.1452190310534522, 2.269930363617992,2.7711854942431104,4.834064681293969,7.395039567308989,9.482043755587496,11.174351744465653,14.32262092410519, 16.566336303436323, 19.203427248228444]

# y2 = [50.54500736130311, 51.630719085354, 52.83116571943757, 53.954277988389926, 55.018400515358394, 56.205936795550876,60.58306270302328,97.32582810902026,146.03209510374626,140.6482204021047,127.58741115872111,94.49820948633418, 105.60054041846824, 149.55213813389273, 157.33118578023158, 163.05797303282415, 168.09547453986792,172.1323678205872,175.9650184839477,178.92969302862065,178.90800030414172,173.92270288613776,178.9300000308449,159.00744272825392,156.12801093248237,151.097207832778,155.8193635945391]
# y3 = [1.6569777067371985, 1.7772083862970391, 1.8990048140843554,2.021497614805043, 2.1452190310534522, 2.269930363617992,2.7711854942431104,4.834064681293969,7.395039567308989,9.482043755587496,11.174351744465653,14.32262092410519, 16.566336303436323, 19.203427248228444,19.51184915852568, 19.768190227397678, 19.989060700511875,20.16592669134472,20.305610705074663,20.517622457286574,20.57308626976492,20.5046062338012,20.32804968515330,19.262171458333903,18.802215999363996,18.580639094684514,  18.04572438595322]


fig, ax = plt.subplots(figsize=(6, 6), dpi=300)


# 设置自变量的范围和个数
# x = ["10", "20", "40", "80", "160","320"]
x = [1,2,3,4,5,6,7,10,20,30,40,50,75,100]
# x = [1,2,3,4,5,6,10,20,30,40,50,75,100,150,160,170,180,190,200,225,250,275,300,400,800,1000,4000]



# x = ["1","2","3","4","5","6", "10", "20", "30","40","50","75","100","150"]
# x = ["1", "5", "10", "20", "30","40"]
# 画图
# ax.plot(x, y1, label='RMSE', linestyle='-', marker='*', markersize='10')
# ax.plot(x, y3, label='SNR', linestyle='--', marker='p', markersize='10')
# ax.plot(x, y2, label='DR', linestyle='-.', marker='o', markersize='10')

ax.plot(x, y3, label='SNR', markersize='10')
ax.plot(x, y2, label='DR', markersize='10')



# 设置坐标轴
# ax.set_xlim(0, 9.5)
# ax.set_ylim(-2, 4.2)

# ax.set_xscale("log")
# ax.set_yscale("log")
# ax.set_xlim(0.01e-1, 0.01e2)
ax.set_ylim(10e1, 10e3)
# ax.set_aspect(1)
# ax.set_title("adjustable = box")

# ax.set_ylim(0, 3.2)
# ax.set_ylim(0.5, 2.9)
# ax.set_xlabel("$n$",fontsize=16)
ax.set_xlabel("$n_{re}$",fontsize=16)
# ax.set_xlabel("Iterations", fontsize=16)
ax.set_ylabel("Value", fontsize=16)
# 设置刻度
ax.tick_params(axis='both', labelsize=16)
# 显示网格
# ax.grid(True, linestyle='-.')
# ax.yaxis.grid(True, linestyle='-.')
# 添加图例
legend = ax.legend(loc='best')
plt.subplots_adjust(left=0.129, right=0.985, bottom=0.138, top=0.946)
plt.xscale('log')
plt.yscale('log')
# 'linear', 'log', 'symlog', 'asinh', 'logit', 'function', 'functionlog'

plt.title("$n = 100$")
# plt.title("$n_{re} = 1$")
plt.show()
fig.savefig('Assessment_analysis.eps')