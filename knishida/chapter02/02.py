import numpy as np
import matplotlib.pyplot as plt

n=np.arange(21)
omega=0.1*2*np.pi
x1=np.array(np.sin(omega*n))
x2=np.array(np.sin((omega+2*np.pi)*n))
x3=np.array(x1-x2)
print(x3)

ax1=plt.subplot(2,2,1)
ax2=plt.subplot(2,2,3)
ax3=plt.subplot(2,2,2)
ax4=plt.subplot(2,2,4)

ax1.plot(n,x1)
ax2.plot(n,x2)
ax3.plot(n,x3)
ax4.plot(n,x3)

ax4.set_ylim(-1,1)

ax1.set_xlabel("Time[sample]")
ax1.set_ylabel("Amplitude")
ax2.set_xlabel("Time[sample]")
ax2.set_ylabel("Amplitude")
ax3.set_xlabel("Time[sample]")
ax3.set_ylabel("Amplitude")
ax4.set_xlabel("Time[sample]")
ax4.set_ylabel("Amplitude")

ax1.set_title("sin(ωn)")
ax2.set_title("sin((ω+2π)n)")
ax3.set_title("error(w/o setting measurement range)")
ax4.set_title("error(w setting measurement range)")

plt.tight_layout()

plt.show()