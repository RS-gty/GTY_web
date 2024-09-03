
import numpy as np
import matplotlib.pyplot as plt
import time

lens = 5
num = 10000
t = np.linspace(0, lens, num)
x = np.cos(2 * np.pi * t + 0.5) + 0.1*np.cos(2 * np.pi * 100 * t)
X = np.fft.fft(x)
A = (X.real ** 2 + X.imag ** 2) ** 0.5 * 2 / num

k = np.fft.fftfreq(num, lens/num)

R = np.random.randn(19, 19)

W = [np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(0.0), np.float64(851.9275398441116), np.float64(782.9684562718293), np.float64(712.495009415182), np.float64(640.6435041273056), np.float64(567.5529106063769), np.float64(493.3645956090947), np.float64(418.2220490289032), np.float64(342.27060636779277), np.float64(265.65716763845137), np.float64(188.52991324044845), np.float64(111.03801735998353), np.float64(33.33135944752138), np.float64(-44.43976566864688), np.float64(-122.12493847223354), np.float64(-199.57390568995567), np.float64(-276.63687090098904), np.float64(-353.1647842628217), np.float64(-429.00963079311794), np.float64(-504.0247166500331), np.float64(-578.0649528572678), np.float64(-650.9871359251031), np.float64(-722.6502248246583), np.float64(-792.9156137796667), np.float64(-861.6474003481558), np.float64(-928.7126482755249), np.float64(-993.981644610624), np.float64(-1057.3281505875564), np.float64(-1118.6296457879373), np.float64(-1177.7675651113916), np.float64(-1234.6275280959487), np.float64(-1289.0995601447976), np.float64(-1341.0783052315248), np.float64(-1390.463229672435), np.float64(-1437.1588165718274), np.float64(-1481.0747505641518), np.float64(-1522.126092495725), np.float64(-1560.23344370815), np.float64(-1595.3230996056946), np.float64(-1627.3271922096092), np.float64(-1656.1838214236614), np.float64(-1681.837174757015), np.float64(-1704.2376352728727), np.float64(-1723.3418775541159), np.float64(-1739.1129515003227), np.float64(-1751.5203537940895), np.float64(-1760.5400868984304), np.float64(-1766.1547054711496), np.float64(-1768.353350106413), np.float64(-1767.1317683382567), np.float64(-1762.4923228654125), np.float64(-1754.443986981539), np.float64(-1743.0023272197004), np.float64(-1728.189473244658), np.float64(-1710.0340750512055), np.float64(-1688.5712475513394), np.float64(-1663.842502657428), np.float64(-1635.8956689927525), np.float64(-1604.7847993846988), np.float64(-1570.5700663195307), np.float64(-1533.3176455609364), np.float64(-1493.0995881574593), np.float64(-1449.9936810863555), np.float64(-1404.083296803418), np.float64(-1355.4572319897536), np.float64(-1304.2095358074068), np.float64(-1250.4393279959822), np.float64(-1194.2506071621297), np.float64(-1135.7520496326472), np.float64(-1075.0567992602678), np.float64(-1012.2822485886653)]
print(np.modf(21.35124)[0])
PHI = np.angle(X)
plt.plot(W)
plt.plot(k, A)
plt.show()